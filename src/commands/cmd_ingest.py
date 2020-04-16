"""Standard library"""
import os
import csv
from string import capwords

"""Third party modules"""
import click
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

"""Internal application modules"""
from src.main import pass_environment

engine = create_engine(
    os.environ.get("DATABASE_URL", "postgresql://postgres@localhost/covid_db")
)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class VaCovid(Base):
    """VaCovid models the va_covid table that will be necessary for
    interacting with datasets involved in coronavirus."""

    __tablename__ = "va_covid"
    id = Column(Integer, primary_key=True, autoincrement=True)
    report_date = Column(String(10), nullable=False, unique=False)
    fips = Column(String(5), nullable=False, unique=True)
    locality = Column(String(50), nullable=True)
    health_district = Column(String(50), nullable=True)
    total_cases = Column(Integer, nullable=True)


@click.command("ingest", short_help="Ingest the Virginia Covid-19 case data.")
@pass_environment
def cli(ctx):
    """Data ingestion of all covid-19 va data"""

    ctx.log("Ingesting Covid-19 Virginia Cases...")

    with open(
        "data/VDH-COVID-19-PublicUseDataset-Cases.csv", newline="", encoding="utf-8-sig"
    ) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            report_date = row.get("Report Date")
            fips = capwords(row.get("FIPS", "").lower())
            locality = row.get("Locality", "").upper()
            health_district = capwords(row.get("Health District", "").lower())
            total_cases = capwords(row.get("Total Cases", "").lower())

            Session.add(
                VaCovid(
                    report_date=report_date,
                    fips=fips,
                    locality=locality,
                    health_district=health_district,
                    total_cases=total_cases,
                )
            )
            Session.commit()

    ctx.log("Done...")
