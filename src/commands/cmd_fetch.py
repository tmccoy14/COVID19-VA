"""Standard library"""
import os

"""Third party modules"""
import click
import wget

"""Internal application modules"""
from src.main import pass_environment


@click.command("fetch", short_help="Fetch the Virginia Covid-19 case data.")
@pass_environment
def cli(ctx):
    """Fetch covid-19 va data from the source."""

    ctx.log("Fetching Covid-19 Virginia Cases...")

    url = "https://data.virginia.gov/api/views/bre9-aqqr/rows.csv?accessType=DOWNLOAD"

    filename = wget.download(url)

    os.rename(
        "VDH-COVID-19-PublicUseDataset-Cases.csv",
        "data/VDH-COVID-19-PublicUseDataset-Cases.csv",
    )

    ctx.log("Done...")
