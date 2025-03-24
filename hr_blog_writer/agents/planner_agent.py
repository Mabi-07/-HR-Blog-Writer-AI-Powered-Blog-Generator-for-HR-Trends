# agents/planner_agent.py
import requests
from hr_blog_writer.config import SERPAPI_API_KEY
from hr_blog_writer.config import HUGGINGFACE_API_KEY

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {
   "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",

    "Content-Type": "application/json"
}

def generate_outline(topic):
    prompt = f"Create a detailed outline for a 2000-word blog post on the following HR topic:\n\n{topic}"

    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
        headers={"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"},
        json={"inputs": prompt}
    )

    result = response.json()
    return result[0]["generated_text"].strip() if isinstance(result, list) and "generated_text" in result[0] else str(result)
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
    return output.split(prompt)[-1].strip()  # Get only the response part
