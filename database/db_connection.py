# # PostgreSQL connection
# # Executing SQL queries
# # CRUD operations
# # Returning model objects

# import os
# import psycopg
# from dotenv import load_dotenv

# load_dotenv()

# class DatabaseConnection:
#     def __init__(self):
#         self.connection = None

#     def connect(self):
#         if self.connection is None:
#             self.connection = psycopg.connect(
#                 host=os.getenv("DB_HOST"),
#                 port=os.getenv("DB_PORT"),
#                 dbname=os.getenv("DB_NAME"),
#                 user=os.getenv("DB_USER"),
#                 password=os.getenv("DB_PASSWORD")
#             )
#         return self.connection

#     def disconnect(self):
#         if self.connection is not None:
#             self.connection.close()
#             self.connection = None

#     def get_connection(self):
#         return self.connect()

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from database.queries import CREATE_USERS_TABLE, CREATE_FLIGHTS_TABLE, CREATE_PREDICTIONS_TABLE

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Creates the project database if it does not already exist
def create_database():
    connection = psycopg2.connect(
        host=DB_HOST,
        database="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname=%s;", (DB_NAME,))
    database_exists = cursor.fetchone()
    if not database_exists:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully.")
    else:
        print(f"Database '{DB_NAME}' already exists.")

    cursor.close()
    connection.close()

# Creates all required project tables
def create_tables():
    with DatabaseConnection() as cursor:
        cursor.execute(CREATE_USERS_TABLE)
        cursor.execute(CREATE_FLIGHTS_TABLE)
        cursor.execute(CREATE_PREDICTIONS_TABLE)

    print("All database tables are ready.")

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
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Database Error: {exc_value}")
            self.connection.rollback()
        else:
            self.connection.commit()

        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()