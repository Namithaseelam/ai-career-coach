import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

def call_ollama(prompt: str):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return {'error': response.text}
    
    return response.json()


def generate_resume(data):

    prompt = f"""
    Generate a professional resume.

    Name: {data.name}
    Skills: {', '.join(data.skills)}
    Experience: {data.experience}

    Format it properly with sections.
    """

    result = call_ollama(prompt)

    if "error" in result: 
        return result
    
    return result['response']


def get_career_suggestions(skills):

    prompt = f"""
    Suggest 5 career paths for someone with these skills:
    {', '.join(skills)}

    Give short explanations.
    """

    result = call_ollama(prompt)

    if "error" in result:
        return result
    
    return result["response"]