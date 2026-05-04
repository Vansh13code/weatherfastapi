from fastapi import APIRouter
from services.api_services import append_weather, fetch_weather
from services.data_services import load_data, save_data

router = APIRouter()

@router.get("/weather")
def get_all():
    df = load_data()
    return df.to_dict(orient="records")

@router.post("/weather")
def add(record: dict):
    df = load_data()
    df = df.append(record, ignore_index=True)
    save_data(df)
    return {"msg": "Added"}

@router.put("/weather/{index}")
def update(index: int, record: dict):
    df = load_data()
    df.loc[index] = record
    save_data(df)
    return {"msg": "Updated"}

@router.delete("/weather/{index}")
def delete(index: int):
    df = load_data()
    df = df.drop(index)
    save_data(df)
    return {"msg": "Deleted"}

@router.get("/external/{city}")
def external(city: str):
    return fetch_weather(city)

@router.post("/weather/fetch/{city}")
def fetch_and_store(city: str):
    return append_weather(city)