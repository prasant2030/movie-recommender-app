#!/usr/bin/env python3
"""
Script to run the Movie Recommender Streamlit app
"""

import subprocess
import sys
import os

def main():
    """Run the Streamlit app"""
    print("🎬 Starting Movie Recommender App...")
    print("📱 App will be available at: http://localhost:8501")
    print("🔧 Press Ctrl+C to stop the app")
    print("-" * 50)
    
    try:
        # Run streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 App stopped by user")
    except Exception as e:
        print(f"❌ Error running app: {e}")

if __name__ == "__main__":
    main() 