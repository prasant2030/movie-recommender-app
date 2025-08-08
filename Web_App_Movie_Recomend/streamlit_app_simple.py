import streamlit as st
import random

# Page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# Movie database
movies = {
    "Action": [
        {"title": "The Dark Knight", "year": 2008, "description": "Batman faces the Joker in this epic crime thriller."},
        {"title": "Mad Max: Fury Road", "year": 2015, "description": "Post-apocalyptic action masterpiece."},
        {"title": "John Wick", "year": 2014, "description": "Ex-hitman seeks revenge for his dog."},
        {"title": "Mission: Impossible - Fallout", "year": 2018, "description": "Ethan Hunt's most dangerous mission."},
        {"title": "The Avengers", "year": 2012, "description": "Earth's mightiest heroes unite."}
    ],
    "Comedy": [
        {"title": "The Grand Budapest Hotel", "year": 2014, "description": "Wes Anderson's quirky hotel comedy."},
        {"title": "Superbad", "year": 2007, "description": "Teen comedy about friendship and parties."},
        {"title": "Bridesmaids", "year": 2011, "description": "Hilarious wedding comedy."},
        {"title": "The Hangover", "year": 2009, "description": "Vegas bachelor party gone wrong."},
        {"title": "Shaun of the Dead", "year": 2004, "description": "Zombie comedy masterpiece."}
    ],
    "Drama": [
        {"title": "The Shawshank Redemption", "year": 1994, "description": "Story of hope and friendship in prison."},
        {"title": "Forrest Gump", "year": 1994, "description": "Life story of a simple man."},
        {"title": "The Godfather", "year": 1972, "description": "Epic crime family saga."},
        {"title": "Pulp Fiction", "year": 1994, "description": "Quentin Tarantino's masterpiece."},
        {"title": "Goodfellas", "year": 1990, "description": "True story of mob life."}
    ],
    "Horror": [
        {"title": "The Shining", "year": 1980, "description": "Psychological horror in a haunted hotel."},
        {"title": "A Nightmare on Elm Street", "year": 1984, "description": "Freddy Krueger terrorizes dreams."},
        {"title": "The Exorcist", "year": 1973, "description": "Classic demonic possession horror."},
        {"title": "Halloween", "year": 1978, "description": "Michael Myers stalks babysitters."},
        {"title": "Get Out", "year": 2017, "description": "Social thriller with horror elements."}
    ],
    "Sci-Fi": [
        {"title": "Blade Runner", "year": 1982, "description": "Neo-noir sci-fi about replicants."},
        {"title": "The Matrix", "year": 1999, "description": "Reality-bending sci-fi action."},
        {"title": "Interstellar", "year": 2014, "description": "Space exploration and time travel."},
        {"title": "Arrival", "year": 2016, "description": "First contact with alien life."},
        {"title": "Ex Machina", "year": 2014, "description": "AI consciousness thriller."}
    ]
}

# Main app
def main():
    st.title("🎬 Movie Recommender")
    st.markdown("### Discover your next favorite movie!")
    
    # Status indicator
    st.success("✅ Movie Recommender is Ready!")
    
    # Genre selection
    st.sidebar.header("🎭 Choose Genres")
    selected_genres = st.sidebar.multiselect(
        "Select your favorite genres:",
        list(movies.keys()),
        default=[]
    )
    
    # Number of recommendations
    num_recommendations = st.sidebar.slider(
        "Number of movies to recommend:",
        min_value=1,
        max_value=10,
        value=5
    )
    
    # Get recommendations button
    if st.sidebar.button("🎯 Get Recommendations", type="primary"):
        if selected_genres:
            recommendations = []
            for genre in selected_genres:
                genre_movies = movies[genre].copy()
                random.shuffle(genre_movies)
                recommendations.extend(genre_movies[:num_recommendations//len(selected_genres) + 1])
            
            random.shuffle(recommendations)
            recommendations = recommendations[:num_recommendations]
            
            st.success(f"Found {len(recommendations)} movies for you!")
            
            # Display recommendations
            for i, movie in enumerate(recommendations, 1):
                with st.container():
                    st.markdown(f"""
                    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0;">
                        <h3>#{i} 🎬 {movie['title']} ({movie['year']})</h3>
                        <p><strong>Description:</strong> {movie['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Please select at least one genre!")
    
    # Welcome message
    if not selected_genres:
        st.markdown("""
        ### Welcome to Movie Recommender! 🎬
        
        **How to use:**
        1. Select your favorite genres from the sidebar
        2. Choose how many movies you'd like to see
        3. Click "Get Recommendations" to discover new movies
        
        **Available Genres:**
        - 🎭 Action
        - 😄 Comedy  
        - 🎭 Drama
        - 👻 Horror
        - 🚀 Sci-Fi
        
        Start by selecting genres from the sidebar!
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🎬 Movie Recommender App | Powered by Streamlit</p>
        <p>✅ Always Working - No API Dependencies</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
