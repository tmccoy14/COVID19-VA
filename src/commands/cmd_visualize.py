"""Standard library"""
import os

"""Third party modules"""
import click

"""Internal application modules"""
from src.main import pass_environments


@pass_environment
def cli(ctx):
    """Data visualization of all covid-19 va data."""


@cli.command("visualize")
@pass_environment
def list(ctx):
    ctx.log("Generation visualizations...")
