"""Standard library"""
import os

"""Third party modules"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class DB(Base):
    """DB consists of the database connection URL and sessionmaker"""

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
