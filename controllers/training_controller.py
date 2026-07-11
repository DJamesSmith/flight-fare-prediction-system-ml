# Responsibilities:
# 1. Load feature dataset
# 2. Encode features
# 3. Split dataset
# 4. Train models
# 5. Evaluate models
# 6. Save best model
# 7. Save encoder

from services.training_service import TrainingService


class TrainingController:
    def __init__(self):
        self.training_service: TrainingService = TrainingService()

    def train_models(self):
        try:
            print("\nLoading feature dataset...")
            self.training_service.load_feature_dataset()

            print("Encoding categorical features...")
            self.training_service.encode_features()

            print("Splitting dataset...")
            self.training_service.split_dataset()

            print("Training Linear Regression...")
            self.training_service.train_linear_regression()

            print("Training Decision Tree...")
            self.training_service.train_decision_tree()

            print("Training Random Forest...")
            self.training_service.train_random_forest()

            print("Evaluating models...")
            metrics = self.training_service.evaluate_models()

            print("\nModel Evaluation\n")
            print(metrics.to_string(index=False))

            print("Comparing models...")
            self.training_service.compare_models()

            print("\nSaving best model...")
            self.training_service.save_best_model()

            print("Saving encoder...")
            self.training_service.save_encoder()

            print("\nTraining pipeline completed successfully.")
        except Exception as error:
            print(error)