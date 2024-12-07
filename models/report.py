from utils.db import db


class Report(db.Model):
    Aadhar_number = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    description = db.Column(db.Integer, nullable=False)
