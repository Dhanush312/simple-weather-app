import requests

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32


# ---------- User Input ----------
city = input("Enter city name: ").strip()

# If user enters empty city, stop the program
if not city:
    print("Please enter a valid city name.")
    exit()  # Exit the program completely

unit_input = input("Enter unit (c for Celsius, f for Fahrenheit): ").strip().lower()

# Validate temperature unit input
if unit_input not in ("c", "f"):
    print("Invalid unit. Please enter 'c' or 'f'.")
    exit()


# ---------- API Configuration ----------
api_key = ""  # TODO: Add your OpenWeather API key here
units = "metric"  # Always request temperature in Celsius from API

# Base URL for OpenWeather current weather API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"


# ---------- API Request ----------
try:
    response = requests.get(url, timeout=10)  # timeout avoids hanging forever
except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")
    exit()


# ---------- Response Handling ----------
if response.status_code == 200:
    data = response.json()
    try:
        # Extract temperature and weather description
        temperature_celsius = data["main"]["temp"]
        description = data["weather"][0]["description"]

        # Convert temperature if user selected Fahrenheit
        if unit_input == "f":
            temperature = celsius_to_fahrenheit(temperature_celsius)
            unit_symbol = "°F"
        else:
            temperature = temperature_celsius
            unit_symbol = "°C"

        print(
            f"The temperature in {city} is {temperature:.2f} {unit_symbol} "
            f"and the weather is described as {description}."
        )

    except KeyError:
        # Happens if API response structure changes
        print("Error: Unexpected response format from the API.")

elif response.status_code == 404:
    # City name does not exist in OpenWeather database
    print("City not found. Please check the city name and try again.")

else:
    # Any other error like 401 (invalid API key), 500, etc.
    print("Failed to retrieve data.")
    print("Please check the city name, API key, or try again later.")
