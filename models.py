from app import db

class cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @property
    def serialize(self):
        return {
        'id': self.id,
        'make': self.make,
        'model': self.model,
        'year': self.year
        }

class motorcycles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String)
    model = db.Column(db.String)
    size = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def __init__(self, manufacture, model, size, year):
        self.manufacture = manufacture
        self.model = model
        self.size = size
        self.year = year

    @property
    def serialize(self):
        return {
        'id': self.id,
        'manufacture': self.manufacture,
        'model': self.model,
        'size': self.size,
        'year': self.year
        }


    # def __repr__(self):
    #     return '<car %r, %s>' %self.model %self.make
