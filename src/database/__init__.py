"""Standard library"""
import os

"""Third party modules"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


# Create database engine and database session
engine = create_engine("postgresql://postgres@localhost/covid_db", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

# Initialize database with tables
def init_db():
    """Internal application modules"""
    import src.models

    Base.metadata.create_all(bind=engine)
