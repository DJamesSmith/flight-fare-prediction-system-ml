import pandas as pd
from utilities.logger import ApplicationLogger

class FeatureTransformer:
    @staticmethod
    def feature_transform(dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.copy()        # Since it already returns a new dataframe, I would make it explicit that it works on a copy rather than relying on callers to remember .copy()

        print("\nBefore conversion")
        print(dataframe.dtypes)

        dataframe["Journey_Date"] = pd.to_datetime(dataframe["Journey_Date"], errors="raise")
        dataframe["Departure_Time"] = pd.to_datetime(dataframe["Departure_Time"].astype(str), format="%H:%M:%S", errors="raise")
        dataframe["Arrival_Time"] = pd.to_datetime(dataframe["Arrival_Time"].astype(str), format="%H:%M:%S", errors="raise")

        print("\nAfter conversion")
        print(dataframe.dtypes)

        # From: Journey_Date - create: Journey_Day, Journey_Month
        dataframe["Journey_Day"] = dataframe["Journey_Date"].dt.day
        dataframe["Journey_Month"] = dataframe["Journey_Date"].dt.month

        dataframe["Departure_Hour"] = dataframe["Departure_Time"].dt.hour
        dataframe["Departure_Minute"] = dataframe["Departure_Time"].dt.minute

        dataframe["Arrival_Hour"] = dataframe["Arrival_Time"].dt.hour
        dataframe["Arrival_Minute"] = dataframe["Arrival_Time"].dt.minute

        duration = (
            dataframe["Duration"]
            .str.extract(r"(?:(\d+)h)?\s*(?:(\d+)m)?")
            .fillna(0)
            .astype(int))
        dataframe["Duration_Minutes"] = (duration[0] * 60 + duration[1])

        stop_mapping: dict[str, int] = {
            "Non-Stop": 0,
            "1 Stop": 1,
            "2 Stops": 2,
            "3 Stops": 3,
            "4 Stops": 4
        }
        dataframe["Total_Stops"] = (dataframe["Total_Stops"].replace(stop_mapping))
        dataframe.drop(columns=["Journey_Date", "Departure_Time", "Arrival_Time", "Duration"], inplace=True)
        ApplicationLogger.info("Feature engineering completed successfully.")
        return dataframe
    
# How to use:
# self.dataframe = FeatureTransformer.feature_transform(self.dataframe)

# 1. airline
# 2. journey_date
# 3. source
# 4. destination
# 5. route
# 6. departure_time
# 7. arrival_time
# 8. duration
# 9. total_stops
# 10. additional_information
# 11. fare