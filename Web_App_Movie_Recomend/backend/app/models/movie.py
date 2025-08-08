from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class MovieBase(BaseModel):
    title: str
    genre: str
    year: int
    description: str
    poster_url: str


class MovieResponse(MovieBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class GenreResponse(BaseModel):
    genres: List[str]


class RecommendationRequest(BaseModel):
    genres: List[str]
    count: int = 5


class RecommendationResponse(BaseModel):
    movies: List[MovieResponse]
    total_count: int 