#!/usr/bin/env python3
"""
Movie Recommendation App - Streamlit Frontend
Main application entry point
"""

import streamlit as st
from components.genre_selector import GenreSelector
from components.recommendation_display import RecommendationDisplay
from components.movie_card import MovieCard
from services.api_client import APIClient
from config.settings import API_BASE_URL

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
</style>
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
    
    # Sidebar for genre selection
    with st.sidebar:
        st.header("🎭 Genre Selection")
        st.markdown("Select one or more genres to get personalized recommendations:")
        
        # Genre selector component
        genre_selector = GenreSelector(api_client)
        selected_genres = genre_selector.render()
        
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
                    try:
                        recommendations = api_client.get_recommendations(
                            genres=selected_genres,
                            count=recommendation_count
                        )
                        st.session_state.recommendations = recommendations
                        st.session_state.selected_genres = selected_genres
                        st.session_state.recommendation_count = recommendation_count
                        st.success(f"Found {len(recommendations)} movies for you!")
                    except Exception as e:
                        st.error(f"Error getting recommendations: {str(e)}")
            else:
                st.warning("Please select at least one genre!")
    
    # Main content area
    if st.session_state.recommendations:
        # Display recommendations
        recommendation_display = RecommendationDisplay()
        recommendation_display.render(st.session_state.recommendations)
        
        # Action buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("🔄 Get More Recommendations"):
                if st.session_state.selected_genres:
                    with st.spinner("Finding more movies..."):
                        try:
                            recommendations = api_client.get_recommendations(
                                genres=st.session_state.selected_genres,
                                count=st.session_state.recommendation_count
                            )
                            st.session_state.recommendations = recommendations
                            st.success(f"Found {len(recommendations)} new movies!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error getting recommendations: {str(e)}")
        
        with col2:
            if st.button("🏠 Start Over"):
                st.session_state.recommendations = []
                st.session_state.selected_genres = []
                st.rerun()
        
        with col3:
            if st.button("📊 View All Movies"):
                st.session_state.show_all_movies = True
                st.rerun()
    
    elif st.session_state.get('show_all_movies', False):
        # Show all movies view
        st.header("📚 All Available Movies")
        
        try:
            all_movies = api_client.get_all_movies()
            if all_movies:
                # Group movies by genre
                movies_by_genre = {}
                for movie in all_movies:
                    genre = movie.get('genre', 'Unknown')
                    if genre not in movies_by_genre:
                        movies_by_genre[genre] = []
                    movies_by_genre[genre].append(movie)
                
                # Display movies by genre
                for genre, movies in movies_by_genre.items():
                    st.subheader(f"🎭 {genre} Movies")
                    cols = st.columns(3)
                    for i, movie in enumerate(movies):
                        with cols[i % 3]:
                            movie_card = MovieCard()
                            movie_card.render(movie)
                
                if st.button("🔙 Back to Recommendations"):
                    st.session_state.show_all_movies = False
                    st.rerun()
            else:
                st.info("No movies available.")
        except Exception as e:
            st.error(f"Error loading movies: {str(e)}")
    
    else:
        # Welcome screen
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>Welcome to Movie Recommender! 🎬</h2>
            <p style="font-size: 1.2rem; color: #666;">
                Select your favorite genres from the sidebar and get personalized movie recommendations.
            </p>
            <br>
            <div style="display: flex; justify-content: center; gap: 2rem;">
                <div style="text-align: center;">
                    <h3>🎭 Choose Genres</h3>
                    <p>Select from Action, Comedy, Drama, Horror, Sci-Fi, and more!</p>
                </div>
                <div style="text-align: center;">
                    <h3>🎯 Get Recommendations</h3>
                    <p>Discover movies tailored to your preferences</p>
                </div>
                <div style="text-align: center;">
                    <h3>🔄 Explore More</h3>
                    <p>Keep discovering new movies you'll love</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 