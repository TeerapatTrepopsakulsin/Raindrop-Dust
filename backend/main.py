from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import SessionLocal, engine
from .utils import db_groupby_hourly
from . import models
from .routes import data, forecast, raw


models.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    await db_groupby_hourly(db)

    yield

    engine.dispose()


app = FastAPI(
    title="Raindrop Dust",
    description="FastAPI application providing PM and dust particles data "
                "along with environmental elements and weather conditions.",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(data.router)
app.include_router(forecast.router)
app.include_router(raw.router)


@app.get("/")
async def root():
    return {"message": "Raindrop Dust API!"}
