#!/usr/bin/env python3
"""
Simple test script to start the FastAPI server
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(__file__))

try:
    print("Importing app...")
    from app.main import app
    print("App imported successfully!")
    
    print("Starting server...")
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc() 