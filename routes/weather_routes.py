from fastapi import APIRouter
from services.api_services import append_weather, fetch_weather
from services.data_services import load_data, save_data
import pandas as pd
from weather_schemas import WeatherSchema

router = APIRouter()

@router.get("/weather")
def get_all():
    df = load_data()
    wrong_cols = ["wind_kph", "wind_speed_kph", "rainfall"]
    df = df.drop(columns=[col for col in wrong_cols if col in df.columns])

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    df = df.astype(object).where(pd.notnull(df), None)
    return df.to_dict(orient="records")

@router.post("/weather")
def add(record: WeatherSchema):
    df = load_data()
    new_row = record.dict()

    import pandas as pd
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    save_data(df)

    return {"msg": "Added", "data": new_row}

@router.put("/weather/{index}")
def update(index: int, record: WeatherSchema):
    df = load_data()

    df.loc[index] = record.dict()

    save_data(df)

    return {"msg": "Updated", "data": record.dict()}

@router.delete("/weather/{index}")
def delete(index: int):
    df = load_data()
    df = df.drop(index)
    save_data(df)
    return {"msg": "Deleted"}


@router.post("/weather/fetch/{city}")
def fetch_and_store(city: str):
    return append_weather(city)