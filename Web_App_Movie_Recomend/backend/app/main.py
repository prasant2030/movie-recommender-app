from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database.connection import engine
from .database.models import Base
from .api import movies, recommendations

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Movie Recommendation API",
    description="A simple API for movie recommendations based on genre preferences",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(movies.router)
app.include_router(recommendations.router)


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Movie Recommendation API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "movies": "/api/movies",
            "genres": "/api/movies/genres",
            "recommendations": "/api/recommendations"
        }
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    
    return {"status": "healthy", "service": "movie-recommendation-api"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 