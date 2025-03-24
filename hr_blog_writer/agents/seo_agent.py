import json
import requests
from hr_blog_writer.config import HUGGINGFACE_API_KEY

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

MAX_INPUT_CHARS = 3000

def truncate(text, max_len):
    return text if len(text) <= max_len else text[:max_len]

def optimize_for_seo(content):
    prompt = f"""You are an SEO expert. Improve the following blog post to maximize its SEO performance by adding relevant keywords, improving headings, and making the content more engaging.

Blog Content:
{truncate(content, MAX_INPUT_CHARS)}

Optimized Blog:
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

    print("SEO Agent Response Status:", response.status_code)

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
