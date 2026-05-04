from fastapi import APIRouter
from services.data_services import load_data

router = APIRouter()

@router.get("/analysis/avg-temp")
def avg_temp():
    df = load_data()
    result = df.groupby("city")["temperature_c"].mean()
    
    
    return {city: float(temp) for city, temp in result.items()}


@router.get("/analysis/temperaturemaxmin")
def temperature_max_min():
    df = load_data()
    
    return {
        "max": float(df["temperature_c"].max()),
        "min": float(df["temperature_c"].min())
    }
@router.get("/analysis/rainfall")
def rainfall():
    df = load_data()
    
    return {
        "total_rainfall": float(df["rainfall"].sum())
    }
@router.get("/analysis/humidity")
def humidity():
    df = load_data()
    
    return {
        "max": float(df["humidity"].max()),
        "min": float(df["humidity"].min())
    }

@router.get("/analysis/moving_averages_and_stats_summary")
def moving_averages_and_stats_summary():
    df = load_data()
    
    df["temp7davg"] = df["temperature_c"].rolling(window=7).mean()
    
    summary = {
        "temperature": {
            "mean": float(df["temperature_c"].mean()),
            "median": float(df["temperature_c"].median()),
            "std_dev": float(df["temperature_c"].std())
        },
        "humidity": {
            "mean": float(df["humidity"].mean()),
            "median": float(df["humidity"].median()),
            "std_dev": float(df["humidity"].std())
        },
        "rainfall": {
            "total": float(df["rainfall"].sum())
        }
    }
    
    return {
        "moving_averages": df[["city", "temp7davg"]].to_dict(orient="records"),
        "summary_statistics": summary
    }