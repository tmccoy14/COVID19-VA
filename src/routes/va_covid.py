from flask import request
from flask_restx import Namespace, Resource, fields

from src.server.extensions import db
from src.models import VaCovid as va_covid

api = Namespace("VaCovid", description="VA Covid-19 Cases")

va_covid = api.model(
    "VaCovid",
    {
        "report_date": fields.String(
            required=True, description="VA Covid-19 cases report date."
        ),
        "fips": fields.String(required=True, description="Va Covid-19 area code."),
        "locality": fields.String(
            required=True, description="VA Covid-19 region affected."
        ),
        "health_district": fields.String(required=True, description="Notes"),
        "total_cases": fields.String(
            required=True, description="Total cases in region."
        ),
    },
)

# ROUTE: /vacovid/
@api.route("/")
class CovidCrud(Resource):
    @api.doc("List all va covid cases")
    @api.marshal_with(va_covid)
    def get(self):
        """List all va covid cases"""
        return va_covid.query.all()
