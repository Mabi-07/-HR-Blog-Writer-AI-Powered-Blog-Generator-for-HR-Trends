import requests
from hr_blog_writer.config import HUGGINGFACE_API_KEY

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

def query_model(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 800, "temperature": 0.7},
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()[0]["generated_text"]

def create_outline(topic, context_text):
    prompt = f"""
You are a blog planner for HR content.

Generate a detailed SEO-optimized blog post outline for the topic:
"{topic}"

Use this context to help:
{context_text}

Include headings, subheadings, and a logical structure.
"""
    output = query_model(prompt)
    return output.split(prompt)[-1].strip()