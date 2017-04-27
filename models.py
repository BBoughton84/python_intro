from app import db

class cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    year = db.Column(db.Integer)

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    # @property
    # def serialize(self):
    #         return {
    #         'id': self.id,
    #         'artist': self.artist,
    #         'title': self.title,
    #         'year': self.year
    #         }

    @property
    def bringAll(self):
            return all(self)


    def __repr__(self):
        return '<car %r>' %self.artist
