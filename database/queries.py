CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    user_code VARCHAR(6) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('Admin', 'User', 'Guest')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_FLIGHTS_TABLE = """
CREATE TABLE IF NOT EXISTS flights(
    flight_id SERIAL PRIMARY KEY,
    flight_code VARCHAR(6) UNIQUE NOT NULL,
    airline VARCHAR(100) NOT NULL,
    journey_date DATE NOT NULL,
    source VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    route VARCHAR(100) NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    duration VARCHAR(50) NOT NULL,
    total_stops VARCHAR(30) NOT NULL,
    additional_information VARCHAR(255),
    fare DECIMAL(10,2) NOT NULL
);
"""

# DECIMAL(10,2): (stores up to 10 digits, 2 decimal places).

CREATE_PREDICTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS predictions(
    prediction_id SERIAL PRIMARY KEY,
    prediction_code VARCHAR(6) UNIQUE NOT NULL,
    user_id INTEGER NOT NULL,
    flight_id INTEGER NOT NULL,
    predicted_fare DECIMAL(10,2) NOT NULL,
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_prediction_user
        FOREIGN KEY(user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_prediction_flight
        FOREIGN KEY(flight_id)
        REFERENCES flights(flight_id)
        ON DELETE CASCADE
);
"""

# --------------- USER queries ---------------
INSERT_DEFAULT_ADMIN = """INSERT INTO users (user_code, username, email, password, role) VALUES (%s, %s, %s, %s, %s);"""           # check this for user_code in db_connection
EXISTS_ADMIN = """SELECT EXISTS(SELECT 1 FROM users WHERE role = 'Admin');"""

INSERT_USER = """INSERT INTO users (user_code, username, email, password, role) VALUES (%s, %s, %s, %s, %s) RETURNING user_id, created_at;"""
GET_USER_BY_ID = """SELECT * FROM users WHERE user_id = %s;"""
GET_USER_BY_USERNAME = """SELECT * FROM users WHERE username = %s;"""
GET_USER_BY_EMAIL = """SELECT * FROM users WHERE email = %s;"""
GET_USER_BY_LOGIN = """SELECT * FROM users WHERE username = %s OR email = %s;"""
GET_ALL_USERS = """SELECT * FROM users ORDER BY user_id;"""
UPDATE_USER = """UPDATE users SET username = %s, email = %s, password = %s, role = %s WHERE user_id = %s;"""
UPDATE_PASSWORD = """UPDATE users SET password = %s WHERE user_id = %s;"""
DELETE_USER = """DELETE FROM users WHERE user_id = %s;"""

EXISTS_USER_CODE = """SELECT EXISTS(SELECT 1 FROM users WHERE user_code=%s);"""

# -------------- FLIGHT queries --------------
INSERT_FLIGHT = """
INSERT INTO flights(
    flight_code,
    airline,
    journey_date,
    source,
    destination,
    route,
    departure_time,
    arrival_time,
    duration,
    total_stops,
    additional_information,
    fare)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""
GET_FLIGHT_BY_ID = """SELECT * FROM flights WHERE flight_id = %s;"""
GET_ALL_FLIGHTS = """SELECT * FROM flights ORDER BY flight_id;"""
SEARCH_FLIGHTS = "SELECT * FROM flights WHERE 1=1"
DELETE_ALL_FLIGHTS = """DELETE FROM flights;"""
EXISTS_FLIGHT_CODE = """SELECT EXISTS(SELECT 1 FROM flights WHERE flight_code=%s);"""

# ------------ PREDICTION queries ------------

INSERT_PREDICTION = """INSERT INTO predictions (user_id, flight_id, prediction_code, predicted_fare) VALUES (%s, %s, %s, %s) RETURNING prediction_id, prediction_time;"""
GET_PREDICTION_BY_ID = """SELECT * FROM predictions WHERE prediction_id = %s;"""
GET_ALL_PREDICTIONS = """SELECT * FROM predictions ORDER BY prediction_time DESC;"""
DELETE_PREDICTION = """DELETE FROM predictions WHERE prediction_id = %s;"""
GET_PREDICTIONS_BY_USER = """SELECT * FROM predictions WHERE user_id = %s ORDER BY prediction_time DESC;"""
EXISTS_PREDICTION_CODE = """SELECT EXISTS(SELECT 1 FROM predictions WHERE prediction_code=%s);"""