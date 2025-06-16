import requests
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
load_dotenv()
api_key= os.environ.get("api_key")
Base_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get().strip() #Get city for input
    if not ciy:
        messagebox.showwarning("Input Error!","Enter the Correct city.")

    url = f"{Base_URL}?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["Cod"] == 200:
            city_name = data[name]
            temperature= data["main"]["temp"]
            description= data["weather"][0]["description"]
            humidity= data["main"]["humidity"]
            wind_speed= data["wind"]["speed"]

            result_text = (
                f"📍 City: {city_name}\n"
                f"🌡️ Temperature: {temperature}°C\n"
                f"🌥️ Condition: {description}\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌬️ Wind Speed: {wind_speed} m/s"
            )
            # Color based on temperature
            if temperature >= 30:
                temp_color = "red"
            elif temperature >= 20:
                temp_color = "orange"
            elif temperature >= 10:
                temp_color = "blue"
            else:
                temp_color = "purple"
            #Background colour
            if "rain" in description.lower():
                bg_color = "lightblue"
            elif "cloud" in description.lower():
                bg_color = "lightgrey"
            elif "clear" in description.lower():
                bg_color = "lightyellow"
            else:
                bg_color = "white"

            result_label.config(text = result_text,
                fg = temp_color,
                bg = bg_color,
                font = ("courier","11","bold")
            )





