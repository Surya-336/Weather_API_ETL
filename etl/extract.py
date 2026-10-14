import json
import os
import requests
from dotenv import load_dotenv
from logs.log import extract_log

load_dotenv()
url = os.getenv("Base_url")
api_key = os.getenv("API_KEY")

def get_request(city,country="IN"):
    
    if not api_key:
        raise RuntimeError("Set API_KEY in your environment or .env file")
    
    extract_log.info("Extracting Started")
    response = requests.get(
        url,
        params={
            "q": f"{city},{country}",
            "limit": 1,
            "appid": api_key,
            "units":"metric"
        },

        timeout=10
    )
    if not response.ok:
        raise RuntimeError(f"OpenWeatherMap request failed: HTTP {response.status_code}")
    forecast = response.json()

    
    
    with open("Data.json", "w", encoding="utf-8") as output:
        json.dump(forecast, output, indent=2, ensure_ascii=False)
    extract_log.info("Extracted Details Saved in json format")
    return forecast