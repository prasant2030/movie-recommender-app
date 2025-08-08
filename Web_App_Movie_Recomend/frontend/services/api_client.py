"""
API Client for communicating with the Movie Recommendation backend
"""

import requests
import streamlit as st
from typing import List, Dict, Optional
from config.settings import API_BASE_URL, ERROR_MESSAGES


class APIClient:
    """Client for communicating with the Movie Recommendation API"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Optional[Dict]:
        """Make HTTP request to the API"""
        try:
            url = f"{self.base_url}{endpoint}"
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            st.error(ERROR_MESSAGES["api_unavailable"])
            return None
        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {str(e)}")
            return None
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
            return None
    
    def get_health(self) -> bool:
        """Check if the API is healthy"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_genres(self) -> List[str]:
        """Get available genres from the API"""
        result = self._make_request('GET', '/api/movies/genres')
        if result and 'genres' in result:
            return result['genres']
        return []
    
    def get_all_movies(self) -> List[Dict]:
        """Get all movies from the API"""
        result = self._make_request('GET', '/api/movies')
        if result:
            return result
        return []
    
    def get_movies_by_genre(self, genre: str) -> List[Dict]:
        """Get movies by specific genre"""
        result = self._make_request('GET', f'/api/movies?genre={genre}')
        if result:
            return result
        return []
    
    def get_recommendations(self, genres: List[str], count: int = 5) -> List[Dict]:
        """Get movie recommendations based on selected genres"""
        payload = {
            'genres': genres,
            'count': count
        }
        result = self._make_request('POST', '/api/recommendations', json=payload)
        if result and 'movies' in result:
            return result['movies']
        return []
    
    def get_movie_by_id(self, movie_id: int) -> Optional[Dict]:
        """Get a specific movie by ID"""
        result = self._make_request('GET', f'/api/movies/{movie_id}')
        return result
    
    def get_movies_count(self) -> int:
        """Get total number of movies"""
        result = self._make_request('GET', '/api/movies/count/total')
        if result and 'total_movies' in result:
            return result['total_movies']
        return 0 