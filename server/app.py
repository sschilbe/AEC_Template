from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
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
    halifax_data_file = open('./data/cities/Halifax.txt', 'r')
    halifax_data_lines = halifax_data_file.readlines()
    halifax = parse_city_from_data_lines(halifax_data_lines)
    halifax_data_file.close()

    saintjohn_data_file = open('./data/cities/SaintJohn.txt', 'r')
    saintjohn_data_lines = saintjohn_data_file.readlines()
    saintjohn = parse_city_from_data_lines(saintjohn_data_lines)
    saintjohn_data_file.close()
    
    stjohns_data_file = open('./data/cities/SaintJohn.txt', 'r')
    stjohns_data_lines = stjohns_data_file.readlines()
    stjohns = parse_city_from_data_lines(stjohns_data_lines)
    stjohns_data_file.close()

    list_of_cities.append(halifax)
    list_of_cities.append(saintjohn)
    list_of_cities.append(stjohns)

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
    for i in range(4, num_rows):
        grid_data_line = city_data_lines[i].split(',')
        new_li = []
        for j in range(0, num_cols, 2):
            value = grid_data_line[j]
            acceptable_location = grid_data_line[j+1]
            new_dict = {}
            new_dict["value"] = value
            new_dict["acceptable_location"] = bool(acceptable_location)
            new_li.append(new_dict)
        grid_data.append(new_li)
    return grid_data
    

@app.route('/parse/ccs', methods=['GET'])
def parse_ccs_data():
    ccs_data_file = open('./data/CCS/carbonCapture.txt', 'r')
    ccs_data_lines = ccs_data_file.readlines()
    list_of_ccs = parse_ccs_list_from_data_lines(ccs_data_lines)
    ccs_data_file.close()

    return ccs_schema.jsonify(list_of_ccs)

def parse_ccs_list_from_data_lines(ccs_data_lines):
    new_li = []
    for i, ccs in enumerate(ccs_data_lines):
        ccs_data = ccs_data_lines[i].split(', ')
        name = ccs_data[0]
        cost = ccs_data[1]
        radii = []
        for j in range(2, len(ccs_data)):
            radii.append(ccs_data[j].rstrip())
        new_ccs = CCS(name, cost, radii)
        new_li.append(new_ccs)
    return new_li

@app.route('/cityGrid')
def cityGrid():
    city = request.args.get('city')
    budget = 1750000
    carbonCapturePercentage = 21
    grid, totalSpent, actualCarbonCapturePercent = getFilledGrid( city, budget, carbonCapturePercentage )
    data = json.dumps({
        'city': city,
        'dimensions': {
            'length': len( grid ),
            'width': len( grid[0] )
        },
        'grid': grid,
        'results': {
            'budget': budget,
            'totalSpent': totalSpent,
            'targetCarbonCapture': carbonCapturePercentage,
            'actualCarbonCapture': actualCarbonCapturePercent
        }
    })

    return data

def getFilledGrid( city, budget, carbonCapturePercentage ):
    grid = [[]]
    totalSpent = 1500000
    actualCarbonCapturePercent = 22
    return grid, totalSpent, actualCarbonCapturePercent

if __name__ == '__main__':
    app.run()
