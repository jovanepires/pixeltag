from .db import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    hash = db.Column(db.String(250), unique=True)

    def __init__(self, username, hash):
        self.username = username
        self.hash = hash

    def __repr__(self):
        return "<Tag(hash='%s')>" % self.hash
