import tkinter as tk
import requests
import json

def get_location():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            city = data.get("city")
            return city
        else:
            return "City information not available"
    except Exception as e:
        return "Error: Failed to retrieve location information"

def get_weather(city):
    try:
        api_key = "YOUR_WEATHER_API_KEY"  # Insert your own WeatherAPI key here
        api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None

def display_weather(data, city):
    if data:
        location = data.get("location")
        if location:
            name = location.get("name")
            region = location.get("region")
            country = location.get("country")
            location_label.config(text=f"Location: {name}, {region}, {country}")

        current = data.get("current")
        if current:
            condition = current.get("condition")
            if condition:
                weather = condition.get("text")
                temp_c = current.get("temp_c")
                feels_like_c = current.get("feelslike_c")
                wind_kph = current.get("wind_kph")
                humidity = current.get("humidity")
                weather_label.config(text=f"Current weather in {city}: {weather}")
                temp_label.config(text=f"Temperature: {temp_c}°C (Feels like: {feels_like_c}°C)")
                wind_label.config(text=f"Wind Speed: {wind_kph} km/h")
                humidity_label.config(text=f"Humidity: {humidity}%")
    else:
        weather_label.config(text="Failed to retrieve weather information.")

def fetch_weather():
    city = get_location()
    if city:
        weather_data = get_weather(city)
        display_weather(weather_data, city)
    else:
        weather_label.config(text="Failed to retrieve location information.")

# GUI setup
root = tk.Tk()
root.title("Weather App")

location_label = tk.Label(root, text="")
location_label.pack(pady=5)

weather_label = tk.Label(root, text="")
weather_label.pack(pady=5)

temp_label = tk.Label(root, text="")
temp_label.pack(pady=5)

wind_label = tk.Label(root, text="")
wind_label.pack(pady=5)

humidity_label = tk.Label(root, text="")
humidity_label.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

root.mainloop()
