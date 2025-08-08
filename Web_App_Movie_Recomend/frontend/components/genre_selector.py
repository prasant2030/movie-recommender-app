"""
Genre Selector Component
Handles genre selection for movie recommendations
"""

import streamlit as st
from typing import List
from services.api_client import APIClient
from config.settings import DEFAULT_GENRES


class GenreSelector:
    """Component for selecting movie genres"""
    
    def __init__(self, api_client: APIClient):
        self.api_client = api_client
    
    def render(self) -> List[str]:
        """Render the genre selector and return selected genres"""
        
        # Get available genres from API or use defaults
        try:
            available_genres = self.api_client.get_genres()
            if not available_genres:
                available_genres = DEFAULT_GENRES
        except:
            available_genres = DEFAULT_GENRES
        
        # Display genre selection
        st.markdown("**Select your favorite genres:**")
        
        # Create genre selection with checkboxes
        selected_genres = []
        
        # Group genres in columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            for i, genre in enumerate(available_genres[:len(available_genres)//2]):
                if st.checkbox(f"🎭 {genre}", key=f"genre_{i}"):
                    selected_genres.append(genre)
        
        with col2:
            for i, genre in enumerate(available_genres[len(available_genres)//2:], start=len(available_genres)//2):
                if st.checkbox(f"🎭 {genre}", key=f"genre_{i}"):
                    selected_genres.append(genre)
        
        # Show selection summary
        if selected_genres:
            st.markdown(f"**Selected genres:** {', '.join(selected_genres)}")
        else:
            st.info("💡 Select one or more genres to get personalized recommendations")
        
        return selected_genres 