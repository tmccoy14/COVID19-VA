"""Standard library"""
import os

"""Third party modules"""
import click
from sqlalchemy import func

"""Internal application modules"""
from src.main import pass_environment
from src.database import db_session
from src.models import VaCovid


@click.command("total", short_help="Get the total Virginia Covid-19 case data.")
@click.option(
    "--locality", "-l", required=False, help="Virginia Locality.",
)
@pass_environment
def cli(ctx, locality):
    """Data visualization of all covid-19 va data."""

    ctx.log("Total Covid-19 Virginia Cases...")

    if locality:
        values = db_session.query(
            func.sum(VaCovid.total_cases).label("total_cases")
        ).filter(VaCovid.locality == locality.upper())

        for _res in values.all():
            if _res[0] is None:
                print(
                    "No available Virginia Covid-19 case data for {}".format(
                        locality.capitalize()
                    )
                )
            else:
                print(
                    "Total cases for {} as of today are: {}".format(
                        locality.capitalize(), _res[0]
                    )
                )
    else:
        values = db_session.query(func.sum(VaCovid.total_cases).label("total_cases"))

        for _res in values.all():
            print("Total cases as of today are: {}".format(_res[0]))
