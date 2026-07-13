# Start application.
# Display main menu.
# Accept user's menu choice.
# Delegate request to appropriate controller.
# Exit application.

from controllers.application_controller import ApplicationController
from database.db_initializer import DatabaseInitializer

if __name__ == "__main__":
    DatabaseInitializer.initialize_database()

    app: ApplicationController = ApplicationController()
    app.start_app()

# ___________________________________
# Remaining:
# base_repository class, parts that are common for all repos
# ___________________________________
# Need to contain these folders in single directory, suitable name?
# 1. data
# 2. dataset
# 3. graphs
# 4. reports
# 5. trained_models
# ___________________________________
# Date-range reports

# ADMIN MENU
# 13. Export Prediction History
# Enter Start Date: YYYY-MM-DD
# Enter End Date: YYYY-MM-DD

# SELECT *
# FROM predictions
# WHERE prediction_time
# BETWEEN %s
# AND %s
# ORDER BY prediction_time;

# Then in ReportService -> export_prediction_history_csv(start_date,end_date)
# ___________________________________
#  Future prospect in bookings:
# Admin can check for a selected flight, given date range, where total stops > 2, how many users were booked or something along those lines.
# For this you'll need JOINs, GROUP BY and other clauses