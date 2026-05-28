import httpx

from datetime import date, timedelta

BABALDU_LATITUDE = 12.2667
BABALDU_LONGITUDE = 9.5167

OPEN_METEO_ARCHIVE_URL = (
    "https://archive-api.open-meteo.com/v1/archive"
)

async def fetch_historical_weather(
    days: int = 30
):

    end_date = date.today()

    start_date = (
        end_date - timedelta(days=days)
    )

    params = {

        "latitude": BABALDU_LATITUDE,

        "longitude": BABALDU_LONGITUDE,

        "start_date": start_date.isoformat(),

        "end_date": end_date.isoformat(),

        "daily": (
            "temperature_2m_max,"
            "temperature_2m_min,"
            "temperature_2m_mean,"
            "precipitation_sum,"
            "wind_speed_10m_max,"
            "relative_humidity_2m_mean,"
            "surface_pressure_mean,"
            "cloud_cover_mean"
        ),

        "timezone": "auto"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            OPEN_METEO_ARCHIVE_URL,
            params=params,
            timeout=60.0
        )

        response.raise_for_status()

        data = response.json()

        return data