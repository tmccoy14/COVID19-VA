"""Standard library"""
import os

"""Third party modules"""
import click
from sqlalchemy import func

"""Internal application modules"""
from src.main import pass_environment
from src.database import db_session
from src.models import VaCovid


@click.command("total", short_help="List the Virginia Covid-19 case data.")
@pass_environment
def cli(ctx):
    """Data visualization of all covid-19 va data."""

    ctx.log("Total Covid-19 Virginia Cases...")

    values = db_session.query(func.sum(VaCovid.total_cases).label("total_cases"))

    for _res in values.all():
        print("Total cases as of today are: {}".format(_res[0]))
