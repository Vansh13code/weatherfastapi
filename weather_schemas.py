 
from pydantic import BaseModel
from typing import Optional

class WeatherSchema(BaseModel):
    date: Optional[str] = None
    city: str
    temperature_c: float
    humidity: float
    wind_speed_kmph: float
    rainfall_mm: float