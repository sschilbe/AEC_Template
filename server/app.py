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
@app.route('/parse/cities', methods=['GET'])
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
    for i in range(4, num_rows+4):
        grid_data_line = city_data_lines[i].split(',')
        new_li = []
        n = len(grid_data_line)
        for j in range(0, n-1, 2):
            value = float(grid_data_line[j])
            acceptable_location = grid_data_line[j+1]
            new_dict = {}
            new_dict["value"] = value
            new_dict["acceptable_location"] = bool(int(acceptable_location))
            new_li.append(new_dict)
        grid_data.append(new_li)
    return grid_data
    

@app.route('/parse/ccs', methods=['GET'])
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

@app.route('/cityGrid/<cityName>')
def cityGrid(cityName):
    parse_city_data()
    parse_ccs_data()

    city = next( city for city in list_of_cities if city.name == cityName )
    budget = 1750000
    carbonCapturePercentage = 21
    
    # Get the original grid for the given city
    grid = city.grid_data
    gridCopy = copy.deepcopy( grid )
    
    updatedGrid, totalSpent, actualCarbonCapturePercent = getFilledGrid( gridCopy, city, budget, carbonCapturePercentage )

    for row in updatedGrid:
        for column in row:
            del column['acceptable_location']

    data = json.dumps({
        'city': city.name,
        'dimensions': {
            'length': len( updatedGrid ),
            'width': len( updatedGrid[0] )
        },
        'grid': updatedGrid,
        'results': {
            'budget': budget,
            'totalSpent': totalSpent,
            'targetCarbonCapture': carbonCapturePercentage,
            'actualCarbonCapture': actualCarbonCapturePercent
        }
    })

    return data

def getFilledGrid( grid, city, budget, targetcarbonCapturePercentage ):
    # Calculate the total carbon emitted for that city
    totalCarbon = 0
    for row in grid:
        for column in row:
            totalCarbon += column['value']
            column['originalValue'] = column['value']
            column['updatedValue'] = column['originalValue']
            del column['value']

    # Initialize all needed variables
    budgetRemaining = budget
    totalCarbonReduction = 0
    currentReduction = 0

    # Keep looping while targets have not been met
    while( budgetRemaining > 0 and ( ( totalCarbonReduction / totalCarbon ) * 100 ) < targetcarbonCapturePercentage):
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
                        if budgetRemaining - device.cost > 0:
                            # Have enough money to try this device
                            carbonPerDollar, currentReduction = calculateCarbonPerDollar( grid, i, j, device )
                            if lowest == None:
                                placed = True
                                lowest = { 'row': i, 'column': j, 'device': device, 'carbonPerDollar': carbonPerDollar, 'reduction': currentReduction }
                            else:
                                if carbonPerDollar > lowest['carbonPerDollar']:
                                    lowest = { 'row': i, 'column': j, 'device': device, 'carbonPerDollar': carbonPerDollar, 'reduction': currentReduction }
                    # End devices for
            # End column for
        # End row for

        if not placed:

            # Could not place a device anywhere so we should exit the equation
            break

        # Update calculated values with this device placement
        budgetRemaining -= lowest['device'].cost
        totalCarbonReduction += lowest['reduction']
        grid[lowest['row']][lowest['column']]['acceptable_location'] = False
        grid[lowest['row']][lowest['column']]['deviceAtLocation'] = {}
        grid[lowest['row']][lowest['column']]['deviceAtLocation']['name'] = lowest['device'].name
        grid[lowest['row']][lowest['column']]['deviceAtLocation']['radii'] = len( lowest['device'].radii ) - 1

        # Update the grid values with the impact of placing this device
        radius = len( lowest['device'].radii ) - 1
        centerX = lowest['row']
        centerY = lowest['column']

        for x in range( centerX - radius, centerX + radius):
            for y in range( centerY - radius, centerY + radius ):
                distance = dist( centerX, centerY, x, y )
                if validSpot( distance, radius, x, y , len( grid ), len( grid[0] ) ):
                    grid[x][y]['updatedValue'] -= grid[x][y]['originalValue'] * ( lowest['device'].radii[distance] / 100 )
                    grid[x][y]['updatedValue'] = round( grid[x][y]['updatedValue'], 1 )
    # End while

    return grid, budget - budgetRemaining, round( ( ( totalCarbonReduction / totalCarbon ) * 100 ), 2 )

def calculateCarbonPerDollar( grid, i, j, device ):
    # Iterate in a circle around the spot
    radius = len( device.radii ) - 1
    centerX = i
    centerY = j
    carbonReduction = 0

    for x in range( centerX - radius, centerX + radius):
        for y in range( centerY - radius, centerY + radius ):
            distance = dist( centerX, centerY, x, y )
            if validSpot( distance, radius, x, y , len( grid ), len( grid[0] ) ):
                carbonReduction += grid[x][y]['originalValue'] * ( device.radii[distance] / 100 )

    carbonPerDollar = carbonReduction/device.cost
    return carbonPerDollar, carbonReduction

def validSpot( distance, radius, x, y , xMax, yMax ):
    return distance <= radius and x >= 0 and y >=0 and x < xMax and y < yMax

def dist(x1, y1, x2, y2):
    return abs( x1 - x2 ) + abs( y1 - y2 )

if __name__ == '__main__':
    app.run()

