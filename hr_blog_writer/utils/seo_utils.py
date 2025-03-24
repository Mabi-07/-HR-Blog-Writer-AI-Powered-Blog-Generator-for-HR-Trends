import random

def find_keywords(topic):
    # Simulate fetching keywords for simplicity
    return [topic.lower(), "HR strategy", "employee engagement", "talent management"]

def insert_keywords(content, keywords):
    for keyword in keywords:
        content = content.replace("HR", f"HR and {keyword}", 1)
    return content
