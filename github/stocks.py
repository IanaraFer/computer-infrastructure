#! /usr/bin/env python

# Financial data.
import yfinance as yf

# Dates and times.
import datetime as dt

# Get data for microsoft, apple and google
tickers = ['MSFT', 'AAPL', 'GOOG']
df = yf.download(tickers, period="1d", interval="1m")

# Get the current date and time
filename = dt.datetime.now()
# Create a string from the current data and time
filename = filename.strftime("%Y%m%d_%H%M%S")
# Prepend data folders, append ile extension.
filename = filename + ".csv"

# Save the data to a CSV file.
df['Close'].to_csv(filename)
