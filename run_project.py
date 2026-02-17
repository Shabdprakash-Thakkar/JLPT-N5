# ========== Unified Project Runner v5.0.0 ==========
import os
import sys

# Ensure project root is in path for relative imports if needed
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

if __name__ == "__main__":
    print("--- JLPT N5 Master Project ---")
    print("Starting Frontend, Backend, and API...")
    print("Visit: http://127.0.0.1:5000")
    app.run(debug=True)
