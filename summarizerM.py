import os
from transformers import pipeline


def summarize_text(text, chunk_size=1000):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = [summarizer(chunk, max_length=200, min_length=50, do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)




