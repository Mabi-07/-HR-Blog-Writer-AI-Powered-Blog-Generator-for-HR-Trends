from hr_blog_writer.config import HUGGINGFACE_API_KEY
import requests

def proofread_and_improve(text):
    prompt = f"""
You are a professional editor. Improve the grammar, clarity, and style of the following blog post. Do not change the structure drastically.

Blog Post:
{text}
    """

    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
        headers={"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"},
        json={"inputs": prompt}
    )

    result = response.json()
    return result[0]["generated_text"] if isinstance(result, list) and "generated_text" in result[0] else str(result)
