import pandas as pd

from app.services.historical_weather_service import (
    fetch_historical_weather
)

OUTPUT_PATH = (
    "../../models/datasets/babaldu_weather.csv"
)

async def build_weather_dataset(days: int = 365):

    data = await fetch_historical_weather(days)

    daily = data["daily"]

    df = pd.DataFrame({

        "date": daily["time"],

        "temp_max": daily["temperature_2m_max"],

        "temp_min": daily["temperature_2m_min"],

        "temp_mean": daily["temperature_2m_mean"],

        "rainfall": daily["precipitation_sum"],

        "wind_speed": daily["wind_speed_10m_max"],

        "humidity": daily["relative_humidity_2m_mean"],

        "pressure": daily["surface_pressure_mean"],

        "cloud_cover": daily["cloud_cover_mean"]
    })

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Sort chronologically
    df = df.sort_values("date")

    # =========================
    # FEATURE ENGINEERING
    # =========================

    # Previous day temperature
    df["temp_mean_lag1"] = (
        df["temp_mean"].shift(1)
    )

    # Previous day rainfall
    df["rainfall_lag1"] = (
        df["rainfall"].shift(1)
    )

    # Rolling averages
    df["temp_rolling_3"] = (
        df["temp_mean"]
        .rolling(window=3)
        .mean()
    )

    df["rainfall_rolling_3"] = (
        df["rainfall"]
        .rolling(window=3)
        .mean()
    )

    # =========================
    # FORECAST TARGETS
    # =========================

    # Tomorrow temperature
    df["target_temp_t1"] = (
        df["temp_mean"].shift(-1)
    )

    # Tomorrow rainfall
    df["target_rainfall_t1"] = (
        df["rainfall"].shift(-1)
    )

    # Rain tomorrow? classification
    df["target_rain_event_t1"] = (
        df["target_rainfall_t1"] > 0
    ).astype(int)

    # Drop null rows
    df = df.dropna()

    # Save dataset
    df.to_csv(
        OUTPUT_PATH,
        index=False
    )

    return df