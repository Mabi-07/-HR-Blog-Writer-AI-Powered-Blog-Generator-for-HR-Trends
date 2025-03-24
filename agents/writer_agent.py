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
        "parameters": {"max_new_tokens": 1200, "temperature": 0.7},
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()[0]["generated_text"]

def generate_blog(outline, context_text):
    prompt = f"""
Using the outline below, generate a high-quality, SEO-optimized HR blog post.

Outline:
{outline}

Context:
{context_text}

Write in a clear, professional tone. Add examples where relevant.
"""
    output = query_model(prompt)
    return output.split(prompt)[-1].strip()