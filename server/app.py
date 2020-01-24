from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
import copy
import json
import os, pdb

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
ma = Marshmallow(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# classes
class City():
    def __init__(self, name, num_rows, num_cols, grid_data):
        self.name = name
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid_data = grid_data

class CitySchema(ma.Schema):
    class Meta:
        fields = ('name', 'num_rows', 'num_cols', 'grid_data')

list_of_cities = []
cities_schema = CitySchema(many=True)

class CCS():
    def __init__(self, name, cost, radii):
        self.name = name
        self.cost = cost
        self.radii = radii

class CCSSchema(ma.Schema):
    class Meta:
        fields = ('name', 'cost', 'radii')

list_of_ccs = []
ccs_schema = CCSSchema(many=True)

# parses in city data from text files and adds to list_of_cities
@app.before_first_request
def parse_city_data():
    directory_str = './data/cities/'
    directory = os.fsencode(directory_str)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        data_file = open(directory_str + filename)
        data_file_lines = data_file.readlines()
        city = parse_city_from_data_lines(data_file_lines)
        data_file.close()
        list_of_cities.append(city)

    return cities_schema.jsonify(list_of_cities)

# builds and returns a City object based on the list of data provided
def parse_city_from_data_lines(city_data_lines):
    name = city_data_lines[0].rstrip()
    num_rows = int(city_data_lines[2])
    num_cols = int(city_data_lines[3])
    grid_data = build_grid_data(num_rows, num_cols, city_data_lines)
    city = City(name, num_rows, num_cols, grid_data)
    return city

# builds and returns a 2-D list representing the grid of data for the city
def build_grid_data(num_rows, num_cols, city_data_lines):
    grid_data = []
    grid_id = 1
    for i in range(4, num_rows+4):
        grid_data_line = city_data_lines[i].split(',')
        new_li = []
        n = len(grid_data_line)
        for j in range(0, n-1, 2):
            value = float(grid_data_line[j])
            acceptable_location = grid_data_line[j+1]
            new_dict = {}
            new_dict["id"] = grid_id
            new_dict["value"] = value
            new_dict["acceptable_location"] = bool(int(acceptable_location))
            new_li.append(new_dict)
            grid_id += 1 # iterate id 
        grid_data.append(new_li)
    return grid_data
    

@app.before_first_request
def parse_ccs_data():
    ccs_data_file = open('./data/CCS/carbonCapture.txt', 'r')
    ccs_data_lines = ccs_data_file.readlines()
    list_of_ccs.extend( parse_ccs_list_from_data_lines(ccs_data_lines) )
    ccs_data_file.close()

    return ccs_schema.jsonify(list_of_ccs)

def parse_ccs_list_from_data_lines(ccs_data_lines):
    new_li = []
    for i, ccs in enumerate(ccs_data_lines):
        ccs_data = ccs_data_lines[i].split(', ')
        name = ccs_data[0]
        cost = float(ccs_data[1])
        radii = []
        for j in range(2, len(ccs_data)):
            radii.append(float(ccs_data[j].rstrip()))
        new_ccs = CCS(name, cost, radii)
        new_li.append(new_ccs)
    return new_li

@app.route('/cityGrid/<city_name>')
def city_grid(city_name):
    city = next( city for city in list_of_cities if city.name == city_name )
    budget = 1750000
    carbon_capture_percentage = 21
    
    # Get the original grid for the given city
    grid = city.grid_data
    grid_copy = copy.deepcopy( grid )
    
    updated_grid, total_spent, actual_carbon_capture_percent = get_filled_grid( grid_copy, city, budget, carbon_capture_percentage )

    for row in updated_grid:
        for column in row:
            del column['acceptable_location']

    data = json.dumps({
        'city': city.name,
        'dimensions': {
            'length': len( updated_grid ),
            'width': len( updated_grid[0] )
        },
        'grid': updated_grid,
        'results': {
            'budget': budget,
            'totalSpent': total_spent,
            'targetCarbonCapture': carbon_capture_percentage,
            'actualCarbonCapture': actual_carbon_capture_percent
        }
    })

    return data

def get_filled_grid( grid, city, budget, target_carbon_capture_percentage ):
    # Calculate the total carbon emitted for that city
    total_carbon = 0
    for row in grid:
        for column in row:
            total_carbon += column['value']
            column['originalValue'] = column['value']
            column['updatedValue'] = column['originalValue']
            del column['value']

    # Initialize all needed variables
    budget_remaining = budget
    total_carbon_reduction = 0
    current_reduction = 0

    # Keep looping while targets have not been met
    while( budget_remaining > 0 and ( ( total_carbon_reduction / total_carbon ) * 100 ) < target_carbon_capture_percentage):
        placed = False
        lowest = None

        # Loop through each Row
        for i, row in enumerate( grid ):
            # Loop through each column in row
            for j, column in enumerate( row ):
                # Can a device be placed here
                if column['acceptable_location']:
                    # Try each device in the device list
                    for device in list_of_ccs:
                        if budget_remaining - device.cost > 0:
                            # Have enough money to try this device
                            carbon_per_dollar, current_reduction = calculate_carbon_per_dollar( grid, i, j, device )
                            if lowest == None:
                                placed = True
                                lowest = { 'row': i, 'column': j, 'device': device, 'carbonPerDollar': carbon_per_dollar, 'reduction': current_reduction }
                            else:
                                if carbon_per_dollar > lowest['carbonPerDollar']:
                                    lowest = { 'row': i, 'column': j, 'device': device, 'carbonPerDollar': carbon_per_dollar, 'reduction': current_reduction }
                    # End devices for
            # End column for
        # End row for

        if not placed:

            # Could not place a device anywhere so we should exit the equation
            break

        # Update calculated values with this device placement
        budget_remaining -= lowest['device'].cost
        total_carbon_reduction += lowest['reduction']
        grid[lowest['row']][lowest['column']]['acceptable_location'] = False
        grid[lowest['row']][lowest['column']]['deviceAtLocation'] = {}
        grid[lowest['row']][lowest['column']]['deviceAtLocation']['name'] = lowest['device'].name
        grid[lowest['row']][lowest['column']]['deviceAtLocation']['radii'] = len( lowest['device'].radii ) - 1

        # Update the grid values with the impact of placing this device
        radius = len( lowest['device'].radii ) - 1
        center_x = lowest['row']
        center_y = lowest['column']

        for x in range( center_x - radius, center_x + radius):
            for y in range( center_y - radius, center_y + radius ):
                distance = dist( center_x, center_y, x, y )
                if valid_spot( distance, radius, x, y , len( grid ), len( grid[0] ) ):
                    grid[x][y]['updatedValue'] -= grid[x][y]['originalValue'] * ( lowest['device'].radii[distance] / 100 )
                    grid[x][y]['updatedValue'] = round( grid[x][y]['updatedValue'], 1 )
    # End while

    return grid, budget - budget_remaining, round( ( ( total_carbon_reduction / total_carbon ) * 100 ), 2 )

def calculate_carbon_per_dollar( grid, i, j, device ):
    # Iterate in a circle around the spot
    radius = len( device.radii ) - 1
    center_x = i
    center_y = j
    carbon_reduction = 0

    for x in range( center_x - radius, center_x + radius):
        for y in range( center_y - radius, center_y + radius ):
            distance = dist( center_x, center_y, x, y )
            if valid_spot( distance, radius, x, y , len( grid ), len( grid[0] ) ):
                carbon_reduction += grid[x][y]['originalValue'] * ( device.radii[distance] / 100 )

    carbon_per_dollar = carbon_reduction/device.cost
    return carbon_per_dollar, carbon_reduction

def valid_spot( distance, radius, x, y , xMax, yMax ):
    return distance <= radius and x >= 0 and y >=0 and x < xMax and y < yMax

def dist(x1, y1, x2, y2):
    return abs( x1 - x2 ) + abs( y1 - y2 )

if __name__ == '__main__':
    app.run()
