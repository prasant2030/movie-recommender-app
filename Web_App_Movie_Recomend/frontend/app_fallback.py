#!/usr/bin/env python3
"""
Movie Recommendation App - Streamlit Frontend (Fallback Version)
Works with or without backend API
"""

import streamlit as st
import requests
import json
import random
from typing import List, Dict, Optional

# Configuration
API_BASE_URL = "https://movie-recomondation.onrender.com"

# Fallback movie data
FALLBACK_MOVIES = {
    "Action": [
        {"title": "The Dark Knight", "genre": "Action", "year": 2008, "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."},
        {"title": "Mad Max: Fury Road", "genre": "Action", "year": 2015, "description": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max."},
        {"title": "John Wick", "genre": "Action", "year": 2014, "description": "An ex-hitman comes out of retirement to track down the gangsters who killed his dog and stole his car."},
        {"title": "Mission: Impossible - Fallout", "genre": "Action", "year": 2018, "description": "Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission goes wrong."},
        {"title": "The Avengers", "genre": "Action", "year": 2012, "description": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity."}
    ],
    "Comedy": [
        {"title": "The Grand Budapest Hotel", "genre": "Comedy", "year": 2014, "description": "A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel's glorious years under an exceptional concierge."},
        {"title": "Superbad", "genre": "Comedy", "year": 2007, "description": "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry."},
        {"title": "Bridesmaids", "genre": "Comedy", "year": 2011, "description": "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef."},
        {"title": "The Hangover", "genre": "Comedy", "year": 2009, "description": "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding."},
        {"title": "Shaun of the Dead", "genre": "Comedy", "year": 2004, "description": "A man decides to turn his moribund life around by winning back his ex-girlfriend, reconciling his relationship with his mother, and dealing with an entire community that has returned from the dead to eat the living."}
    ],
    "Drama": [
        {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994, "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
        {"title": "Forrest Gump", "genre": "Drama", "year": 1994, "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart."},
        {"title": "The Green Mile", "genre": "Drama", "year": 1999, "description": "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift."},
        {"title": "Schindler's List", "genre": "Drama", "year": 1993, "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis."},
        {"title": "12 Angry Men", "genre": "Drama", "year": 1957, "description": "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence."}
    ],
    "Horror": [
        {"title": "The Shining", "genre": "Horror", "year": 1980, "description": "A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future."},
        {"title": "A Nightmare on Elm Street", "genre": "Horror", "year": 1984, "description": "The monstrous spirit of a slain janitor seeks revenge by invading the dreams of teenagers whose parents were responsible for his untimely death."},
        {"title": "The Exorcist", "genre": "Horror", "year": 1973, "description": "When a 12-year-old girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her."},
        {"title": "Halloween", "genre": "Horror", "year": 1978, "description": "Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield, Illinois to kill again."},
        {"title": "The Silence of the Lambs", "genre": "Horror", "year": 1991, "description": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims."}
    ],
    "Sci-Fi": [
        {"title": "Blade Runner", "genre": "Sci-Fi", "year": 1982, "description": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator."},
        {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999, "description": "A computer programmer discovers that reality as he knows it is a simulation created by machines, and joins a rebellion to break free."},
        {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
        {"title": "Arrival", "genre": "Sci-Fi", "year": 2016, "description": "A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world."},
        {"title": "Ex Machina", "genre": "Sci-Fi", "year": 2014, "description": "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a highly advanced humanoid A.I."}
    ],
    "Thriller": [
        {"title": "Se7en", "genre": "Thriller", "year": 1995, "description": "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi."},
        {"title": "Gone Girl", "genre": "Thriller", "year": 2014, "description": "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent."},
        {"title": "The Silence of the Lambs", "genre": "Thriller", "year": 1991, "description": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims."},
        {"title": "Memento", "genre": "Thriller", "year": 2000, "description": "A man with short-term memory loss attempts to track down his wife's murderer."},
        {"title": "Fight Club", "genre": "Thriller", "year": 1999, "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more."}
    ]
}

DEFAULT_GENRES = list(FALLBACK_MOVIES.keys())

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
    .status-fallback {
        background-color: #fff3cd;
        color: #856404;
        border: 1px solid #ffeaa7;
    }
</style>
""", unsafe_allow_html=True)

class APIClient:
    """API client with fallback to local data"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'MovieRecommender/1.0'
        })
    
    def check_health(self) -> Dict:
        """Check if the API is healthy"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            return {
                'status': 'success',
                'status_code': response.status_code,
                'data': response.json() if response.status_code == 200 else None,
                'error': None
            }
        except:
            return {'status': 'error', 'error': 'API unavailable'}
    
    def get_genres(self) -> List[str]:
        """Get available genres with fallback"""
        try:
            response = self.session.get(f"{self.base_url}/api/movies/genres", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('genres', DEFAULT_GENRES)
        except:
            pass
        return DEFAULT_GENRES
    
    def get_recommendations(self, genres: List[str], count: int = 5) -> List[Dict]:
        """Get movie recommendations with fallback to local data"""
        try:
            payload = {
                'genres': genres,
                'count': count
            }
            
            response = self.session.post(
                f"{self.base_url}/api/recommendations", 
                json=payload, 
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('movies', [])
        except:
            pass
        
        # Fallback to local data
        recommendations = []
        for genre in genres:
            if genre in FALLBACK_MOVIES:
                genre_movies = FALLBACK_MOVIES[genre].copy()
                random.shuffle(genre_movies)
                recommendations.extend(genre_movies[:count//len(genres) + 1])
        
        # Shuffle and limit to requested count
        random.shuffle(recommendations)
        return recommendations[:count]

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
    health_result = api_client.check_health()
    
    if health_result['status'] == 'success' and health_result['status_code'] == 200:
        st.markdown('<div class="status-indicator status-online">✅ Backend API is Online</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-indicator status-fallback">🔄 Using Fallback Data (Backend Unavailable)</div>', unsafe_allow_html=True)
        st.info("The backend API is currently unavailable. You're using our curated fallback movie database.")
    
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
                    
                    if recommendations:
                        st.success(f"Found {len(recommendations)} movies for you!")
                    else:
                        st.warning("No movies found. Please try different genres.")
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
    st.markdown(f"""
    <div style='text-align: center; color: #666;'>
        <p>🎬 Movie Recommender App | Powered by Streamlit & FastAPI</p>
        <p>Backend API: <a href='{API_BASE_URL}' target='_blank'>{API_BASE_URL}</a></p>
        <p>Status: {'🟢 Online' if health_result['status'] == 'success' else '🔄 Fallback Mode'}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
