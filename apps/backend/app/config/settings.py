from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROJECT_NAME = os.getenv(
        "PROJECT_NAME",
        "Babaldu Weather Intelligence API"
    )

    API_VERSION = os.getenv(
        "API_VERSION",
        "1.0.0"
    )

settings = Settings()