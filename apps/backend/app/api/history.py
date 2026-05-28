from fastapi import APIRouter

from app.services.historical_weather_service import (
    fetch_historical_weather
)

router = APIRouter(
    prefix="/history",
    tags=["Historical Weather"]
)

@router.get("/{days}")
async def get_historical_weather(days: int):

    data = await fetch_historical_weather(days)

    return data