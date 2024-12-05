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
        weather_info = {
            "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "temperature": data.get('temperature'),
            "condition": data.get('condition'),
            # Add other relevant fields from the JSON response
        }
        print(weather_info)  # You can replace this with code to save the data file or database
    else:
        print("Failed to retrieve the weather data")

# Schedule the task at 10 AM everyday
schedule.every().day.at("10:00").do(fetch_weather_data)

print("Scheduler started. Waiting for the job to run at 10:00 AM every day.")
while True:
    schedule.run_pending()
    time.sleep(60)
