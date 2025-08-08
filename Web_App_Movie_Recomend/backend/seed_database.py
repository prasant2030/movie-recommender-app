#!/usr/bin/env python3
"""
Database seeding script for Movie Recommendation API
Run this script to populate the database with initial movie data
"""

import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.database.connection import engine
from app.database.models import Base
from app.database.seed_data import seed_database


def main():
    """Main function to seed the database"""
    print("Starting database seeding process...")
    
    try:
        # Create tables if they don't exist
        print("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        
        # Seed the database
        print("Seeding database with movie data...")
        seed_database()
        
        print("Database seeding completed successfully!")
        
    except Exception as e:
        print(f"Error during database seeding: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 