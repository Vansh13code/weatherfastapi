from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from services.data_services import load_data
import matplotlib.pyplot as plt
import io
import pandas as pd
router = APIRouter()


def generate_plot():
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()
    return StreamingResponse(img, media_type="image/png")


@router.get("/temperature-trend")
def temperature_trend():
    df = load_data()

    if "date" not in df.columns or "temperature_c" not in df.columns:
        raise HTTPException(status_code=400, detail="Required columns missing")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df = df.sort_values("date")
    
    plt.figure()
    plt.scatter(df["date"], df["temperature_c"])
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trend")

    return generate_plot()


@router.get("/rainfall")
def rainfall_comparison():
    df = load_data()

    if "city" not in df.columns or "rainfall_mm" not in df.columns:
        raise HTTPException(status_code=400, detail="Required columns missing")

    rainfall = df.groupby("city")["rainfall_mm"].sum()

    plt.figure()
    rainfall.plot(kind="bar")
    plt.title("Rainfall by City")

    return generate_plot()


@router.get("/humidity")
def humidity_distribution():
    df = load_data()

    if "humidity" not in df.columns:
        raise HTTPException(status_code=400, detail="Humidity column missing")

    plt.figure()
    plt.hist(df["humidity"], bins=20)
    plt.title("Humidity Distribution")

    return generate_plot()