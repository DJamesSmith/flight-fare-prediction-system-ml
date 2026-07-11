import os

BASE_DIR                    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIRECTORY = os.path.join(BASE_DIR, "outputs")

# input data
DATASET_PATH                = os.path.join(BASE_DIR, "dataset", "data_train.csv")                         # training feed
TEST_DATASET_PATH           = os.path.join(BASE_DIR, "dataset", "test_set.csv")                           # for testing the trained model data (unused)

DATA_DIRECTORY = os.path.join(OUTPUT_DIRECTORY, "data")
MODEL_DIRECTORY = os.path.join(OUTPUT_DIRECTORY, "trained_models")
REPORT_DIRECTORY = os.path.join(OUTPUT_DIRECTORY, "reports")
GRAPH_DIRECTORY = os.path.join(OUTPUT_DIRECTORY, "graphs")

CLEANED_DATASET_PATH = os.path.join(DATA_DIRECTORY, "cleaned_dataset.csv")
FEATURE_DATASET_PATH = os.path.join(DATA_DIRECTORY, "feature_dataset.csv")

# generated output csv-pkl-pdf file directories
MODEL_PATH = os.path.join(MODEL_DIRECTORY, "flight_model.pkl")
ENCODER_PATH = os.path.join(MODEL_DIRECTORY, "encoder.pkl")
METRICS_REPORT_PATH = os.path.join(REPORT_DIRECTORY, "metrics.csv")
PREDICTION_HISTORY_PATH     = os.path.join(REPORT_DIRECTORY, "prediction_history.csv")
PROJECT_REPORT_PATH         = os.path.join(REPORT_DIRECTORY, "project_report.pdf")

# generated output graph directories
AIRLINE_GRAPH_PATH          = os.path.join(GRAPH_DIRECTORY, "airline_distribution.png")
SOURCE_GRAPH_PATH           = os.path.join(GRAPH_DIRECTORY, "source_distribution.png")
DESTINATION_GRAPH_PATH      = os.path.join(GRAPH_DIRECTORY, "destination_distribution.png")
FARE_GRAPH_PATH             = os.path.join(GRAPH_DIRECTORY, "fare_distribution.png")
CORRELATION_GRAPH_PATH      = os.path.join(GRAPH_DIRECTORY, "correlation_matrix.png")