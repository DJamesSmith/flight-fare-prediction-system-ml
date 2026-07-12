class AdminView:
    def __init__(self):
        pass

    @staticmethod
    def display_admin_menu():
        # print("-" * 10, "ADMIN MENU", "-" * 10, "\n" \
        #     "---------- User Management ----------\n" \
        #     "1. Create User\n" \
        #     "2. View Users\n" \
        #     "3. Update User\n" \
        #     "4. Delete User\n" \
        #     "5. Change Password\n\n" \

        #     "-------------- Flights --------------\n" \
        #     "6. View Flights\n" \
        #     "7. Search Flights\n\n" \

        #     "-------------- Dataset --------------\n" \
        #     "8. Prepare Training Dataset\n\n" \

        #     "--------------- Model ---------------\n" \
        #     "9. Train ML Models\n\n" \

        #     "------------- Prediction -------------\n" \
        #     "12. View Prediction History\n" \
        #     "13. Delete Prediction\n\n" \

        #     "----------- Visualizations -----------\n" \
        #     "10. Compare Model Performance\n" \
        #     "11. Predict Flight Fare\n" \

        #     "--------------- Reports --------------\n" \
        #     "14. Generate Visualizations\n" \
        #     "15. View Evaluation Metrics\n" \
        #     "16. View Prediction Report\n" \
        #     "17. Export Metrics CSV\n" \
        #     "18. Export Prediction History CSV\n" \
        #     "19. Generate Project PDF Report\n" \
        #     "20. View Reports\n\n" \

        #     "21. Logout\n", "" \
        #     "-" * 40)

        print("-" * 10, "ADMIN MENU", "-" * 10, "\n" \
            "1. User Management\n" \
            "2. Flight Explorer\n" \
            "3. Dataset Pipeline\n" \
            "4. Train Models\n" \
            "5. Model Evaluation\n" \
            "6. Predictions\n" \
            "7. Reports\n" \
            "8. Logout\n")
        
    def user_management(self):
        print("-" * 10, "User Management", "-" * 10, "\n" \
            "1. Create User\n" \
            "2. View Users\n" \
            "3. Update User\n" \
            "4. Delete User\n" \
            "5. Change Password\n" \
            "6. Go Back")
        
    def flight_explorer(self):
        print("-" * 10, "User Management", "-" * 10, "\n" \
            "1. View Flights\n" \
            "2. Search Flights\n" \
            "3. Back")
        


    def dataset_pipeline(self):
        pass

    def train_models(self):
        pass

    def model_evaluation(self):
        pass

    def predictions(self):
        pass

    def reports(self):
        pass



# Calls made to following methods:
# 1.
# 2.
# 3.
# 4.
# 5. 
# 6. 
# 7. 
# 8. PreprocessingService, not FlightService. The preprocessing service only defines methods. They aren't executed until the admin selects Prepare Training Dataset.
# 9. training doesn't begin until Train ML Models is chosen.
# 10. 
# 11. 
# 12. 
# 13. VisualizationController.generate_visualizations()
# 14. ReportController.generate_metrics_report()
# 15. 
# 16. 
# 17. ReportController.export_prediction_history_csv()
# 18. ReportController.generate_project_report()
# 19. 
# 20. Logout