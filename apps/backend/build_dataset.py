import asyncio

from app.ml.data_pipeline import (
    build_weather_dataset
)

async def main():

    df = await build_weather_dataset(
        days=365
    )

    print("\nDataset Generated Successfully\n")

    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

if __name__ == "__main__":
    asyncio.run(main())