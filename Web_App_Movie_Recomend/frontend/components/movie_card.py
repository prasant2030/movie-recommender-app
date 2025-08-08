"""
Movie Card Component
Displays individual movie information in a card format
"""

import streamlit as st
from typing import Dict


class MovieCard:
    """Component for displaying movie information in a card format"""
    
    def __init__(self):
        pass
    
    def render(self, movie: Dict):
        """Render a movie card with movie information"""
        
        # Extract movie data
        title = movie.get('title', 'Unknown Title')
        year = movie.get('year', 'Unknown Year')
        genre = movie.get('genre', 'Unknown Genre')
        description = movie.get('description', 'No description available.')
        poster_url = movie.get('poster_url', '')
        
        # Create movie card
        with st.container():
            st.markdown("""
            <style>
            .movie-card {
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                background-color: #f9f9f9;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .movie-title {
                font-size: 1.2rem;
                font-weight: bold;
                color: #1f77b4;
                margin-bottom: 5px;
            }
            .movie-meta {
                color: #666;
                font-size: 0.9rem;
                margin-bottom: 10px;
            }
            .movie-description {
                font-size: 0.9rem;
                line-height: 1.4;
                color: #333;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Movie poster (if available)
            if poster_url:
                try:
                    st.image(poster_url, width=200, caption=title)
                except:
                    st.markdown("🎬 *Poster not available*")
            
            # Movie information
            st.markdown(f"""
            <div class="movie-card">
                <div class="movie-title">{title}</div>
                <div class="movie-meta">📅 {year} | 🎭 {genre}</div>
                <div class="movie-description">{description}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Add some spacing
            st.markdown("<br>", unsafe_allow_html=True)
    
    def render_compact(self, movie: Dict):
        """Render a compact movie card for lists"""
        
        title = movie.get('title', 'Unknown Title')
        year = movie.get('year', 'Unknown Year')
        genre = movie.get('genre', 'Unknown Genre')
        
        st.markdown(f"""
        **{title}** ({year}) - {genre}
        """)
        
        if st.button(f"View Details", key=f"details_{movie.get('id', title)}"):
            st.session_state.selected_movie = movie
            st.rerun() 