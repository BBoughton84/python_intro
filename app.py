# import sqlite3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

#app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models
# from models import cars

@app.route('/api/v1/songs', methods=['GET'])
def index():
    return jsonify(data=[car.serialize for car in models.cars.query.all()])
    #list comprehension


@app.route('/api/title')
def title():
    return jsonify(data=[x.serialize for x in models.cars.query.filter_by(title = 'Truck')])

@app.route('/test')
def test():
    return models.cars.query.all()

if __name__ == '__main__':
    app.debug = True
    app.run()
