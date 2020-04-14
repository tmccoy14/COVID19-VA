"""Standard library"""
import os

"""Third party modules"""
import click
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

"""Internal application modules"""
from src.main import pass_environment


engine = create_engine(
    os.environ.get("DATABASE_URL", "postgresql://postgres@localhost/covid_db")
)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


@click.group(
    "virginia", short_help="List the Virginia Covid-19 case data.",
)
@pass_environment
def cli(ctx):
    """Data listing of all covid-19 va data."""


class VaCovid(Base):
    """VaCovid models the va_covid table that will be necessary for
    interacting with datasets involved in coronavirus."""

    __tablename__ = "va_covid"
    id = Column(Integer, primary_key=True, autoincrement=True)
    report_date = Column(String(10), nullable=False, unique=False)
    fips = Column(String(5), nullable=False, unique=True)
    locality = Column(String(50), nullable=True)
    health_district = Column(String(50), nullable=True)
    total_cases = Column(String(6), nullable=True)


@cli.command("list")
@pass_environment
def list(ctx):
    ctx.log("Finding all VA Covid-19 cases...")
    values = Session.query(VaCovid).all()

    results = [
        [
            value.report_date.upper(),
            value.fips.upper(),
            value.locality.upper(),
            value.health_district.upper(),
            value.total_cases.upper(),
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
