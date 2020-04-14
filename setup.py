from setuptools import setup, find_packages

setup(
    name="covid",
    version="0.1",
    description="Covid is a tool to help ingest, serve, and visualize Virginia Coronavirus data.",
    author="Tucker McCoy",
    author_email="tuckermmccoy@gmail.com",
    keywords="covid-19 virginia python data automation",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "Click==7.0",
        "colorama==0.4.1",
        "Flask==1.1.1",
        "Flask-Cors==3.0.8",
        "Flask-Migrate==2.5.3",
        "flask-restx==0.2.0",
        "Flask-SQLAlchemy==2.4.1",
        "gevent==1.4.0",
        "pandas==1.0.3",
        "psycopg2==2.8.4",
        "tabulate",
    ],
    entry_points={"console_scripts": ["covid=src.main:cli"]},
)
