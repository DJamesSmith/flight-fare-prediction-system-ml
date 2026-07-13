import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from database.db_connection import DatabaseConnection
from database.queries import (
    CREATE_USERS_TABLE,
    CREATE_FLIGHTS_TABLE,
    CREATE_PREDICTIONS_TABLE,
    INSERT_DEFAULT_ADMIN,
    EXISTS_ADMIN,
    EXISTS_USER_CODE,
)

from models.user import User
from repositories.base_repository import BaseRepository
from utilities.logger import ApplicationLogger
from utilities.password_hasher import HashPassword

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

class DatabaseInitializer:
    @staticmethod
    def create_database():
        connection = psycopg2.connect(
            host=DB_HOST,
            database="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (DB_NAME,))
        database_exists = cursor.fetchone()
        if not database_exists:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            ApplicationLogger.info(f"Database '{DB_NAME}' created successfully.")
        else:
            ApplicationLogger.info(f"Database '{DB_NAME}' already exists.")
        cursor.close()
        connection.close()

    @staticmethod
    def create_tables():
        with DatabaseConnection() as db:
            db.cursor.execute(CREATE_USERS_TABLE)
            db.cursor.execute(CREATE_FLIGHTS_TABLE)
            db.cursor.execute(CREATE_PREDICTIONS_TABLE)
        ApplicationLogger.info("All database tables are ready: Users, Flight, Prediction")

    @staticmethod
    def create_default_admin():
        with DatabaseConnection() as db:
            db.cursor.execute(EXISTS_ADMIN)
            admin_exists = db.cursor.fetchone()[0]
            if admin_exists:
                ApplicationLogger.info("Administrator already exists.")
                return
            repository = BaseRepository()
            user_code = repository.generate_unique_code(EXISTS_USER_CODE)
            hashed_password = HashPassword.hash_password("Admin@123")
            db.cursor.execute(INSERT_DEFAULT_ADMIN, (user_code, "admin", "admin@flightfareprediction.com", hashed_password, User.ADMIN))
            ApplicationLogger.info("Default administrator created.")

    @classmethod
    def initialize_database(cls):
        cls.create_database()
        cls.create_tables()
        cls.create_default_admin()