import os
import pickle
import pandas as pd

class FileHandler:
    @staticmethod
    def read_csv(file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

    @staticmethod
    def save_csv(dataframe: pd.DataFrame, file_path: str):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        dataframe.to_csv(file_path, index=False)

    @staticmethod
    def save_pickle(obj: object, file_path: str):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            pickle.dump(obj, file)

    @staticmethod
    def load_pickle(file_path: str):
        with open(file_path, "rb") as file:
            return pickle.load(file)

    @staticmethod
    def file_exists(file_path: str) -> bool:
        return os.path.exists(file_path)

    @staticmethod
    def create_directory(directory_path: str):
        os.makedirs(directory_path, exist_ok=True)


# pd.read_csv() - internally opens the file, reads it, parses it, and closes it automatically.
# df.to_csv() - opens, writes, flushes, and closes the file.

# ------------------------------------------------------------------------

# Adding more functionality as the project grows:
# save_pickle()
# load_pickle()
# create_directory()
# file_exists()

# Why add these now?
# Later, in training_service.py, instead of writing:
# import pickle
# with open(MODEL_PATH, "wb") as file:
#     pickle.dump(model, file)
# you simply write:
# FileHandler.save_pickle(model, MODEL_PATH)

# Instead of
# with open(MODEL_PATH, "rb") as file:
#     model = pickle.load(file)
# you write
# model = FileHandler.load_pickle(MODEL_PATH)

# Instead of
# if os.path.exists(DATASET_PATH):
# you write
# if FileHandler.file_exists(DATASET_PATH):

# Instead of
# os.makedirs("reports/graphs", exist_ok=True)
# you write
# FileHandler.create_directory("reports/graphs")