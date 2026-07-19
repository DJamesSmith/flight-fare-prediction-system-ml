import pandas as pd
from utilities.logger import ApplicationLogger

class FeatureTransformer:
    @staticmethod
    def _ensure_datetime(series: pd.Series) -> pd.Series:
        """
        Converts a column to pandas datetime only when required.
        Handles all:
        - datetime64[ns]
        - datetime.date
        - datetime.time
        - datetime.datetime
        - "22:20"
        - "22:20:00"
        - "1900-01-01 22:20:00"
        """
        if pd.api.types.is_datetime64_any_dtype(series):
            return series
        return pd.to_datetime(series.astype(str), format="mixed", dayfirst=True, errors="raise")

    @staticmethod
    def feature_transform(dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe = dataframe.copy()            # Since it already returns a new dataframe, I would make it explicit that it works on a copy rather than relying on callers to remember .copy()

        ApplicationLogger.debug(f"Before feature engineering:\n{dataframe.dtypes}")
        # ---------- Normalize date/time columns ----------
        dataframe["Journey_Date"] = FeatureTransformer._ensure_datetime(dataframe["Journey_Date"])
        dataframe["Departure_Time"] = FeatureTransformer._ensure_datetime(dataframe["Departure_Time"])
        dataframe["Arrival_Time"] = FeatureTransformer._ensure_datetime(dataframe["Arrival_Time"])
        ApplicationLogger.debug(f"After datetime conversion:\n{dataframe.dtypes}")

        # ---------- Date features ----------
        dataframe["Journey_Day"] = dataframe["Journey_Date"].dt.day
        dataframe["Journey_Month"] = dataframe["Journey_Date"].dt.month

        # ---------- Departure features ----------
        dataframe["Departure_Hour"] = dataframe["Departure_Time"].dt.hour
        dataframe["Departure_Minute"] = dataframe["Departure_Time"].dt.minute

        # ---------- Arrival features ----------
        dataframe["Arrival_Hour"] = dataframe["Arrival_Time"].dt.hour
        dataframe["Arrival_Minute"] = dataframe["Arrival_Time"].dt.minute

        # ---------- Duration ----------
        duration = (
            dataframe["Duration"]
                .str.extract(r"(?:(\d+)h)?\s*(?:(\d+)m)?")
                .fillna(0)
                .astype(int)
        )

        dataframe["Duration_Minutes"] = (duration[0] * 60 + duration[1])

        # ---------- Stops ----------
        stop_mapping: dict[str, int] = {
            "Non-Stop": 0,
            "1 Stop": 1,
            "2 Stops": 2,
            "3 Stops": 3,
            "4 Stops": 4,
        }
        dataframe["Total_Stops"] = dataframe["Total_Stops"].map(stop_mapping)
        dataframe.drop(columns=["Journey_Date", "Departure_Time", "Arrival_Time", "Duration",], inplace=True,)
        ApplicationLogger.info("Feature engineering completed successfully.")
        return dataframe


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