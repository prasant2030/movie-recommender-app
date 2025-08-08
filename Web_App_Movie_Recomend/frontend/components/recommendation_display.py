"""
Recommendation Display Component
Displays movie recommendations in a grid layout
"""

import streamlit as st
from typing import List, Dict
from .movie_card import MovieCard


class RecommendationDisplay:
    """Component for displaying movie recommendations"""
    
    def __init__(self):
        self.movie_card = MovieCard()
    
    def render(self, recommendations: List[Dict]):
        """Render movie recommendations in a grid layout"""
        
        if not recommendations:
            st.warning("No recommendations found. Try selecting different genres.")
            return
        
        # Header
        st.header("🎯 Your Movie Recommendations")
        st.markdown(f"Found **{len(recommendations)}** movies for you!")
        
        # Display recommendations in a grid
        if len(recommendations) <= 3:
            # For 1-3 movies, display in a single row
            cols = st.columns(len(recommendations))
            for i, movie in enumerate(recommendations):
                with cols[i]:
                    self.movie_card.render(movie)
        else:
            # For more movies, display in a 3-column grid
            for i in range(0, len(recommendations), 3):
                row_movies = recommendations[i:i+3]
                cols = st.columns(3)
                
                for j, movie in enumerate(row_movies):
                    with cols[j]:
                        self.movie_card.render(movie)
                
                # Add spacing between rows
                if i + 3 < len(recommendations):
                    st.markdown("<br>", unsafe_allow_html=True)
        
        # Summary
        st.markdown("---")
        genres = list(set([movie.get('genre', 'Unknown') for movie in recommendations]))
        st.markdown(f"**Recommendations based on:** {', '.join(genres)}")
        
        # Statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Movies", len(recommendations))
        with col2:
            avg_year = sum(movie.get('year', 0) for movie in recommendations) / len(recommendations)
            st.metric("Average Year", f"{avg_year:.0f}")
        with col3:
            unique_genres = len(set(movie.get('genre', 'Unknown') for movie in recommendations))
            st.metric("Genres Covered", unique_genres) 