🌤️ Simple Weather App
---

A lightweight Python-based command-line weather application that retrieves real-time weather data using the OpenWeatherMap API.
Users can input a city name to view current weather conditions, including temperature (in Celsius or Fahrenheit) and a brief weather description.

✨ Features
----------

✅ City-Based Search – Fetch weather data by entering a city name

🌍 Real-Time Weather Data – Powered by the OpenWeatherMap API

🌡️ Temperature Units – Supports Celsius and Fahrenheit

⚠️ Error Handling – Gracefully handles:

Invalid city names

Network connectivity issues

Unexpected API responses

🧰 Prerequisites

Make sure you have the following installed:

Python 3.6 or higher

Active Internet Connection

OpenWeatherMap API Key

🚀 Installation
1️⃣ Clone the Repository
git clone https://github.com/Dhanush312/simple-weather-app.git
cd simple-weather-app

2️⃣ Set Up a Virtual Environment (Optional but Recommended)
Windows
python -m venv env
.\env\Scripts\activate

macOS / Linux
python3 -m venv env
source env/bin/activate

3️⃣ Install Dependencies
pip install requests python-dotenv

⚙️ Configuration
🔑 Get an API Key

Sign up at OpenWeatherMap to obtain a free API key.

📁 Create Environment File

Create a file named .env in the project root directory.

📝 Add Your API Key
API_KEY=your_api_key_here


🔒 Note: The application loads the API key securely using environment variables—no hardcoding required.

▶️ Usage

Run the application using:

python app.py


Follow the on-screen prompts to:

Enter the city name

Choose your preferred temperature unit (Celsius or Fahrenheit)

🤝 Contributing

Contributions are welcome! 🚀
To contribute to this project:

Fork the repository

Create a new feature branch:

git checkout -b feature-branch


Commit your changes:

git commit -am "Add new feature"


Push to your branch:

git push origin feature-branch


Open a Pull Request

📄 License

This project is licensed under the MIT License.
