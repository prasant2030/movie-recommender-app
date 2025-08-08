# 🎬 Movie Recommender

A modern, responsive Streamlit frontend for movie recommendations.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-recommender-prasant.streamlit.app)

## 🌟 Live Demo
🔗 **[Try the App Live](https://movie-recommender-prasant.streamlit.app)** *(Update this URL after deployment)*

## ✨ Features

- **🎭 Genre Selection**: Multi-select genre interface
- **🎯 Smart Recommendations**: Get personalized movie suggestions
- **📱 Responsive Design**: Works on desktop and mobile
- **🔄 Real-time Updates**: Get new recommendations instantly
- **📊 Movie Browser**: View all available movies by genre
- **🎨 Modern UI**: Clean, intuitive interface

## 🚀 Quick Start

### Online (Streamlit Cloud)
Just visit: [https://movie-recommender-prasant.streamlit.app](https://movie-recommender-prasant.streamlit.app)

### Local Development
```bash
# Clone repository
git clone https://github.com/prasant2030/App_Devopment.git
cd App_Devopment/movie-recommender

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit 1.48+
- **Language**: Python 3.11+
- **Dependencies**: requests, pandas, pillow
- **Styling**: Custom CSS
- **Deployment**: Streamlit Cloud

## 📁 Project Structure

```
movie-recommender/
├── app.py                              # Main Streamlit application
├── requirements.txt                    # Python dependencies
├── .streamlit/
│   └── config.toml                    # Streamlit configuration
├── components/                         # UI Components
│   ├── genre_selector.py              # Genre selection widget
│   ├── movie_card.py                  # Individual movie display
│   └── recommendation_display.py      # Results display
├── config/
│   └── settings.py                    # App settings and constants
└── services/
    └── api_client.py                  # Backend API client
```

## 🎯 How to Use

1. **Select Genres**: Choose one or more genres from the sidebar
2. **Set Count**: Choose how many recommendations you want (1-20)
3. **Get Recommendations**: Click "Get Recommendations" to see movies
4. **Explore More**: Use "Get More Recommendations" for new suggestions

## ⚙️ Configuration

The app works with or without a backend API:
- **With Backend**: Fetches real movie data from API
- **Without Backend**: Uses fallback data and shows appropriate messages

## 🚀 Deployment

This app is deployed on **Streamlit Cloud**:
- **Repository**: `prasant2030/App_Devopment`
- **Branch**: `main`
- **Main file**: `movie-recommender/app.py`

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Developer

**Prasant** - [GitHub](https://github.com/prasant2030)