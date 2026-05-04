import pandas as pd

df = pd.read_csv("weather_data.csv")

df = df.drop(columns=[col for col in ["wind_kph", "wind_speed_kph", "rainfall"] if col in df.columns])

df.to_csv("weather_data.csv", index=False)