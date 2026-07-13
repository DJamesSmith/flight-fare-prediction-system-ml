# PostgreSQL connection
# Executing SQL queries
# CRUD operations
# Returning model objects

import os
import psycopg2
from dotenv import load_dotenv
from utilities.logger import ApplicationLogger

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Context manager responsible only for opening and closing PostgreSQL connections
# Custom Context Manager responsible only for opening and closing PostgreSQL connections
class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.connection.rollback()
            ApplicationLogger.warning(f"Database transaction rolled back: {exc_value}")
        else:
            self.connection.commit()
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Introduce BaseRepository to hold shared behavior of flight, user and prediction repos.