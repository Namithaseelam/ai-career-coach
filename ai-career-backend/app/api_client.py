import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")

print("Load Base URL:", API_BASE_URL)
class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    
    def get_data(self, endpoint: str, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"GET {url} failed: {response.status_code}, {response.text}")
        
    
    def post_data(self, endpoint: str, data: dict):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code in (200, 201):
            return response.json()
        else: 
            raise Exception(f"POST {url} failed: {response.status_code}, {response.text}")