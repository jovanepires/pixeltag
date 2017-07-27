import datetime
from .db import db

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.String(100), nullable=False)
    user_agent = db.Column(db.String(250), nullable=False)
    cookies = db.Column(db.String(2000), nullable=False)
    accept_languages = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, tag_id, ip, user_agent, cookies, accept_languages):
        self.tag_id = tag_id
        self.ip = ip
        self.user_agent = user_agent
        self.cookies = cookies
        self.accept_languages = accept_languages

    def __repr__(self):
        return "<Stats(hash='%s' date='%s')>" % self.hash % self.date
