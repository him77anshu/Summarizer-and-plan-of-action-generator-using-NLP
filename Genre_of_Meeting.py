import openai
import os
from dotenv import load_dotenv


load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Prefine Genre class 
genres = ["Business", "Technical", "Team Meeting", "Brainstorming", "Planning", "Casual", "Classroom Meeting"]

def detect_genre(transcript):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that classifies meeting transcripts into genres."},
            {"role": "user", "content": f"Classify the following text into one of these genres: {', '.join(genres)}.\n\nText: {transcript}"}
        ]
    )
    genre = response.choices[0].message.content
    return genre.strip()


with open("transcription.txt", "r") as f:
       transcript = f.read()

print(detect_genre(transcript))