import pandas as pd

FILE_PATH = "weather_data.csv"

def load_data():
    return pd.read_csv(FILE_PATH)

def save_data(df):
    df.to_csv(FILE_PATH, index=False)