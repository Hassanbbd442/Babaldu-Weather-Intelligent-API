from fastapi import APIRouter

from app.services.weather_service import (
    fetch_current_weather
)

from app.schemas.weather_schema import (
    CurrentWeatherResponse
)

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)

@router.get(
    "/current",
    response_model=CurrentWeatherResponse
)
async def get_current_weather():

    weather = await fetch_current_weather()

    return weather