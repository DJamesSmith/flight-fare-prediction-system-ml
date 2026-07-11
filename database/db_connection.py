# PostgreSQL connection
# Executing SQL queries
# CRUD operations
# Returning model objects

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from models.user import User
from utilities.logger import ApplicationLogger
from utilities.password_hasher import HashPassword
from database.queries import CREATE_USERS_TABLE, CREATE_FLIGHTS_TABLE, CREATE_PREDICTIONS_TABLE, GET_ADMIN, INSERT_DEFAULT_ADMIN

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
    with DatabaseConnection() as db:
        db.cursor.execute(CREATE_USERS_TABLE)
        db.cursor.execute(CREATE_FLIGHTS_TABLE)
        db.cursor.execute(CREATE_PREDICTIONS_TABLE)
    ApplicationLogger.info("All database tables are ready.")

def create_default_admin():
    with DatabaseConnection() as db:
        db.cursor.execute(GET_ADMIN, ("admin",))
        if db.cursor.fetchone() is None:
            hashed_password: str = HashPassword.hash_password("Admin@123")
            db.cursor.execute(INSERT_DEFAULT_ADMIN, ("admin", hashed_password, User.ADMIN))
            ApplicationLogger.info("Default administrator created.")
        else:
            ApplicationLogger.info("Default administrator already exists.")

def initialize_database():
    create_database()
    create_tables()
    create_default_admin()

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
            ApplicationLogger.warning(f"Database Transaction rolled back: {exc_value}")
            self.connection.rollback()
        else:
            self.connection.commit()

        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()


# Introduce BaseRepository to hold shared behavior of flight, user and prediction repos.