from models import cars
from models import motorcycles
from app import db

db.session.query(motorcycles).delete()
db.session.commit()
db.session.query(cars).delete()
db.session.commit()

car = cars('GMC', 'Truck', 2014)
db.session.add(car)
car = cars('Subaru', 'Car', 2015)
db.session.add(car)
car = cars('BMW', 'Coupe', 2016)
db.session.add(car)
car1 = cars('Chevy', 'SUV', 2017)
car2 = cars('Benz', 'Convertable', 2018)
car3 = cars('Lincoln', 'Limo', 2019)
car4 = cars('Lexus', 'Luxury', 2011)

db.session.add(car1)
db.session.add(car2)
db.session.add(car3)
db.session.add(car4)

bike = motorcycles('Honda', 'CBR', 600, 2014)
db.session.add(bike)
bike = motorcycles('Triump', 'Speed Triple', 675, 2013)
db.session.add(bike)
bike = motorcycles('Honda', 'CR', 150, 2011)
db.session.add(bike)
bike = motorcycles('Harly', 'Sportster', 900, 2016)
db.session.add(bike)
bike = motorcycles('Suzuki', 'SV', 650, 2006)
db.session.add(bike)
bike = motorcycles('Yamaha', 'R1', 1000, 2012)
db.session.add(bike)
bike = motorcycles('Honda', 'Gullwing', 1800, 2011)
db.session.add(bike)


db.session.commit()
