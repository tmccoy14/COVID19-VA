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

    url = "http://www.vdh.virginia.gov/content/uploads/sites/182/2020/03/VDH-COVID-19-PublicUseDataset-Cases.csv"

    filename = wget.download(url)

    os.rename(
        "VDH-COVID-19-PublicUseDataset-Cases.csv",
        "data/VDH-COVID-19-PublicUseDataset-Cases.csv",
    )

