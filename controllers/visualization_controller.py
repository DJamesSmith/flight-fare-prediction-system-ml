# Responsibilities:
# Load the processed dataset
# Generate charts
# Inform the user

from services.visualization_service import VisualizationService

class VisualizationController:
    def __init__(self) -> None:
        self.visualization_service: VisualizationService = VisualizationService()

    def generate_visualizations(self) -> None:
        try:
            self.visualization_service.load_dataset()
            self.visualization_service.save_graphs()
            print("\nVisualizations generated successfully.")
            print("Graphs have been saved to the output directory.")

        except Exception as error:
            print(error)