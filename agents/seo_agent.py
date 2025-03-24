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

def optimize_for_seo(content, target_keywords):
    keywords = ", ".join(target_keywords)
    prompt = f"""
Improve the following blog content to be more SEO-friendly.

Content:
{content}

Target Keywords: {keywords}

Make sure the keywords are naturally integrated and the formatting (headings, structure) is optimized for search engines.
"""
    output = query_model(prompt)
    return output.split(prompt)[-1].strip()