# import sqlite3
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import json


#app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine('postgres://localhost:5432/cars')


import models
# from models import motorcycles

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

@app.route('/bikepostnew', methods=['GET', 'POST'])
def addNew():
    if request.method == 'POST':
        incomingObject = json.loads(request.data)
        toSave = models.motorcycles(incomingObject["manufacture"], incomingObject["model"], incomingObject["size"], incomingObject["year"])
        db.session.add(toSave)
        db.session.commit()
        return request.data
    else:
        return "this is not a post, you probably did GET"


@app.route('/update/<int:carId>', methods=['GET', 'PATCH'])
def patch(carId):
    if request.method == 'PATCH':
        newItem = json.loads(request.data)
        itemToUpdate = models.cars.query.get(carId)

        itemToUpdate.make = newItem["make"]
        itemToUpdate.model = newItem["model"]
        itemToUpdate.year = newItem["year"]

        db.session.commit()

        print("inside IF")
    return "we are working on patching"


@app.route('/delete/<int:deleteId>', methods=['GET', 'DELETE'])
def delete(deleteId):
    if request.method == 'DELETE':

        engine.execute('DELETE from "motorcycles" where id=(%s)', deleteId)

        # db.session.commit()
        return "hello delete"
    else:
        return "You are not very DELETE-Y"


if __name__ == '__main__':
    app.debug = True
    app.run()
