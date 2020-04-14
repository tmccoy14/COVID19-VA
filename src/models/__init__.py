import datetime

from src.server.extensions import db


class VaCovid(db.Model):
    __tablename__ = "va_covid"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    report_date = db.Column(db.String(10), nullable=False)
    fips = db.Column(db.String(5), nullable=False)
    locality = db.Column(db.String(50), nullable=False)
    health_district = db.Column(db.String(50), nullable=False)
    total_cases = db.Column(db.String(6), nullable=False)
