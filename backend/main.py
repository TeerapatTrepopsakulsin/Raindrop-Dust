from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from database import get_db, SessionLocal, engine
from sqlalchemy.orm import Session
from utils import schematise_hourly_response, db_groupby_hourly
import crud, models, schemas
from datetime import datetime


models.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    await db_groupby_hourly(db)

    yield

    engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/data/latest", response_model=list[schemas.HourlyResponse], response_description="Get the latest collected data with the given limit.")
async def get_latest_data(limit:int=1, db: Session = Depends(get_db)):
    data = crud.get_hourly(db, limit=limit)
    return data


@app.get("/data", response_model=list[schemas.HourlyResponse])
async def get_data(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data

@app.get("/data/pm", response_model=list[schemas.PMResponse])
async def get_pm(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data

@app.get("/data/aqi", response_model=list[schemas.AQIResponse])
async def get_aqi(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data


@app.get("/data/particle", response_model=list[schemas.ParticlesResponse])
async def get_particle(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data

@app.get("/data/summary") #TODO response_model
async def get_summary(db: Session = Depends(get_db)):
    pass


@app.get("/data/summary/custom") #TODO response_model
async def get_custom_summary(db: Session = Depends(get_db)):
    pass


@app.post("/forecast")
async def forecast():
    # TODO: Implement forecasting logic
    return {"forecast": "result"}
