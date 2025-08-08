from .models import Movie
from .connection import SessionLocal
import random


def get_seed_movies():
    """Return list of seed movies"""
    return [
        # Action Movies
        {
            "title": "The Dark Knight",
            "genre": "Action",
            "year": 2008,
            "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"
        },
        {
            "title": "Mad Max: Fury Road",
            "genre": "Action",
            "year": 2015,
            "description": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTcwYjEyNTBiZmM1XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"
        },
        {
            "title": "John Wick",
            "genre": "Action",
            "year": 2014,
            "description": "An ex-hit-man comes out of retirement to track down the gangsters that killed his dog and took everything from him.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwNTM2MTk4MzE@._V1_.jpg"
        },
        {
            "title": "Mission: Impossible - Fallout",
            "genre": "Action",
            "year": 2018,
            "description": "Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNjRlZmM4ODAtY2I1YS00ZDdmLTkyYTgtZjI5MWU3NmZkMTEwXkEyXkFqcGdeQXVyMzY0MTE3NzU@._V1_.jpg"
        },
        {
            "title": "The Matrix",
            "genre": "Action",
            "year": 1999,
            "description": "A computer programmer discovers that reality as he knows it is a simulation created by machines, and joins a rebellion to break free.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
        },

        # Comedy Movies
        {
            "title": "The Grand Budapest Hotel",
            "genre": "Comedy",
            "year": 2014,
            "description": "A writer encounters the owner of an aging hotel who tells him of his early years as a lobby boy in the hotel's glorious years under an exceptional concierge.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMzM5NjUxNjY5MV5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_.jpg"
        },
        {
            "title": "Shaun of the Dead",
            "genre": "Comedy",
            "year": 2004,
            "description": "A man decides to turn his moribund life around by winning back his ex-girlfriend, reconciling his relationship with his mother, and dealing with an entire community that has returned from the dead to eat the living.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTUxODc1OTcxOV5BMl5BanBnXkFtZTcwOTM2Mjk3NA@@._V1_.jpg"
        },
        {
            "title": "Superbad",
            "genre": "Comedy",
            "year": 2007,
            "description": "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMjA0ODM5MjM5NF5BMl5BanBnXkFtZTcwNjA1ODI5NQ@@._V1_.jpg"
        },
        {
            "title": "The Hangover",
            "genre": "Comedy",
            "year": 2009,
            "description": "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNGQwZjg5YmYtY2VkNC00NzliLTljYTctNzI5NmU3MjE2ODQzXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"
        },
        {
            "title": "Bridesmaids",
            "genre": "Comedy",
            "year": 2011,
            "description": "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMjA1Njk0OTU2N15BMl5BanBnXkFtZTcwNjQzNDU5NA@@._V1_.jpg"
        },

        # Drama Movies
        {
            "title": "The Shawshank Redemption",
            "genre": "Drama",
            "year": 1994,
            "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg"
        },
        {
            "title": "Forrest Gump",
            "genre": "Drama",
            "year": 1994,
            "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
        },
        {
            "title": "The Green Mile",
            "genre": "Drama",
            "year": 1999,
            "description": "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTUxMzQyNjA5Nl5BMl5BanBnXkFtZTYwOTU2NTY3._V1_.jpg"
        },
        {
            "title": "Schindler's List",
            "genre": "Drama",
            "year": 1993,
            "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTUyNjU3XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
        },
        {
            "title": "12 Angry Men",
            "genre": "Drama",
            "year": 1957,
            "description": "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYzlBMGVjZTRhN2UwXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_.jpg"
        },

        # Horror Movies
        {
            "title": "The Shining",
            "genre": "Horror",
            "year": 1980,
            "description": "A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence, while his psychic son sees horrific forebodings from both past and future.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjRhOS00MjUwLWIyMGMtNjMxY2Q3YzFjMDFmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
        },
        {
            "title": "A Nightmare on Elm Street",
            "genre": "Horror",
            "year": 1984,
            "description": "The monstrous spirit of a slain child murderer seeks revenge by invading the dreams of teenagers whose parents were responsible for his untimely death.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNzFjNmNhNWQtNTAyNS00OThkLTg1N2ItYjFiYzNhOTMxZWRkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
        },
        {
            "title": "The Exorcist",
            "genre": "Horror",
            "year": 1973,
            "description": "When a 12-year-old girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BYWFlZGY2NDktY2ZjOS00ZWNlLTgwODZkNThlOTlkYjUwXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg"
        },
        {
            "title": "Halloween",
            "genre": "Horror",
            "year": 1978,
            "description": "Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield, Illinois to kill again.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNzk1OGU2NmMtNTdhZC00NjdlLWE5YTMtZTQ0YzZhMzNkNDI5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
        },
        {
            "title": "Get Out",
            "genre": "Horror",
            "year": 2017,
            "description": "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc4MTI@._V1_.jpg"
        },

        # Sci-Fi Movies
        {
            "title": "Inception",
            "genre": "Sci-Fi",
            "year": 2010,
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg"
        },
        {
            "title": "Interstellar",
            "genre": "Sci-Fi",
            "year": 2014,
            "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"
        },
        {
            "title": "Blade Runner",
            "genre": "Sci-Fi",
            "year": 1982,
            "description": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
        },
        {
            "title": "The Martian",
            "genre": "Sci-Fi",
            "year": 2015,
            "description": "An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_.jpg"
        },
        {
            "title": "Arrival",
            "genre": "Sci-Fi",
            "year": 2016,
            "description": "A linguist works with the military to communicate with alien lifeforms after twelve mysterious spacecraft appear around the world.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNzFjNmNhNWQtNTAyNS00OThkLTg1N2ItYjFiYzNhOTMxZWRkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
        },

        # Thriller Movies
        {
            "title": "Gone Girl",
            "genre": "Thriller",
            "year": 2014,
            "description": "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTk0MDQ3MzAzOV5BMl5BanBnXkFtZTgwNzU1NzE3MjE@._V1_.jpg"
        },
        {
            "title": "The Silence of the Lambs",
            "genre": "Thriller",
            "year": 1991,
            "description": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLGE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
        },
        {
            "title": "Se7en",
            "genre": "Thriller",
            "year": 1995,
            "description": "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his modus operandi.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
        },
        {
            "title": "Fight Club",
            "genre": "Thriller",
            "year": 1999,
            "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BNDIzNDU0YzEtYzE5Ni00ZjlkLTk5ZjgtNjM3NWE4YzA3Nzk3XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg"
        },
        {
            "title": "Zodiac",
            "genre": "Thriller",
            "year": 2007,
            "description": "Between 1968 and 1983, a San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac Killer, an unidentified individual who terrorizes Northern California with a killing spree.",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BMTQxNjc1NzQ2OF5BMl5BanBnXkFtZTgwOTQxMjI5MzI@._V1_.jpg"
        }
    ]


def seed_database():
    """Seed the database with initial movie data"""
    db = SessionLocal()
    try:
        # Check if movies already exist
        existing_movies = db.query(Movie).count()
        if existing_movies > 0:
            print(f"Database already contains {existing_movies} movies. Skipping seed.")
            return

        # Get seed movies
        movies_data = get_seed_movies()
        
        # Create movie objects
        movies = []
        for movie_data in movies_data:
            movie = Movie(**movie_data)
            movies.append(movie)
        
        # Add to database
        db.add_all(movies)
        db.commit()
        
        print(f"Successfully seeded database with {len(movies)} movies.")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    # Create tables
    from .connection import engine
    from .models import Base
    Base.metadata.create_all(bind=engine)
    
    # Seed database
    seed_database() 