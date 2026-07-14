import logging

logging.basicConfig(
    filename="flight_fare_prediction.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",                       # Append to existing log file
    datefmt="%d-%m-%Y %H:%M:%S"
)

class ApplicationLogger:
    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def warning(message: str):
        logging.warning(message)

    @staticmethod
    def error(message: str):
        logging.error(message)

    @staticmethod
    def debug(message: str):
        logging.debug(message)

# How to use:
# ApplicationLogger.info("Model trained successfully.")