# 📁 Repository Structure for App_Devopment

## Recommended Folder Organization

```
App_Devopment/
├── README.md                           # Main repository README
├── LICENSE                             # MIT License
├── movie-recommender/                  # Movie Recommender Project
│   ├── app.py                         # Main Streamlit app
│   ├── requirements.txt               # Dependencies
│   ├── README.md                      # Project-specific README
│   ├── .streamlit/
│   │   └── config.toml               # Streamlit config
│   ├── components/                    # UI Components
│   │   ├── __init__.py
│   │   ├── genre_selector.py
│   │   ├── movie_card.py
│   │   └── recommendation_display.py
│   ├── config/                        # Configuration
│   │   ├── __init__.py
│   │   └── settings.py
│   └── services/                      # API Services
│       ├── __init__.py
│       └── api_client.py
└── other-projects/                    # Future projects
    └── ...
```

## For Streamlit Cloud Deployment

- **Repository**: `prasant2030/App_Devopment`
- **Branch**: `main`
- **Main file path**: `movie-recommender/app.py`
- **App URL**: `movie-recommender-prasant`