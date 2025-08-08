# Movie Recommendation API Backend

A FastAPI-based backend for a movie recommendation system that provides random movie suggestions based on genre preferences.

## Features

- **Simple Recommendation Logic**: Random selection of movies by genre
- **RESTful API**: Clean, documented endpoints
- **SQLite Database**: Lightweight, file-based database
- **Seed Data**: 30 popular movies across 6 genres
- **CORS Support**: Ready for frontend integration
- **Health Checks**: Monitoring endpoints

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── models/              # Pydantic models
│   │   ├── __init__.py
│   │   └── movie.py         # Movie data models
│   ├── database/            # Database layer
│   │   ├── __init__.py
│   │   ├── connection.py    # SQLite connection management
│   │   ├── models.py        # SQLAlchemy models
│   │   └── seed_data.py     # Initial movie data
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── movie_service.py # Movie operations
│   │   └── recommendation_service.py # Recommendation logic
│   └── api/                 # API routes
│       ├── __init__.py
│       ├── movies.py        # Movie endpoints
│       └── recommendations.py # Recommendation endpoints
├── requirements.txt
├── seed_database.py         # Database seeding script
└── README.md
```

## Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Seed the Database

```bash
python seed_database.py
```

This will create the database and populate it with 30 movies across 6 genres:
- Action (5 movies)
- Comedy (5 movies)
- Drama (5 movies)
- Horror (5 movies)
- Sci-Fi (5 movies)
- Thriller (5 movies)

### 3. Run the Server

```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Core Endpoints

#### `GET /api/movies`
Get all movies with optional filtering
- Query params: `genre`, `limit`, `offset`
- Response: List of movies

#### `GET /api/movies/genres`
Get all available genres
- Response: List of unique genres

#### `POST /api/recommendations`
Get movie recommendations
- Request body: `{"genres": ["Action", "Comedy"], "count": 5}`
- Response: Random movies from selected genres

#### `GET /api/movies/{movie_id}`
Get specific movie details
- Response: Movie details

### Utility Endpoints

#### `GET /`
API information and available endpoints

#### `GET /health`
Health check endpoint

#### `GET /api/movies/count/total`
Get total number of movies in database

## API Documentation

Once the server is running, you can access:
- **Interactive API Docs**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

## Database Schema

### Movies Table
- `id` (Primary Key)
- `title` (Text)
- `genre` (Text, indexed)
- `year` (Integer, indexed)
- `description` (Text)
- `poster_url` (Text)
- `created_at` (Timestamp)

## Recommendation Logic

The recommendation system uses a simple random selection algorithm:

1. **Genre Filtering**: Select movies from requested genres
2. **Random Selection**: Pick N random movies from filtered results
3. **Fallback Logic**: If not enough movies in selected genres, include movies from all genres
4. **Session Management**: Optional exclusion of previously shown movies

## Development

### Adding New Movies

To add new movies to the database:

1. Edit `app/database/seed_data.py`
2. Add new movie entries to the `get_seed_movies()` function
3. Run `python seed_database.py` again

### Extending the API

The modular structure makes it easy to add new features:

- **New Models**: Add to `app/models/`
- **New Services**: Add to `app/services/`
- **New Endpoints**: Add to `app/api/`

## Error Handling

The API includes comprehensive error handling:
- **400 Bad Request**: Invalid input parameters
- **404 Not Found**: Requested resource doesn't exist
- **500 Internal Server Error**: Server-side errors

## CORS Configuration

The API is configured to allow cross-origin requests from any origin. In production, you should specify actual frontend origins.

## Testing

You can test the API using the interactive documentation at `/docs` or with tools like curl:

```bash
# Get all genres
curl http://localhost:8000/api/movies/genres

# Get recommendations
curl -X POST http://localhost:8000/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{"genres": ["Action", "Comedy"], "count": 3}'
``` 