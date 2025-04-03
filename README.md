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
### Accessing the app
- use the credntials set by you in .env file to login

## Output Images
- Without Country name
<img width="480" alt="Screenshot 2025-04-03 at 10 49 23 AM" src="https://github.com/user-attachments/assets/0c4de169-8a7f-4290-a5ed-91f3e4487eb8" />

- With country names
<img width="480" alt="Screenshot 2025-04-03 at 10 49 17 AM" src="https://github.com/user-attachments/assets/dac79f3a-b2a0-47ae-ae37-47d20f70a90a" />

- WIth No matching Lyrics found
<img width="480" alt="Screenshot 2025-04-03 at 11 00 34 AM" src="https://github.com/user-attachments/assets/09fdaa61-d188-4e1f-a00b-0a4225d1ee2f" />

- Login Page
<img width="551" alt="Screenshot 2025-04-03 at 11 28 32 AM" src="https://github.com/user-attachments/assets/98382d9c-af86-4988-833e-07d366457fb2" />



