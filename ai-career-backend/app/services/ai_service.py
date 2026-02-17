import os
import requests
from dotenv import load_dotenv

load_dotenv()

AI_API_URL = os.getenv('AI_API_URL')
AI_API_KEY = os.getenv("AI_API_KEY")


def generate_resume(data):
    payload = {
        "name": data.name,
        "skills": data.skills,
        "experience": data.experience
    }

    response = requests.post(
        AI_API_URL,
        headers={
             "Authorization": f"Bearer {AI_API_KEY}",
            "Content-Type": "application/json"
        }, 
        json=payload
        )
    
    return response.json()

def get_career_suggestions(skills):
    payload = {"skills": skills}

    response = requests.post(
        AI_API_URL,
        headers={
             "Authorization": f"Bearer {AI_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    return response.json()
