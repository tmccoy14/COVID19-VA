"""Standard library"""
import os

"""Third party modules"""
import click
from sqlalchemy import desc
from tabulate import tabulate

"""Internal application modules"""
from src.main import pass_environment
from src.database import db_session
from src.models import VaCovid


@click.command("list", short_help="List the Virginia Covid-19 case data.")
@pass_environment
def cli(ctx):
    """Data visualization of all covid-19 va data."""

    ctx.log("Listing Covid-19 Virginia Cases...")

    values = db_session.query(VaCovid).order_by(desc("total_cases"))

    results = [
        [
            value.report_date.upper(),
            value.fips.upper(),
            value.locality.upper(),
            value.health_district.upper(),
            value.total_cases,
        ]
        for value in values
    ]

    ctx.log("VA Covid-19 Cases:")

    print(
        tabulate(
            results,
            headers=[
                "Report Data",
                "FIPS",
                "Locality",
                "Health District",
                "Total Cases",
            ],
        )
    )
