#!/usr/bin/env python3
"""
Movie Recommendation App - Streamlit Frontend (Working Version)
Always works - no API connection issues
"""

import streamlit as st
import random
from typing import List, Dict

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
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .status-indicator {
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
    }
    .status-working {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
</style>
""", unsafe_allow_html=True)

# Complete movie database
MOVIE_DATABASE = {
    "Action": [
        {"title": "The Dark Knight", "genre": "Action", "year": 2008, "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."},
        {"title": "Mad Max: Fury Road", "genre": "Action", "year": 2015, "description": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max."},
        {"title": "John Wick", "genre": "Action", "year": 2014, "description": "An ex-hitman comes out of retirement to track down the gangsters who killed his dog and stole his car."},
        {"title": "Mission: Impossible - Fallout", "genre": "Action", "year": 2018, "description": "Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission goes wrong."},
        {"title": "The Avengers", "genre": "Action", "year": 2012, "description": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity."},
        {"title": "Die Hard", "genre": "Action", "year": 1988, "description": "An action classic where an off-duty cop must save hostages from terrorists in a Los Angeles skyscraper."},
        {"title": "Gladiator", "genre": "Action", "year": 2000, "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery."},
        {"title": "The Matrix", "genre": "Action", "year": 1999, "description": "A computer programmer discovers that reality as he knows it is a simulation created by machines, and joins a rebellion to break free."}
    ],
    "Comedy": [
        {"title": "The Grand Budapest Hotel", "genre": "Comedy", "year": 2014, "description": "A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel's glorious years under an exceptional concierge."},
        {"title": "Superbad", "genre": "Comedy", "year": 2007, "description": "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry."},
        {"title": "Bridesmaids", "genre": "Comedy", "year": 2011, "description": "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef."},
        {"title": "The Hangover", "genre": "Comedy", "year": 2009, "description": "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding."},
        {"title": "Shaun of the Dead", "genre": "Comedy", "year": 2004, "description": "A man decides to turn his moribund life around by winning back his ex-girlfriend, reconciling his relationship with his mother, and dealing with an entire community that has returned from the dead to eat the living."},
        {"title": "The Big Lebowski", "genre": "Comedy", "year": 1998, "description": "Jeff 'The Dude' Lebowski, mistaken for a millionaire of the same name, seeks restitution for his ruined rug and enlists his bowling buddies to help get it."},
        {"title": "Groundhog Day", "genre": "Comedy", "year": 1993, "description": "A weatherman finds himself inexplicably living the same day over and over again."},
        {"title": "Monty Python and the Holy Grail", "genre": "Comedy", "year": 1975, "description": "King Arthur and his Knights of the Round Table embark on a surreal, low-budget search for the Holy Grail, encountering many very silly obstacles."}
    ],
    "Drama": [
        {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994, "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
        {"title": "Forrest Gump", "genre": "Drama", "year": 1994, "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart."},
        {"title": "The Green Mile", "genre": "Drama", "year": 1999, "description": "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift."},
        {"title": "Schindler's List", "genre": "Drama", "year": 1993, "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis."},
        {"title": "12 Angry Men", "genre": "Drama", "year": 1957, "description": "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence."},
        {"title": "The Godfather", "genre": "Drama", "year": 1972, "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."},
        {"title": "Pulp Fiction", "genre": "Drama", "year": 1994, "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."},
        {"title": "Goodfellas", "genre": "Drama", "year": 1990, "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito."}
    ],
    "Horror": [
        {"title": "The Shining", "genre": "Horror", "year": 1980, "description": "A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future."},
        {"title": "A Nightmare on Elm Street", "genre": "Horror", "year": 1984, "description": "The monstrous spirit of a slain janitor seeks revenge by invading the dreams of teenagers whose parents were responsible for his untimely death."},
        {"title": "The Exorcist", "genre": "Horror", "year": 1973, "description": "When a 12-year-old girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her."},
        {"title": "Halloween", "genre": "Horror", "year": 1978, "description": "Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield, Illinois to kill again."},
        {"title": "The Silence of the Lambs", "genre": "Horror", "year": 1991, "description": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims."},
        {"title": "Alien", "genre": "Horror", "year": 1979, "description": "After a space merchant vessel receives an unknown transmission as a distress call, one of the crew is attacked by a mysterious life form and they soon realize that its life cycle has merely begun."},
        {"title": "The Thing", "genre": "Horror", "year": 1982, "description": "A research team in Antarctica is hunted by a shape-shifting alien that assumes the appearance of its victims."},
        {"title": "Get Out", "genre": "Horror", "year": 2017, "description": "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point."}
    ],
    "Sci-Fi": [
        {"title": "Blade Runner", "genre": "Sci-Fi", "year": 1982, "description": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator."},
        {"title": "The Matrix", "genre": "Sci-Fi", "year": 1999, "description": "A computer programmer discovers that reality as he knows it is a simulation created by machines, and joins a rebellion to break free."},
        {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
        {"title": "Arrival", "genre": "Sci-Fi", "year": 2016, "description": "A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world."},
        {"title": "Ex Machina", "genre": "Sci-Fi", "year": 2014, "description": "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a highly advanced humanoid A.I."},
        {"title": "2001: A Space Odyssey", "genre": "Sci-Fi", "year": 1968, "description": "After discovering a mysterious artifact buried beneath the Lunar surface, mankind sets off on a quest to find its origins with help from intelligent supercomputer H.A.L. 9000."},
        {"title": "E.T. the Extra-Terrestrial", "genre": "Sci-Fi", "year": 1982, "description": "A troubled child summons the courage to help a friendly alien escape Earth and return to his home world."},
        {"title": "Back to the Future", "genre": "Sci-Fi", "year": 1985, "description": "Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the eccentric scientist Doc Brown."}
    ],
    "Thriller": [
        {"title": "Se7en", "genre": "Thriller", "year": 1995, "description": "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi."},
        {"title": "Gone Girl", "genre": "Thriller", "year": 2014, "description": "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent."},
        {"title": "The Silence of the Lambs", "genre": "Thriller", "year": 1991, "description": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims."},
        {"title": "Memento", "genre": "Thriller", "year": 2000, "description": "A man with short-term memory loss attempts to track down his wife's murderer."},
        {"title": "Fight Club", "genre": "Thriller", "year": 1999, "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more."},
        {"title": "The Usual Suspects", "genre": "Thriller", "year": 1995, "description": "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which began when five criminals met at a seemingly random police lineup."},
        {"title": "Shutter Island", "genre": "Thriller", "year": 2010, "description": "In 1954, a U.S. Marshal investigates the disappearance of a murderer who escaped from a hospital for the criminally insane."},
        {"title": "Inception", "genre": "Thriller", "year": 2010, "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."}
    ]
}

AVAILABLE_GENRES = list(MOVIE_DATABASE.keys())

def get_movie_recommendations(selected_genres: List[str], count: int) -> List[Dict]:
    """Get movie recommendations from local database"""
    recommendations = []
    
    # Get movies from selected genres
    for genre in selected_genres:
        if genre in MOVIE_DATABASE:
            genre_movies = MOVIE_DATABASE[genre].copy()
            random.shuffle(genre_movies)
            # Add movies from this genre
            recommendations.extend(genre_movies[:count//len(selected_genres) + 1])
    
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
    
    # Status indicator - always working
    st.markdown('<div class="status-indicator status-working">✅ Movie Recommender is Ready!</div>', unsafe_allow_html=True)
    
    # Sidebar for genre selection
    with st.sidebar:
        st.header("🎭 Genre Selection")
        st.markdown("Select one or more genres to get personalized recommendations:")
        
        # Genre selection
        selected_genres = st.multiselect(
            "Choose your favorite genres:",
            options=AVAILABLE_GENRES,
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
                    recommendations = get_movie_recommendations(
                        selected_genres=selected_genres,
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
        
        # Show some sample movies
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
        <p>✅ Always Working - No API Dependencies</p>
        <p>📚 Curated Movie Database with 48+ Movies</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
