from models import cars
from app import db

db.session.query(cars).delete()
db.session.commit()

car = cars('Truck', 'maker', 2014)
db.session.add(car)
car = cars('Car', 'maker', 2015)
db.session.add(car)
car = cars('Coupe', 'maker', 2016)
db.session.add(car)
car1 = cars('SUV', 'maker', 2017)
car2 = cars('Convertable', 'maker', 2018)
car3 = cars('Limo', 'maker', 2019)
car4 = cars('Luxury', 'maker', 2011)


db.session.add(car1)
db.session.add(car2)
db.session.add(car3)
db.session.add(car4)

db.session.commit()
