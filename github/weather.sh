#!/bin/bash

# Define the directory to save weather data
WEATHER_DIR="data/weather"

# Create the directory if it doesn't exist
mkdir -p $WEATHER_DIR

# Fetch the weather data (replace with your actual command to get weather data)
WEATHER_DATA=$(curl -s "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Dublin")

# Save the weather data to a file with the current date and time as the filename
echo $WEATHER_DATA > $WEATHER_DIR/$(date +%Y%m%d_%H%M%S).json
