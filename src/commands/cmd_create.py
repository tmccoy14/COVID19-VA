"""Standard library"""
import os

"""Third party modules"""
import click

"""Internal application modules"""
from src.main import pass_environment
from src.database import init_db


@click.command("create", short_help="Create the Virginia Covid-19 table.")
@pass_environment
def cli(ctx):
    """Create the table for covid-19 va data"""

    ctx.log("Creating Covid-19 Database Tables...")

    init_db()

    ctx.log("Done...")
