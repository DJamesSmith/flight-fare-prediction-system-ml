# ✔ Load dataset
# ✔ Generate airline distribution chart
# ✔ Generate source city distribution chart
# ✔ Generate destination city distribution chart
# ✔ Generate fare distribution chart
# ✔ Generate correlation analysis
# ✔ Save generated graphs

from abc import ABC, abstractmethod

class VisualizationService(ABC):
    @abstractmethod
    def load_dataset(self):
        pass

    @abstractmethod
    def airline_distribution(self):
        pass

    @abstractmethod
    def source_distribution(self):
        pass

    @abstractmethod
    def destination_distribution(self):
        pass

    @abstractmethod
    def fare_distribution(self):
        pass

    @abstractmethod
    def correlation_analysis(self):
        pass

    @abstractmethod
    def save_graphs(self):
        pass