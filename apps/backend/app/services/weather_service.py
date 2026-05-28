import httpx

BABALDU_LATITUDE = 11.3533
BABALDU_LONGITUDE = 9.5971

OPEN_METEO_URL = (
    "https://api.open-meteo.com/v1/forecast"
)

async def fetch_current_weather():

    params = {
        "latitude": BABALDU_LATITUDE,
        "longitude": BABALDU_LONGITUDE,

        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "surface_pressure,"
            "wind_speed_10m,"
            "precipitation,"
            "cloud_cover,"
            "weather_code"
        )
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            OPEN_METEO_URL,
            params=params,
            timeout=30.0
        )

        response.raise_for_status()

        data = response.json()

        current = data.get("current", {})

        return {
            "location": "Babaldu",

            "latitude": BABALDU_LATITUDE,
            "longitude": BABALDU_LONGITUDE,

            "temperature": current.get(
                "temperature_2m", 0
            ),

            "humidity": current.get(
                "relative_humidity_2m", 0
            ),

            "pressure": current.get(
                "surface_pressure", 0
            ),

            "wind_speed": current.get(
                "wind_speed_10m", 0
            ),

            "rainfall": current.get(
                "precipitation", 0
            ),

            "cloud_cover": current.get(
                "cloud_cover", 0
            ),

            "weather_code": current.get(
                "weather_code", 0
            ),

            "timestamp": current.get(
                "time", ""
            )
        }