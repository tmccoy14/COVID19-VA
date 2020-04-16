import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE va_covid (
            id SERIAL PRIMARY KEY,
            report_date VARCHAR(255) NOT NULL,
            fips VARCHAR(255) NOT NULL,
            locality VARCHAR(255) NOT NULL,
            health_district VARCHAR(255) NOT NULL,
            total_cases VARCHAR(255) NOT NULL
        )
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
