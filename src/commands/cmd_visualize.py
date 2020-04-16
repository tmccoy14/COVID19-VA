"""Third party modules"""
import click
import matplotlib.pyplot as plt
import pandas as pd
import csv

# import pandas as pd
# import matplotlib.pyplot as plt

"""Internal application modules"""
from src.main import pass_environment


@click.command("visualize", short_help="Visualize the Virginia Covid-19 case data.")
@pass_environment
def cli(ctx):
    """Data visualization of all covid-19 va data."""

    ctx.log("Visualizig Covid-19 Virginia Cases...")

    df = pd.read_csv("data/VDH-COVID-19-PublicUseDataset-Cases.csv", sep=",")

    d = dict(zip(df.index, df.values.tolist()))

    df.plot.bar(x="Locality", y=["Total Cases"])
    plt.title("Virginia Covid-19 Cases To Date")
    plt.ylabel("Total Cases")
    plt.xlabel("Locality")
    plt.tick_params(width=2)
    plt.show()

    # x = []
    # y = []

    # with open("data/VDH-COVID-19-PublicUseDataset-Cases.csv", "r") as csvfile:
    #     plots = csv.reader(csvfile, delimiter=",")
    #     for row in plots:
    #         x.append((row[2]))
    #         y.append((row[4]))

    # plt.plot(x, y, label="Loaded from file!")
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.title("Interesting Graph\nCheck it out")
    # plt.legend()
    # plt.show()
