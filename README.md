Simple Weather App
The Simple Weather App is a Python-based command-line application that fetches real-time weather data using the OpenWeatherMap API. Users can enter a city name to view current weather conditions, including temperature (in Celsius or Fahrenheit) and a brief description.

Features
User Input: Accepts city names to query weather data.

API Integration: Fetches real-time data via the OpenWeatherMap API.

Temperature Conversion: Automatically converts temperature to Celsius or Fahrenheit based on user preference.

Error Handling: Gracefully handles connectivity issues, invalid city names, and unexpected data formats.

Prerequisites
To run this application, you will need:

Python 3.6 or higher

An active internet connection

An API Key from OpenWeatherMap

Installation
1. Clone the Repository
Bash
git clone https://github.com/Dhanush312/simple-weather-app.git
cd simple-weather-app
2. Set Up a Virtual Environment (Optional but Recommended)
For Windows:

Bash
python -m venv env
.\env\Scripts\activate
For macOS and Linux:

Bash
python3 -m venv env
source env/bin/activate
3. Install Dependencies
Install the required libraries, including requests for API calls and python-dotenv for security.

Bash
pip install requests python-dotenv
Configuration
Get an API Key: Sign up at OpenWeatherMap to obtain a free API key.

Create Environment File: Create a file named .env in the root directory of the project.

Add Your Key: Open the .env file and add the following line:

Plaintext
API_KEY=your_api_key_here
(Note: The application is configured to load this key securely so you don't have to hardcode it in the script.)

Usage
Run the application using the following command:

Bash
python app.py
Follow the on-screen prompts to:

Enter the city name.

Choose your preferred temperature unit.

Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

Fork the repository.

Create a new branch for your feature:

Bash
git checkout -b feature-branch
Make your changes and commit them:

Bash
git commit -am "Add some feature"
Push to the branch:

Bash
git push origin feature-branch
Create a Pull Request.

License
This project is licensed under the MIT License.
