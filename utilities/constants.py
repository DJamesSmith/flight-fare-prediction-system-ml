import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "data_train.csv")                         # input data / training feed
TEST_DATASET_PATH = os.path.join(BASE_DIR, "dataset", "test_set.csv")
CLEANED_DATASET_PATH = os.path.join(BASE_DIR, "data", "cleaned_dataset.csv")
FEATURE_DATASET_PATH = os.path.join(BASE_DIR, "data", "feature_dataset.csv")

MODEL_PATH = os.path.join(BASE_DIR, "trained_models", "flight_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "trained_models", "encoder.pkl")
METRICS_REPORT_PATH = os.path.join(BASE_DIR, "reports", "metrics.csv")
PREDICTION_HISTORY_PATH = os.path.join(BASE_DIR, "reports", "prediction_history.csv")
PROJECT_REPORT_PATH = os.path.join(BASE_DIR, "reports", "project_report.pdf")