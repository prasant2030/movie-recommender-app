import streamlit as st
import random

# Page config
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# Complete movie database - NO API NEEDED
MOVIE_DATABASE = {
    "Action": [
        {"title": "The Dark Knight", "year": 2008, "description": "Batman faces the Joker in this epic crime thriller."},
        {"title": "Mad Max: Fury Road", "year": 2015, "description": "Post-apocalyptic action masterpiece."},
        {"title": "John Wick", "year": 2014, "description": "Ex-hitman seeks revenge for his dog."},
        {"title": "Mission: Impossible - Fallout", "year": 2018, "description": "Ethan Hunt's most dangerous mission."},
        {"title": "The Avengers", "year": 2012, "description": "Earth's mightiest heroes unite."},
        {"title": "Die Hard", "year": 1988, "description": "Action classic with Bruce Willis."},
        {"title": "Gladiator", "year": 2000, "description": "Epic Roman revenge story."},
        {"title": "The Matrix", "year": 1999, "description": "Reality-bending sci-fi action."}
    ],
    "Comedy": [
        {"title": "The Grand Budapest Hotel", "year": 2014, "description": "Wes Anderson's quirky hotel comedy."},
        {"title": "Superbad", "year": 2007, "description": "Teen comedy about friendship and parties."},
        {"title": "Bridesmaids", "year": 2011, "description": "Hilarious wedding comedy."},
        {"title": "The Hangover", "year": 2009, "description": "Vegas bachelor party gone wrong."},
        {"title": "Shaun of the Dead", "year": 2004, "description": "Zombie comedy masterpiece."},
        {"title": "The Big Lebowski", "year": 1998, "description": "The Dude abides."},
        {"title": "Groundhog Day", "year": 1993, "description": "Time loop comedy classic."},
        {"title": "Monty Python and the Holy Grail", "year": 1975, "description": "Surreal comedy masterpiece."}
    ],
    "Drama": [
        {"title": "The Shawshank Redemption", "year": 1994, "description": "Story of hope and friendship in prison."},
        {"title": "Forrest Gump", "year": 1994, "description": "Life story of a simple man."},
        {"title": "The Godfather", "year": 1972, "description": "Epic crime family saga."},
        {"title": "Pulp Fiction", "year": 1994, "description": "Quentin Tarantino's masterpiece."},
        {"title": "Goodfellas", "year": 1990, "description": "True story of mob life."},
        {"title": "The Green Mile", "year": 1999, "description": "Prison drama with supernatural elements."},
        {"title": "Schindler's List", "year": 1993, "description": "Holocaust drama masterpiece."},
        {"title": "12 Angry Men", "year": 1957, "description": "Jury room drama classic."}
    ],
    "Horror": [
        {"title": "The Shining", "year": 1980, "description": "Psychological horror in a haunted hotel."},
        {"title": "A Nightmare on Elm Street", "year": 1984, "description": "Freddy Krueger terrorizes dreams."},
        {"title": "The Exorcist", "year": 1973, "description": "Classic demonic possession horror."},
        {"title": "Halloween", "year": 1978, "description": "Michael Myers stalks babysitters."},
        {"title": "Get Out", "year": 2017, "description": "Social thriller with horror elements."},
        {"title": "Alien", "year": 1979, "description": "Space horror masterpiece."},
        {"title": "The Thing", "year": 1982, "description": "Antarctic horror thriller."},
        {"title": "The Silence of the Lambs", "year": 1991, "description": "Psychological thriller horror."}
    ],
    "Sci-Fi": [
        {"title": "Blade Runner", "year": 1982, "description": "Neo-noir sci-fi about replicants."},
        {"title": "The Matrix", "year": 1999, "description": "Reality-bending sci-fi action."},
        {"title": "Interstellar", "year": 2014, "description": "Space exploration and time travel."},
        {"title": "Arrival", "year": 2016, "description": "First contact with alien life."},
        {"title": "Ex Machina", "year": 2014, "description": "AI consciousness thriller."},
        {"title": "2001: A Space Odyssey", "year": 1968, "description": "Sci-fi masterpiece."},
        {"title": "E.T. the Extra-Terrestrial", "year": 1982, "description": "Family-friendly alien story."},
        {"title": "Back to the Future", "year": 1985, "description": "Time travel adventure."}
    ],
    "Thriller": [
        {"title": "Se7en", "year": 1995, "description": "Serial killer thriller with Brad Pitt."},
        {"title": "Gone Girl", "year": 2014, "description": "Psychological thriller about marriage."},
        {"title": "The Silence of the Lambs", "year": 1991, "description": "FBI agent vs. serial killer."},
        {"title": "Memento", "year": 2000, "description": "Memory loss thriller."},
        {"title": "Fight Club", "year": 1999, "description": "Underground fighting club thriller."},
        {"title": "The Usual Suspects", "year": 1995, "description": "Crime thriller with twist ending."},
        {"title": "Shutter Island", "year": 2010, "description": "Psychological thriller mystery."},
        {"title": "Inception", "year": 2010, "description": "Dream-stealing sci-fi thriller."}
    ]
}

def get_movie_recommendations(selected_genres, count):
    """Get movie recommendations from local database - NO API NEEDED"""
    recommendations = []
    
    for genre in selected_genres:
        if genre in MOVIE_DATABASE:
            genre_movies = MOVIE_DATABASE[genre].copy()
            random.shuffle(genre_movies)
            recommendations.extend(genre_movies[:count//len(selected_genres) + 1])
    
    random.shuffle(recommendations)
    return recommendations[:count]

def main():
    st.title("🎬 Movie Recommender")
    st.markdown("### Discover your next favorite movie!")
    
    # Status indicator - ALWAYS WORKING
    st.success("✅ Movie Recommender is Ready! No API needed!")
    
    # Genre selection
    st.sidebar.header("🎭 Choose Genres")
    selected_genres = st.sidebar.multiselect(
        "Select your favorite genres:",
        list(MOVIE_DATABASE.keys()),
        default=[]
    )
    
    # Number of recommendations
    num_recommendations = st.sidebar.slider(
        "Number of movies to recommend:",
        min_value=1,
        max_value=15,
        value=5
    )
    
    # Get recommendations button
    if st.sidebar.button("🎯 Get Recommendations", type="primary"):
        if selected_genres:
            with st.spinner("Finding the perfect movies for you..."):
                recommendations = get_movie_recommendations(selected_genres, num_recommendations)
                st.success(f"Found {len(recommendations)} movies for you!")
                
                # Display recommendations
                for i, movie in enumerate(recommendations, 1):
                    with st.container():
                        st.markdown(f"""
                        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0; border-left: 5px solid #1f77b4;">
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
        - 😱 Thriller
        
        Start by selecting genres from the sidebar!
        """)
        
        # Show sample movies
        st.subheader("🎬 Popular Movies by Genre")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Action**")
            st.write("• The Dark Knight")
            st.write("• Mad Max: Fury Road")
            st.write("• John Wick")
        
        with col2:
            st.markdown("**Comedy**")
            st.write("• The Grand Budapest Hotel")
            st.write("• Superbad")
            st.write("• The Hangover")
        
        with col3:
            st.markdown("**Drama**")
            st.write("• The Shawshank Redemption")
            st.write("• Forrest Gump")
            st.write("• The Godfather")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🎬 Movie Recommender App | Powered by Streamlit</p>
        <p>✅ 100% Standalone - No API Dependencies</p>
        <p>📚 48+ Curated Movies</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
