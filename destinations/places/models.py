from destinations.app import db


class Place(db.Model):
    """ Place Table Is to store places Visited so far """
    __tablename__ = "places"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(256))
    is_visited = db.Column(db.Boolean())

    def __repr__(self):
        return f"Name : {self.name}"

    @property
    def serialized(self):
        return {
            "name": self.name,
            "id": self.id,
            "country": self.country,
            "is_visited": True
        }
