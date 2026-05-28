from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.history import router as history_router

from app.config.settings import settings
from app.api.weather import router as weather_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(weather_router)
app.include_router(history_router)

@app.get("/")
async def root():

    return {
        "message": (
            "Babaldu Weather Intelligence API Running"
        )
    }