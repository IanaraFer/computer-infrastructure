# Weather information.
# Import requests, schedule and time
import requests
import schedule
import time
from datetime import datetime
# Downlow weather web pag.
    
    
def fetch_weather_data():
    url = 'https://prodapi.metweb.ie/observations/athenry/today'
    response = requests.get(url)
    if response.ok:
        data = response.json()  # Assuming the response is in JSON format
        if isinstance(data, list):
            data = data[0]  # Extract the first item if it's a list
        weather_info = {
            "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "temperature": data.get('temperature'),
            "condition": data.get('condition'),
            # Add other relevant fields from the JSON response
        }
        # You can replace this with code to save the data file or database
        print(weather_info)
    else:
        print("Failed to retrieve the weather data")