from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database.connection import get_db
from ..models.movie import RecommendationRequest, RecommendationResponse, MovieResponse
from ..services.recommendation_service import RecommendationService
from ..services.movie_service import MovieService

router = APIRouter(prefix="/api/recommendations", tags=["recommendations"])


@router.post("/", response_model=RecommendationResponse)
def get_recommendations(
    request: RecommendationRequest,
    db: Session = Depends(get_db)
):
    """
    Get movie recommendations based on selected genres
    """
    try:
        # Validate that requested genres exist
        available_genres = MovieService.get_available_genres(db)
        invalid_genres = [genre for genre in request.genres if genre not in available_genres]
        
        if invalid_genres:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid genres: {invalid_genres}. Available genres: {available_genres}"
            )
        
        # Validate count
        if request.count <= 0:
            raise HTTPException(status_code=400, detail="Count must be greater than 0")
        
        if request.count > 50:
            raise HTTPException(status_code=400, detail="Count cannot exceed 50")
        
        # Get recommendations
        recommendations = RecommendationService.get_recommendations_with_fallback(
            db=db,
            genres=request.genres,
            count=request.count
        )
        
        return RecommendationResponse(
            movies=recommendations,
            total_count=len(recommendations)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")


@router.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "service": "movie-recommendation-api"} 