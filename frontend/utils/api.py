import os
import requests
from dotenv import load_dotenv


# Load env
load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def get_api_res(path: str):
    # Get data from backend endpoints
    response = requests.get(f"{BASE_URL}{path}")
    return response
