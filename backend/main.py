from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from database import get_db, SessionLocal, engine
from sqlalchemy.orm import Session
from utils import schematise_hourly_response, db_groupby_hourly
import crud, models, schemas


models.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    await db_groupby_hourly(db)

    yield

    engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/data/latest", response_model=list[schemas.Hourly])
async def get_latest_data(limit:int=1, db: Session = Depends(get_db)):
    data = crud.get_hourly(db, limit=limit)
    data = schematise_hourly_response(data)
    return data


@app.get("/data")
async def get_data(skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    weathers = crud.get_hourly(db, skip=skip, limit=limit)
    return weathers


@app.post("/forecast")
async def forecast():
    # TODO: Implement forecasting logic
    return {"forecast": "result"}
