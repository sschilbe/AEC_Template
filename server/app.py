from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import json
import os

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# Favicon to display in
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
