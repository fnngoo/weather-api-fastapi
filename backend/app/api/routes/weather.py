import random

from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter(tags=["weather"])

WEATHERS = ["晴", "多云", "阴", "小雨", "中雨", "大雨", "雷阵雨", "雪", "雾"]


class WeatherResponse(BaseModel):
    city: str
    weather: str
    temperature: int


@router.get("/get_weather", response_model=WeatherResponse)
def get_waether(city: str = Query(..., description="城市名")) -> WeatherResponse:
    """Return a random weather condition for the given city."""
    return WeatherResponse(
        city=city,
        weather=random.choice(WEATHERS),
        temperature=random.randint(-10, 40),
    )
