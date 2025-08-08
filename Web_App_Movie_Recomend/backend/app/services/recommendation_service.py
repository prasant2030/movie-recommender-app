import random
from sqlalchemy.orm import Session
from typing import List
from ..database.models import Movie
from ..models.movie import MovieResponse
from .movie_service import MovieService


class RecommendationService:
    """Service class for recommendation logic"""
    
    @staticmethod
    def get_random_recommendations(
        db: Session, 
        genres: List[str], 
        count: int,
        exclude_ids: List[int] = None
    ) -> List[Movie]:
        """
        Get random movie recommendations from specified genres
        
        Args:
            db: Database session
            genres: List of genres to select from
            count: Number of recommendations to return
            exclude_ids: List of movie IDs to exclude (for session history)
        
        Returns:
            List of randomly selected movies
        """
        # Get all movies from specified genres
        movies = MovieService.get_movies_by_genre(db, genres)
        
        if not movies:
            return []
        
        # Exclude previously shown movies if provided
        if exclude_ids:
            movies = [movie for movie in movies if movie.id not in exclude_ids]
        
        # If we don't have enough movies after exclusion, return all available
        if len(movies) <= count:
            return movies
        
        # Randomly select the requested number of movies
        return random.sample(movies, count)
    
    @staticmethod
    def get_recommendations_with_fallback(
        db: Session,
        genres: List[str],
        count: int,
        exclude_ids: List[int] = None
    ) -> List[Movie]:
        """
        Get recommendations with fallback logic
        
        If not enough movies in selected genres, fall back to all movies
        """
        recommendations = RecommendationService.get_random_recommendations(
            db, genres, count, exclude_ids
        )
        
        # If we don't have enough recommendations, get from all movies
        if len(recommendations) < count:
            all_movies = MovieService.get_all_movies(db)
            
            if exclude_ids:
                all_movies = [movie for movie in all_movies if movie.id not in exclude_ids]
            
            # Get additional movies to reach the requested count
            remaining_count = count - len(recommendations)
            additional_movies = random.sample(all_movies, min(remaining_count, len(all_movies)))
            
            recommendations.extend(additional_movies)
        
        return recommendations[:count] 