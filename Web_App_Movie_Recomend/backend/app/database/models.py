from sqlalchemy import Column, Integer, String, Text, DateTime, Index
from sqlalchemy.sql import func
from .connection import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    genre = Column(String(100), nullable=False, index=True)
    year = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    poster_url = Column(String(500), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Create index on genre for faster queries
    __table_args__ = (
        Index('idx_movies_genre', 'genre'),
        Index('idx_movies_year', 'year'),
    ) 