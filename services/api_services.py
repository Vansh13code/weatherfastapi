import requests
import pandas as pd
from services.data_services import load_data, save_data

def fetch_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key=2f3a130b1da5436f92771934260405&q={city}"
    return requests.get(url).json()

def append_weather(city: str):
    data = fetch_weather(city)

    normalized_data = {
        "city": data["location"]["name"],
        "temperature_c": float(data["current"]["temp_c"]),
        "humidity": float(data["current"]["humidity"]),
        "wind_speed_kmph": float(data["current"]["wind_kph"]),
        "rainfall_mm": float(data["current"]["precip_mm"])
    }

    df = load_data()

    new_row = pd.DataFrame([normalized_data])
    df = pd.concat([df, new_row], ignore_index=True)

    save_data(df)

    return {"msg": "Weather added successfully", "data": normalized_data}