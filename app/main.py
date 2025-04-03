from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from app.services.lyrics import get_lyrics_from_musixmatch
from app.services.summarizer import summarize_lyrics
from app.services.country import extract_countries
from app.services.cache import get_cached_song, cache_song

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "error": None})

@app.post("/submit", response_class=HTMLResponse)
def form_post(request: Request, artist: str = Form(...), title: str = Form(...)):
    cache_key = f"{artist.lower()}_{title.lower()}"
    cached = get_cached_song(cache_key)
    if cached:
        return templates.TemplateResponse("result.html", {"request": request, **cached})

    lyrics = get_lyrics_from_musixmatch(artist, title)
    print("lyrics:", lyrics)
    if not lyrics:
        return templates.TemplateResponse("form.html", {"request": request, "error": "Lyrics not found."})

    summary = summarize_lyrics(lyrics)
    print("summary:", summary)
    countries = extract_countries(lyrics)
    print("countries:", countries)
    result = {"artist": artist, "title": title, "summary": summary, "countries": countries, "lyrics": lyrics}

    cache_song(cache_key, result)
    return templates.TemplateResponse("result.html", {"request": request, **result})

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
