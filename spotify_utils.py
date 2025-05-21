# This file will give functions to interact with the Spotify API.
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

def get_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
    )
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_tracks_by_emotion(emotion):
    mood_playlist_keywords = {
        'happy': 'feel good',
        'sad': 'sad songs',
        'angry': 'rage workout',
        'neutral': 'chill vibes',
        'calm': 'relaxing music',
        'fear': 'calm piano',
        'disgust': 'power songs',
        'surprise': 'upbeat mix'
    }

    keyword = mood_playlist_keywords.get(emotion.lower(), 'mood booster')

    sp = get_spotify_client()
    results = sp.search(q=keyword, type='track', limit=5)

    tracks = []
    for item in results['tracks']['items']:
        track = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'url': item['external_urls']['spotify']
        }
        tracks.append(track)
    return tracks
