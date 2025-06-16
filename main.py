import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.environ.get("api_key")
BASE_URL = f"http://api.openweathermap.org/data/2.5/weather"
while True:
    city=input("Enter the City/state Name (or exist): ").strip()
    if city.lower() == "exit":
        print("Goodbaye! Stay Safe Out There.")
        break
    
    if not city:
        print("Please Enter the Valid City.")
        continue

    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    try: 
        response= requests.get(url)
        data = response.json()
    

        if data["cod"] == 200:
            city_name= data["name"]
            temperature= data["main"]["temp"]
            description= data["weather"][0]["description"]
            humidity= data["main"]["humidity"]
            wind_speed= data["wind"]["speed"]

            print(f"Weather in city {city_name}")
            print(f"🌡️ temperature: {temperature}°C")
            print(f"🌥️ condition: {description}")
            print(f"💧 Humidity: {humidity}")
            print(f"🌬️ Wind Speed: {wind_speed} m/s")    

        else:
            print("❌ City not found! Please enter a valid city name.")  
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
