# In-memory cache
song_cache = {}

def get_cached_song(key: str):
    print(f"Fetching song from cache: {key}")
    return song_cache.get(key)

def cache_song(key: str, data: dict):
    song_cache[key] = data
