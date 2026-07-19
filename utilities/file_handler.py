import os
import pickle
import pandas as pd

class FileHandler:
    @staticmethod
    def read_csv(file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

    @staticmethod
    def save_csv(dataframe: pd.DataFrame, file_path: str):
        FileHandler.create_directory(os.path.dirname(file_path))
        dataframe.to_csv(file_path, index=False)

    @staticmethod
    def save_pickle(obj: object, file_path: str):
        FileHandler.create_directory(os.path.dirname(file_path))
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