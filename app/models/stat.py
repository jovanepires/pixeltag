from .db import db

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, tag_id, ip):
        self.tag_id = tag_id
        self.ip = ip

    def __repr__(self):
        return "<Stats(hash='%s' date='%s')>" % self.hash % self.date
