import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Logger:
    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def warning(message: str):
        logging.warning(message)

    @staticmethod
    def error(message: str):
        logging.error(message)

# How to use:
# Logger.info("Model trained successfully.")

# ------------------------------------------------------------
# Is it okay if add these in logging.basicConfig() ?
# filename="audit.log",
# filemode="a",                       # Append to existing log file
# datefmt="%d-%m-%Y %H:%M:%S"


# Can i add this too ? What does this do ?
# logger = logging.getLogger(__name__)