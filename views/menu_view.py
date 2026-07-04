class MenuView:
    def __init__(self):
        pass

    @staticmethod
    def display_welcome():
        print("-" * 60)
        print("\t\tFlight Fare Prediction System")
        print("-" * 60)

    @staticmethod
    def display_main_menu():
        MenuView.display_welcome()
        print("1. Login")
        print("2. Exit")
        print("-" * 60)