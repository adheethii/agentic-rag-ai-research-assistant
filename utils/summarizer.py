from transformers import pipeline

summarizer = pipeline("summarization")

def summarize(text):

    summary = summarizer(text, max_length=120, min_length=40)

    return summary[0]["summary_text"]