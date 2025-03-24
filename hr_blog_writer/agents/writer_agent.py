import json
import requests
from hr_blog_writer.config import HUGGINGFACE_API_KEY

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

MAX_CHARS = 3000  # adjust this based on model limits

def truncate_text(text, max_len):
    return text if len(text) <= max_len else text[:max_len]

def generate_blog(outline, research_text):
    # Truncate inputs to avoid API input size limits
    outline = truncate_text(outline, MAX_CHARS)
    research_text = truncate_text(research_text, MAX_CHARS)

    prompt = f"""You are an expert HR blog writer. Using the following outline and research, write a detailed blog post.

Outline:
{outline}

Research:
{research_text}

Write the blog post below:
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 1024,
            "return_full_text": False
        }
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    print("Writer Agent Response Status:", response.status_code)

    try:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif "generated_text" in result:
            return result["generated_text"]
        else:
            raise ValueError(f"Unexpected response format:\n{result}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to decode JSON: {e}\nRaw response:\n{response.text}")
