import requests
import os

def get_lyrics_from_musixmatch(artist: str, title: str) -> str:
    api_key = os.getenv("MUSIXMATCH_API_KEY")
    endpoint = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get"
    params = {"q_artist": artist, "q_track": title, "apikey": api_key}

    try:
        res = requests.get(endpoint, params=params)
        data = res.json()
        lyrics = data["message"]["body"].get("lyrics", {}).get("lyrics_body", "")
        return lyrics.strip() if lyrics else None
    except Exception:
        return None
