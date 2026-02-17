from flask import Blueprint, jsonify
import sys
import os

# Create a Blueprint for Frontend API
frontend_api = Blueprint('frontend_api', __name__)

# Dynamically add Frontend/Base to path to import en_jp
# This is necessary because the project structure uses deep nesting
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_JP_PATH = os.path.join(BASE_DIR, 'Frontend', 'Base')
if EN_JP_PATH not in sys.path:
    sys.path.append(EN_JP_PATH)

from en_jp import load_translations

@frontend_api.route("/translations/<lang>")
def get_translations_api(lang):
    """API endpoint for fetching merged translations."""
    # Scan from the project root
    translations = load_translations(lang, base_path=BASE_DIR)
    return jsonify(translations)
