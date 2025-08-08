from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database.connection import get_db
from ..models.movie import MovieResponse, GenreResponse
from ..services.movie_service import MovieService

router = APIRouter(prefix="/api/movies", tags=["movies"])


@router.get("/", response_model=List[MovieResponse])
def get_movies(
    genre: Optional[str] = Query(None, description="Filter by genre"),
    limit: Optional[int] = Query(None, ge=1, le=100, description="Limit number of results"),
    offset: Optional[int] = Query(None, ge=0, description="Offset for pagination"),
    db: Session = Depends(get_db)
):
    """
    Get all movies with optional filtering and pagination
    """
    try:
        if genre:
            movies = MovieService.get_movies_by_genre(db, [genre])
        else:
            movies = MovieService.get_all_movies(db, limit=limit, offset=offset)
        
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving movies: {str(e)}")


@router.get("/genres", response_model=GenreResponse)
def get_genres(db: Session = Depends(get_db)):
    """
    Get all available genres
    """
    try:
        genres = MovieService.get_available_genres(db)
        return GenreResponse(genres=genres)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving genres: {str(e)}")


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    """
    Get a specific movie by ID
    """
    try:
        movie = MovieService.get_movie_by_id(db, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving movie: {str(e)}")


@router.get("/count/total")
def get_movies_count(db: Session = Depends(get_db)):
    """
    Get total number of movies in database
    """
    try:
        count = MovieService.get_movies_count(db)
        return {"total_movies": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving movie count: {str(e)}") 