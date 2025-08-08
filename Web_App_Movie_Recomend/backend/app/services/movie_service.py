from sqlalchemy.orm import Session
from typing import List, Optional
from ..database.models import Movie
from ..models.movie import MovieResponse


class MovieService:
    """Service class for movie-related operations"""
    
    @staticmethod
    def get_all_movies(db: Session, limit: Optional[int] = None, offset: Optional[int] = None) -> List[Movie]:
        """Get all movies with optional pagination"""
        query = db.query(Movie)
        
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
            
        return query.all()
    
    @staticmethod
    def get_movies_by_genre(db: Session, genres: List[str]) -> List[Movie]:
        """Get movies by specified genres"""
        return db.query(Movie).filter(Movie.genre.in_(genres)).all()
    
    @staticmethod
    def get_available_genres(db: Session) -> List[str]:
        """Get all unique genres from the database"""
        genres = db.query(Movie.genre).distinct().all()
        return [genre[0] for genre in genres]
    
    @staticmethod
    def get_movie_by_id(db: Session, movie_id: int) -> Optional[Movie]:
        """Get a specific movie by ID"""
        return db.query(Movie).filter(Movie.id == movie_id).first()
    
    @staticmethod
    def get_movies_count(db: Session) -> int:
        """Get total number of movies in database"""
        return db.query(Movie).count()
    
    @staticmethod
    def get_movies_count_by_genre(db: Session, genres: List[str]) -> int:
        """Get count of movies for specified genres"""
        return db.query(Movie).filter(Movie.genre.in_(genres)).count() 