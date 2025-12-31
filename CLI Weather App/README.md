CLI WEATHER APP

A command-line weather application built in Python that fetches
real-time weather data using the OpenWeatherMap API.

  --------------------------------------------------
  FEATURES
  --------------------------------------------------
  - Fetches live weather data by city name -
  Supports metric (°C) and imperial (°F) units -
  Command-line interface using argparse - Uses
  context managers for API session handling -
  Graceful error handling - Clean, beginner-friendly
  Python structure

  --------------------------------------------------

REQUIREMENTS

-   Python 3.8+
-   requests library
-   OpenWeatherMap API key

  --------------------------------------------------
  INSTALLATION
  --------------------------------------------------
  1. Install dependencies: pip install requests

  2. Save the file as: weather_cli.py
  --------------------------------------------------

USAGE

Basic usage: python weather_cli.py Nairobi –api-key YOUR_API_KEY

With units: python weather_cli.py London –units imperial –api-key
YOUR_API_KEY

  --------------------------------------------------
  EXAMPLE OUTPUT
  --------------------------------------------------
  Weather Information

  --------------------------------------------------

City: Nairobi Temperature: 24°C Condition: Clear Sky Humidity: 60%

  --------------------------------------------------
  CORE PYTHON CONCEPTS USED
  --------------------------------------------------
  - argparse (command-line arguments) - requests &
  HTTP APIs - Context managers (enter / exit) -
  Exception handling - Modular function design

  --------------------------------------------------

LEARNING CONTEXT

This project is aligned with Corey Schafer’s Intermediate Python
tutorials (Week 11): - argparse - requests - context managers -
testing-ready structure

  --------------------------------------------------
  EXTENSIONS (OPTIONAL)
  --------------------------------------------------
  - Add SQLite caching - Add logging - Add 5-day
  forecast - Add multithreading for multiple
  cities - Package as pip-installable CLI tool

  --------------------------------------------------

AUTHOR

Edwin Koech
