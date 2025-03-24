import requests
from serpapi import GoogleSearch
from bs4 import BeautifulSoup
from hr_blog_writer.config import SERPAPI_API_KEY
from hr_blog_writer.config import HUGGINGFACE_API_KEY

def get_trending_topic():
    prompt = "Suggest one trending topic in the Human Resources (HR) field for a 2000-word blog post."

    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
        headers={"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"},
        json={"inputs": prompt}
    )

    result = response.json()
    return result[0]["generated_text"].strip() if isinstance(result, list) and "generated_text" in result[0] else str(result)


def get_trending_hr_topics():
    params = {
        "engine": "google_trends",
        "q": "HR trends",
        "api_key": SERPAPI_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("related_queries", [])

def gather_information(topic, num_articles=5):
    query = f"{topic} site:hr.com OR site:shrm.org"
    params = {
        "engine": "google",
        "q": query,
        "num": num_articles,
        "api_key": SERPAPI_API_KEY
    }
    search = GoogleSearch(params)
    links = [res["link"] for res in search.get_dict().get("organic_results", [])]
    
    content_list = []
    for url in links:
        try:
            html = requests.get(url, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text() for p in paragraphs])
            content_list.append(text)
        except:
            continue
    return content_list
