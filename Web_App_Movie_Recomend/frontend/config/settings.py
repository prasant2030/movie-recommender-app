"""
Configuration settings for the Movie Recommender frontend
"""

# API Configuration
import os
API_BASE_URL = os.getenv("API_BASE_URL", "https://movie-recomondation.onrender.com")

# App Configuration
APP_TITLE = "Movie Recommender"
APP_ICON = "🎬"

# UI Configuration
DEFAULT_RECOMMENDATION_COUNT = 5
MAX_RECOMMENDATION_COUNT = 20
MIN_RECOMMENDATION_COUNT = 1

# Available genres (fallback if API is not available)
DEFAULT_GENRES = [
    "Action",
    "Comedy", 
    "Drama",
    "Horror",
    "Sci-Fi",
    "Thriller"
]

# Error messages
ERROR_MESSAGES = {
    "api_unavailable": "API server is not available. Please check if the backend is running.",
    "no_genres_selected": "Please select at least one genre to get recommendations.",
    "no_movies_found": "No movies found for the selected genres.",
    "network_error": "Network error. Please check your connection."
} 