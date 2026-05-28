from pydantic import BaseModel

class CurrentWeatherResponse(BaseModel):
    location: str
    latitude: float
    longitude: float

    temperature: float
    humidity: float
    pressure: float
    wind_speed: float

    rainfall: float
    cloud_cover: float

    weather_code: int
    timestamp: str