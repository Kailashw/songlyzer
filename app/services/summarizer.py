import openai
import os
from groq import Groq

openai.api_key = os.getenv("OPENAI_API_KEY")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_lyrics(lyrics: str) -> str:
    try:
        prompt = f"Summarize the following song lyrics in one sentence:\n\n{lyrics}"
        # use another way to fetch summary
        response = openai.responses.create(
            model="gpt-4o-mini",
            instructions="You are a song lyrics summarizer assistant.",
            input=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # try generating summary from groq
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_completion_tokens=1024,
                top_p=1,
                stop=None,
                stream=False,
            )

            return response.choices[0].message.content.strip()
        except Exception as e:
            # Handle the error gracefully
            print(f"Error generating summary: {e}")
            return "Unable to generate summary."
