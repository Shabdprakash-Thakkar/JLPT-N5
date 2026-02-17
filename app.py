from flask import Flask, send_from_directory
import os

# Import APIs
from API.frontend_api import frontend_api
# from API.backend_api import backend_api # Placeholder
# from API.database_api import database_api # Placeholder

app = Flask(__name__)

# Base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, 'Frontend', 'Base')

# Register Blueprints (Dispatching to specialized APIs)
app.register_blueprint(frontend_api)
# app.register_blueprint(backend_api)
# app.register_blueprint(database_api)

@app.route("/")
def index():
    """Serve the home page."""
    return send_from_directory(FRONTEND_DIR, "base.html")

@app.route("/<path:filename>")
def serve_static(filename):
    """Serve static files and other HTML pages."""
    return send_from_directory(FRONTEND_DIR, filename)

if __name__ == "__main__":
    # In this new architecture, app.py acts as the manager.
    # Requests are dispatched to frontend_api, etc.
    app.run(debug=True, port=5000)
