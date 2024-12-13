import requests
import json

API_KEY = "WLsY9BF8Kr6aeidh9a1H4iTll9fs8u96zeII00UO"
URL = "https://api.nasa.gov/DONKI/FLR"

def fetch_space_weather(start_date, end_date):
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "api_key": API_KEY
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        for event in data:
            print(f"Flare Class: {event['classType']}, Start Time: {event['beginTime']}")
    else:
        print("Error fetching data:", response.status_code)

if __name__ == "__main__":
    fetch_space_weather("2024-12-01", "2024-12-13")