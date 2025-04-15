import os
import requests
import pandas as pd
from dotenv import load_dotenv


# Load env
load_dotenv()
BASE_URL = os.getenv("BASE_URL")

# Get data from backend
response = requests.get(f"{BASE_URL}/data?limit=-1")
data = response.json()

df = pd.DataFrame(data)
