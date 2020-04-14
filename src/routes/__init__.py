from flask_restx import Api

# IMPORT ROUTES
from src.routes.va_covid import api as va_covid

api = Api(title="VA Covid-19 API", version="1.0", description="Covid-19 VA Cases API")

# ADD ROUTES TO THE VA Covid-19 API
api.add_namespace(va_covid)

"""
Reasoning for importing all of these models is so that database migrations can
take place.
This will auto-inititalize db.Models (as tables) with Flask-Migrate and the
'db' commands.
"""
from src.models import *
