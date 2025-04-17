from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", truncation=True) 
with open("transcription.txt", "r") as f:
    transcribed_text = f.read()
result = sentiment_pipeline(transcribed_text)
print(f"Sentiment: {result[0]['label']}, Score: {result[0]['score']}")