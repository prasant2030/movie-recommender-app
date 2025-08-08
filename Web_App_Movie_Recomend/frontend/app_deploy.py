#!/usr/bin/env python3
"""
Movie Recommendation App - Streamlit Frontend (Deployment Version)
Simplified single-file version for easy deployment
"""

import streamlit as st
import requests
import json
from typing import List, Dict, Optional

# Configuration
API_BASE_URL = "https://movie-recomondation.onrender.com"
DEFAULT_GENRES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Thriller"]

# Page configuration
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-size: 1.1rem;
    }
    .stButton > button:hover {
        background-color: #0d5aa7;
    }
    .movie-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #1f77b4;
    }
    .status-indicator {
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
    }
    .status-online {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    .status-offline {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
</style>
""", unsafe_allow_html=True)

class APIClient:
    """Simplified API client for backend communication"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def check_health(self) -> bool:
        """Check if the API is healthy"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_genres(self) -> List[str]:
        """Get available genres from the API"""
        try:
            response = self.session.get(f"{self.base_url}/api/movies/genres", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('genres', DEFAULT_GENRES)
        except:
            pass
        return DEFAULT_GENRES
    
    def get_recommendations(self, genres: List[str], count: int = 5) -> List[Dict]:
        """Get movie recommendations based on selected genres"""
        try:
            payload = {
                'genres': genres,
                'count': count
            }
            response = self.session.post(f"{self.base_url}/api/recommendations", 
                                       json=payload, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('movies', [])
        except Exception as e:
            st.error(f"Error getting recommendations: {str(e)}")
        return []

def display_movie_card(movie: Dict):
    """Display a movie card"""
    with st.container():
        st.markdown(f"""
        <div class="movie-card">
            <h3>🎬 {movie.get('title', 'Unknown Title')}</h3>
            <p><strong>Genre:</strong> {movie.get('genre', 'Unknown')}</p>
            <p><strong>Year:</strong> {movie.get('year', 'Unknown')}</p>
            <p><strong>Description:</strong> {movie.get('description', 'No description available')}</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Initialize session state
    if 'recommendations' not in st.session_state:
        st.session_state.recommendations = []
    if 'selected_genres' not in st.session_state:
        st.session_state.selected_genres = []
    if 'recommendation_count' not in st.session_state:
        st.session_state.recommendation_count = 5
    
    # Header
    st.markdown('<h1 class="main-header">🎬 Movie Recommender</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Discover your next favorite movie based on genre preferences</p>', unsafe_allow_html=True)
    
    # Initialize API client
    api_client = APIClient(API_BASE_URL)
    
    # Check API status
    api_healthy = api_client.check_health()
    if api_healthy:
        st.markdown('<div class="status-indicator status-online">✅ Backend API is Online</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-indicator status-offline">⚠️ Backend API is Offline - Using Fallback Data</div>', unsafe_allow_html=True)
    
    # Sidebar for genre selection
    with st.sidebar:
        st.header("🎭 Genre Selection")
        st.markdown("Select one or more genres to get personalized recommendations:")
        
        # Get available genres
        available_genres = api_client.get_genres()
        
        # Genre selection
        selected_genres = st.multiselect(
            "Choose your favorite genres:",
            options=available_genres,
            default=[],
            help="Select one or more genres to get movie recommendations"
        )
        
        # Recommendation count selector
        st.subheader("📊 Number of Recommendations")
        recommendation_count = st.slider(
            "How many movies would you like to see?",
            min_value=1,
            max_value=20,
            value=5,
            step=1
        )
        
        # Get recommendations button
        if st.button("🎯 Get Recommendations", type="primary"):
            if selected_genres:
                with st.spinner("Finding the perfect movies for you..."):
                    recommendations = api_client.get_recommendations(
                        genres=selected_genres,
                        count=recommendation_count
                    )
                    st.session_state.recommendations = recommendations
                    st.session_state.selected_genres = selected_genres
                    st.session_state.recommendation_count = recommendation_count
                    st.success(f"Found {len(recommendations)} movies for you!")
            else:
                st.error("Please select at least one genre to get recommendations.")
    
    # Main content area
    if st.session_state.recommendations:
        st.header(f"🎯 Your Movie Recommendations")
        st.markdown(f"*Based on genres: {', '.join(st.session_state.selected_genres)}*")
        
        # Display recommendations
        for i, movie in enumerate(st.session_state.recommendations, 1):
            st.subheader(f"#{i}")
            display_movie_card(movie)
    else:
        # Welcome message
        st.markdown("""
        ### 🎬 Welcome to Movie Recommender!
        
        **How to use:**
        1. Select your favorite genres from the sidebar
        2. Choose how many movies you'd like to see
        3. Click "Get Recommendations" to discover new movies
        
        **Available Genres:**
        - 🎭 Action & Adventure
        - 😄 Comedy
        - 🎭 Drama
        - 👻 Horror
        - 🚀 Sci-Fi
        - 😱 Thriller
        
        Start by selecting genres from the sidebar!
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🎬 Movie Recommender App | Powered by Streamlit & FastAPI</p>
        <p>Backend API: <a href='https://movie-recomondation.onrender.com' target='_blank'>https://movie-recomondation.onrender.com</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
