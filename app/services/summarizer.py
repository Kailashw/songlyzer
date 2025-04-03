import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_lyrics(lyrics: str) -> str:
    try:
        prompt = f"Summarize the following song lyrics in one sentence:\n\n{lyrics}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "Unable to generate summary."
