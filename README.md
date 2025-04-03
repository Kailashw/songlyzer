# songlyzer

A web app to summarize lyrics and detect mentioned countries from a song using either artist + title.

## Features

- Search for song lyrics using **Musixmatch**
- Summarize lyrics using **OpenAI GPT**
- Extract mentioned countries using **pycountry**
- **In-memory caching** to avoid duplicate API calls
- **Jinja2 UI** with HTML templates
- Fully **Dockerized**

## Requirements

- OpenAI API Key
- Musixmatch API Key
- Docker

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourname/songlyzer.git
cd songlyzer
```

### 2. enter the required values in .env file
```bash
cp .env.example .env
# replace values in .env
```

### 3. running commands
```bash
docker build -t songlyzer .
docker run -p 8000:8000 --env-file .env songlyzer
```
