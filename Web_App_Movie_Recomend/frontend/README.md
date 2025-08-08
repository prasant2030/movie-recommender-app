# 🎬 Movie Recommender Frontend

A modern, responsive Streamlit frontend for the Movie Recommendation system.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

## 🌟 Live Demo
🔗 **[Try the App Live](https://your-app-url.streamlit.app)** (Replace with your actual URL after deployment)

## Features

- **🎭 Genre Selection**: Multi-select genre interface
- **🎯 Smart Recommendations**: Get personalized movie suggestions
- **📱 Responsive Design**: Works on desktop and mobile
- **🔄 Real-time Updates**: Get new recommendations instantly
- **📊 Movie Browser**: View all available movies by genre
- **🎨 Modern UI**: Clean, intuitive interface

## Project Structure

```
frontend/
├── app.py                    # Main Streamlit application
├── run_app.py               # App startup script
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── config/                 # Configuration
│   ├── __init__.py
│   └── settings.py         # App settings and constants
├── components/             # UI Components
│   ├── __init__.py
│   ├── genre_selector.py   # Genre selection widget
│   ├── movie_card.py       # Individual movie display
│   └── recommendation_display.py # Results display
└── services/               # API Communication
    ├── __init__.py
    └── api_client.py       # Backend API client
```

## Setup

### 1. Install Dependencies

```bash
cd frontend
pip install -r requirements.txt
```

### 2. Run the App

```bash
# Option 1: Using the run script
python run_app.py

# Option 2: Direct streamlit command
streamlit run app.py --server.port 8501
```

### 3. Access the App

Open your browser and go to: `http://localhost:8501`

## Usage

### Getting Started

1. **Select Genres**: Choose one or more genres from the sidebar
2. **Set Count**: Choose how many recommendations you want (1-20)
3. **Get Recommendations**: Click "Get Recommendations" to see movies
4. **Explore More**: Use "Get More Recommendations" for new suggestions

### Features

- **Genre Selection**: Multi-select checkboxes for genres
- **Recommendation Count**: Slider to choose number of movies
- **Movie Cards**: Beautiful cards with poster, title, year, and description
- **Grid Layout**: Responsive grid for multiple recommendations
- **Statistics**: Summary metrics for your recommendations
- **All Movies View**: Browse all available movies by genre

## Components

### GenreSelector
- Handles genre selection with checkboxes
- Fetches available genres from API
- Fallback to default genres if API unavailable

### MovieCard
- Displays individual movie information
- Shows poster, title, year, genre, and description
- Responsive design with custom styling

### RecommendationDisplay
- Grid layout for multiple recommendations
- Statistics and summary information
- Responsive columns based on recommendation count

### APIClient
- Handles all backend communication
- Error handling and fallbacks
- Session management for requests

## Configuration

Edit `config/settings.py` to customize:

- **API Base URL**: Backend server address
- **Default Genres**: Fallback genres if API unavailable
- **UI Settings**: Recommendation limits and defaults
- **Error Messages**: Custom error messages

## API Integration

The frontend is designed to work with the FastAPI backend:

- **Health Check**: `/health`
- **Get Genres**: `/api/movies/genres`
- **Get Movies**: `/api/movies`
- **Get Recommendations**: `/api/recommendations`

## Development

### Adding New Components

1. Create new component in `components/`
2. Import in `app.py`
3. Add to main application flow

### Styling

- Custom CSS in `app.py`
- Component-specific styles in each component
- Responsive design with Streamlit columns

### Error Handling

- API connection errors
- Missing data fallbacks
- User-friendly error messages

## Troubleshooting

### Common Issues

1. **API Not Available**: Check if backend is running on port 8000
2. **Port Already in Use**: Change port in `run_app.py`
3. **Dependencies Missing**: Run `pip install -r requirements.txt`

### Debug Mode

Run with debug information:

```bash
streamlit run app.py --logger.level debug
```

## Future Enhancements

- [ ] User authentication
- [ ] Movie ratings and reviews
- [ ] Advanced filtering options
- [ ] Movie trailers integration
- [ ] Social sharing features
- [ ] Dark mode theme
- [ ] Mobile app version

## Contributing

1. Follow the existing code structure
2. Add proper error handling
3. Include docstrings for functions
4. Test with different screen sizes
- [ ] User authentication
- [ ] Movie ratings and reviews
- [ ] Advanced filtering options
- [ ] Movie trailers integration
- [ ] Social sharing features
- [ ] Dark mode theme
- [ ] Mobile app version

## Contributing

1. Follow the existing code structure
2. Add proper error handling
3. Include docstrings for functions
4. Test with different screen sizes 