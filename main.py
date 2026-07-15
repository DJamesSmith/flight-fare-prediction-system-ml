# Start application
# Initialize Database
# Delegate request to appropriate controller
# Exit application

from controllers.application_controller import ApplicationController
from database.db_initializer import DatabaseInitializer

if __name__ == "__main__":
    DatabaseInitializer.initialize_database()

    app: ApplicationController = ApplicationController()
    app.start_app()