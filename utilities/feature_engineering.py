import pandas as pd
from utilities.logger import ApplicationLogger

class FeatureTransformer:
    def __init__(self):
        pass

    def feature_transform(self, df: pd.DataFrame):
        # From: Journey_Date - create: Journey_Day, Journey_Month
        self.dataframe["Journey_Day"] = (self.dataframe["Journey_Date"].dt.day)
        self.dataframe["Journey_Month"] = (self.dataframe["Journey_Date"].dt.month)
        self.dataframe["Departure_Hour"] = (self.dataframe["Departure_Time"].dt.hour)
        self.dataframe["Departure_Minute"] = (self.dataframe["Departure_Time"].dt.minute)
        self.dataframe["Arrival_Hour"] = (self.dataframe["Arrival_Time"].dt.hour)
        self.dataframe["Arrival_Minute"] = (self.dataframe["Arrival_Time"].dt.minute)
        duration = (
            self.dataframe["Duration"]
            .str.extract(r"(?:(\d+)h)?\s*(?:(\d+)m)?")
            .fillna(0)
            .astype(int))
        self.dataframe["Duration_Minutes"] = (duration[0] * 60 + duration[1])

        stop_mapping: dict[str, int] = {
            "Non-Stop": 0,
            "1 Stop": 1,
            "2 Stops": 2,
            "3 Stops": 3,
            "4 Stops": 4
        }
        self.dataframe["Total_Stops"] = (self.dataframe["Total_Stops"].replace(stop_mapping))

        transformed_columns: list = ["Journey_Date", "Departure_Time", "Arrival_Time", "Duration"]          # Drop transformed columns
        self.dataframe.drop(columns=transformed_columns, inplace=True)
        ApplicationLogger.info("Feature engineering completed successfully.")