# import sqlite3
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json


#app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models

@app.route('/cars', methods=['GET'])
def index():
    carHolder = []
    cars = models.cars.query.all()
    for car in cars:
        carHolder.append({
        'id':car.id,
        'make':car.make,
        'model':car.model,
        'year':car.year
        })
    return render_template("carDisplay.html", cars = carHolder)
    #list comprehension

@app.route('/cars/<car>')
def cars(car):
    return jsonify(data=[x.serialize for x in models.cars.query.filter_by(model = car )])

@app.route('/cars/<int:id>')
def specificCar(id):
    return jsonify(data=[models.cars.query.get(id).serialize])

@app.route('/bikes')
def bikes():
    bikeHolder = []
    bikes =  models.motorcycles.query.all()
    for bike in bikes:
        bikeHolder.append({
        'id':bike.id,
        'manufacture':bike.manufacture,
        'model':bike.model,
        'size':bike.size,
        'year':bike.year
        })
    return render_template("bikeDisplay.html", bikes = bikeHolder)

@app.route('/bikes/<int:id>')
def specificBike(id):
    return jsonify(data=[models.motorcycles.query.get(id).serialize])

@app.route('/postnew', methods=['GET', 'POST'])
def addNew():
    if request.method == 'POST':
        print("above json loads")
        x = json.loads(request.data)
        print(x["id"])
        print(x["body"])
        return request.data
    else:
        return "this is not a post, you probably did GET"

@app.route('/delete/<int:id>')
def delete(id):
    models.motorcycles.query.filter_by(id=id).delete()
    db.session.commit()
    pass



if __name__ == '__main__':
    app.debug = True
    app.run()
