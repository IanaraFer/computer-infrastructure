name: Weather Update

on:
  schedule:
    # Runs every day at 10 AM GMT
    - cron: '0 10 * * *'
  workflow_dispatch: # Add this line to enable manual triggering

jobs:
  weather:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests schedule

    - name: Verify dependencies
      run: |
        pip show requests
        pip show schedule

    - name: Run weather data script
      run: python weather-data.py