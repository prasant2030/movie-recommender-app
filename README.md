# Movie Recommendation Backend

A FastAPI-based backend for a movie recommendation system with SQLite database.

## Project Structure
```
movie_recommendation_backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database connection
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py             # Database operations
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── movies.py
│   │   │   │   ├── recommendations.py
│   │   │   │   └── preferences.py
│   │   │   └── api.py
│   │   └── deps.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   └── utils/
│       ├── __init__.py
│       └── recommendation_engine.py
├── scripts/
│   └── seed_data.py
├── requirements.txt
└── README.md
```

## Features
- Movie CRUD operations
- Genre-based movie recommendations
- User preference tracking
- Simple recommendation engine
- SQLite database with seed data

## Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Run seed script: `python scripts/seed_data.py`
3. Start server: `uvicorn app.main:app --reload`

## API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 