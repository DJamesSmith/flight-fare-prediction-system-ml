# ✔ Load dataset
# ✔ Generate airline distribution chart
# ✔ Generate source city distribution chart
# ✔ Generate destination city distribution chart
# ✔ Generate fare distribution chart
# ✔ Generate correlation analysis
# ✔ Save generated graphs

# VisualizationService only needs access to the processed dataset (typically feature_dataset.csv) and the evaluation metrics to generate charts,

import matplotlib.pyplot as plt
import pandas as pd
from utilities.constants import (
    FEATURE_DATASET_PATH,
    AIRLINE_GRAPH_PATH,
    SOURCE_GRAPH_PATH,
    DESTINATION_GRAPH_PATH,
    FARE_GRAPH_PATH,
    CORRELATION_GRAPH_PATH
)
from utilities.file_handler import FileHandler
from utilities.logger import ApplicationLogger
from decorators.execution_time import log_execution_time

class VisualizationService:
    def __init__(self):
        self.dataframe: pd.DataFrame = pd.DataFrame()

    def load_dataset(self):
        self.dataframe = FileHandler.read_csv(FEATURE_DATASET_PATH)
        ApplicationLogger.info("Feature dataset loaded.")

    def generate_bar_chart(self, column: str, title: str, x_label: str, y_label: str, save_path: str):
        plt.figure(figsize=(10, 6))
        self.dataframe[column].value_counts().plot(kind="bar")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        ApplicationLogger.info(f"{title} graph generated.")

    # creates and saves graph
    def airline_distribution(self):
        self.generate_bar_chart(column="Airline", title="Airline Distribution", x_label="Airline", y_label="Flights", save_path=AIRLINE_GRAPH_PATH)

    def source_distribution(self):
        self.generate_bar_chart(column="Source", title="Source Distribution", x_label="Source", y_label="Flights", save_path=SOURCE_GRAPH_PATH)

    def destination_distribution(self):
        self.generate_bar_chart(column="Destination", title="Destination Distribution", x_label="Destination", y_label="Flights", save_path=DESTINATION_GRAPH_PATH)

    def fare_distribution(self):
        plt.figure(figsize=(10, 6))
        self.dataframe["Fare"].plot(kind="hist", bins=30)
        plt.title("Fare Distribution")
        plt.xlabel("Fare")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(FARE_GRAPH_PATH)
        plt.close()
        ApplicationLogger.info("Fare distribution graph generated.")

    @log_execution_time
    def correlation_analysis(self):
        correlation = self.dataframe.corr(numeric_only=True)
        plt.figure(figsize=(10, 8))
        plt.imshow(correlation, interpolation="nearest")
        plt.colorbar()
        plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
        plt.yticks(range(len(correlation.columns)), correlation.columns)
        plt.tight_layout()
        plt.savefig(CORRELATION_GRAPH_PATH)
        plt.close()
        ApplicationLogger.info("Correlation analysis graph generated.")
        pass

    @log_execution_time
    def save_graphs(self):
        self.airline_distribution()
        self.source_distribution()
        self.destination_distribution()
        self.fare_distribution()
        self.correlation_analysis()
        ApplicationLogger.info("All graphs generated successfully.")