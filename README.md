# Flight Fare Prediction System using Machine Learning

A machine learning-based Flight Fare Prediction application developed using **Core Python** and **PostgreSQL**. This project demonstrates the complete workflow of data preprocessing, feature engineering, model training, fare prediction, and database integration through a clean, modular MVC-inspired architecture.

---

## Features

- Flight fare prediction using Machine Learning
- Data preprocessing and validation
- Feature engineering
- Model training and evaluation
- Fare prediction based on user inputs
- PostgreSQL database integration
- Modular MVC-inspired architecture
- Repository Pattern implementation
- Command Line Interface (CLI)

---

## Tech Stack

- Python
- Machine Learning
- Pandas
- NumPy
- Scikit-learn
- PostgreSQL
- Psycopg2

---

## Architecture

The project follows a modular MVC-inspired architecture to improve code organization, maintainability, and scalability.

- **Controllers** – Handle application flow and user interactions.
- **Services** – Implement business logic, preprocessing, model training, and prediction.
- **Models** – Represent the application's data models.
- **Database Layer** – Manage PostgreSQL operations using the Repository Pattern.
- **Views** – Display menus and user interactions.
- **Utilities** – Common helper functions and constants.
- **Validation** – Input and dataset validation.

---

## Project Structure

```text
flight-fare-prediction-system-ml/
│
├── controllers/
├── database/
├── models/
├── notes/
├── services/
├── utilities/
├── validation/
├── views/
├── Flight Fare Prediction_SRS.pdf
├── index.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Application Workflow

1. Load the flight dataset.
2. Validate and preprocess the dataset.
3. Perform feature engineering.
4. Train the Machine Learning model.
5. Evaluate model performance.
6. Store prediction history in PostgreSQL.
7. Predict flight fares based on user inputs.

---

## Requirements

- Python 3.x
- PostgreSQL
- pip
- Git

---

## Installation

### Clone the repository

```bash
git clone https://github.com/DJamesSmith/flight-fare-prediction-system-ml.git
```

### Navigate to the project

```bash
cd flight-fare-prediction-system-ml
```

### Create a virtual environment

#### macOS / Linux

```bash
python3 -m venv flight_fare_env
source flight_fare_env/bin/activate
```

#### Windows

```bash
python -m venv flight_fare_env
flight_fare_env\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

1. Install PostgreSQL.
2. Create the required database.
3. Configure the database connection.
4. Execute the SQL scripts.
5. Run the application.

---

## Major Libraries

- Pandas
- NumPy
- Scikit-learn
- Psycopg2

---

## Screenshots

> Screenshots of the application will be added soon.

---

## Roadmap

- Build a Django web application
- Develop a REST API
- Add Docker support
- Implement model persistence
- Hyperparameter tuning
- Deploy to the cloud (AWS/Render)
- Implement CI/CD using GitHub Actions

---

## Learning Outcomes

This project demonstrates practical experience with:

- Core Python
- Object-Oriented Programming (OOP)
- Machine Learning workflow
- Data preprocessing and feature engineering
- PostgreSQL integration
- Repository Pattern
- MVC-inspired architecture
- Modular software design
- Database connectivity
- Predictive analytics

---

## Author

**Dion James Smith**

Backend Software Engineer

**Skills:** Python • Django • PostgreSQL • Machine Learning

---

## License

This project is licensed under the MIT License. See the **LICENSE** file for more information.