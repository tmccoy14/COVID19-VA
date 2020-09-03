"""Standard library"""
import os
import csv
from string import capwords

"""Third party modules"""
import click

"""Internal application modules"""
from src.main import pass_environment
from src import DB, VaCovid


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

            DB.Session.add(
                VaCovid(
                    report_date=report_date,
                    fips=fips,
                    locality=locality,
                    health_district=health_district,
                    total_cases=total_cases,
                )
            )
            DB.Session.commit()

    ctx.log("Done...")
