"""Get the data from backend."""
import os
import requests
from dotenv import load_dotenv


# Load env
load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def get_api_res(path: str):
    if path == "/data/latest?limit=1":
        pass
    elif path == "/raw/primary?limit=-1":
        pass
    elif path == "/raw/secondary?limit=-1":
        pass
    elif path == "/raw/hourly?limit=-1":
        pass
    elif path == "/forecast/1day":
        pass
    elif path == "/forecast/3day":
        pass
    else:
        raise Exception(f"Invalid path: {path}")

    # Get data from backend endpoints
    response = requests.get(f"{BASE_URL}{path}")
    return response
