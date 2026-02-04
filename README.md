# Simple Weather App (Python)

The Simple Weather App is a Python-based command-line application that fetches real-time weather data using the OpenWeatherMap API. It allows users to enter the name of a city and displays the current weather conditions, including temperature (in Celsius or Fahrenheit) and a brief weather description.

---

## Features

- **User Input**: Allows users to enter the city name for which they want to check the weather.
- **API Integration**: Uses the OpenWeatherMap API to fetch real-time weather data.
- **Temperature Conversion**: Converts temperature to Celsius or Fahrenheit based on user preference.
- **Error Handling**: Handles API connectivity issues, invalid inputs, and unexpected data formats gracefully.

---

## Prerequisites

To run this application, you will need:

- Python 3.6 or higher
- `requests` library installed in your Python environment

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Dhanush312/simple-weather-app.git
cd simple-weather-app
2. Set Up a Virtual Environment (Optional but recommended)
For Windows:

python -m venv env
.\env\Scripts\activate
For macOS and Linux:

python3 -m venv env
source env/bin/activate
3. Install Dependencies
pip install requests
API Key Setup
Sign up at OpenWeatherMap to obtain an API key.

Create a file named .env in the root directory.

Add your API key to the file:

API_KEY=your_api_key_here
Update app.py to read the API key securely.

Usage
Run the application using:

python app.py
Follow the on-screen prompts to:

Enter the city name

Choose the temperature unit (Celsius or Fahrenheit)

Contributing
Contributions are welcome! To contribute:

Fork the repository

Create a new branch

git checkout -b feature-branch
Make your changes

Commit your changes

git commit -am "Add some feature"
Push to the branch

git push origin feature-branch
Create a Pull Request

License
This project is licensed under the MIT License.
