CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK(role IN ('Admin', 'User')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_FLIGHTS_TABLE = """
CREATE TABLE IF NOT EXISTS flights(
    flight_id SERIAL PRIMARY KEY,
    airline VARCHAR(100) NOT NULL,
    source VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    journey_date DATE NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    duration VARCHAR(50) NOT NULL,
    total_stops VARCHAR(30) NOT NULL,
    additional_information VARCHAR(255)
);
"""

CREATE_PREDICTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS predictions(
    prediction_id SERIAL PRIMARY KEY,
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
INSERT_USER = """INSERT INTO users (username, password, role) VALUES (%s, %s, %s) RETURNING user_id, created_at;"""
GET_USER_BY_ID = """SELECT user_id, username, password, role, created_at FROM users WHERE user_id = %s;"""
GET_USER_BY_USERNAME = """SELECT user_id, username, password, role, created_at FROM users WHERE username = %s;"""
GET_ALL_USERS = """SELECT user_id, username, password, role, created_at FROM users ORDER BY user_id;"""
UPDATE_USER = """UPDATE users SET username = %s, password = %s, role = %s WHERE user_id = %s;"""
UPDATE_PASSWORD = """UPDATE users SET password = %s WHERE user_id = %s;"""
DELETE_USER = """DELETE FROM users WHERE user_id = %s;"""
EXISTS_BY_USERNAME = """SELECT EXISTS( SELECT 1 FROM users WHERE username = %s);"""
AUTHENTICATE_USER = """SELECT user_id, username, password, role, created_at FROM users WHERE username = %s AND password = %s;"""


# -------------- FLIGHT queries --------------



# ------------ PREDICTION queries ------------
