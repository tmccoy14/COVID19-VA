"""Third party modules"""
import click
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify

"""Internal application modules"""
from src.main import pass_environment


@click.command("visualize", short_help="Visualize the Virginia Covid-19 case data.")
@pass_environment
def cli(ctx):
    """Data visualization of all covid-19 va data."""

    ctx.log("Visualizig Covid-19 Virginia Cases...")

    data = pd.read_csv("data/VDH-COVID-19-PublicUseDataset-Cases.csv")

    location = data["Locality"]
    cases = data["Total Cases"]

    x = []
    y = []

    x = list(location)
    y = list(cases)

    # Make fake dataset
    height = y
    bars = x
    y_pos = np.arange(len(bars))

    # Create horizontal bars
    plt.barh(y_pos, height)

    # Create names on the y-axis
    plt.yticks(y_pos, bars)

    plt.autoscale(enable=True)

    # Show graphic
    plt.show()
