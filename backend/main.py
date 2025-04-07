from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database import get_db, SessionLocal, engine

from sqlalchemy.orm import Session

import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    engine.dispose()

app = FastAPI(lifespan=lifespan)

class DataModel(BaseModel):
    id: int
    value: float

@app.get("/data")
async def get_data(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    weathers = crud.get_weathers(db, skip=skip, limit=limit)
    return weathers

@app.post("/forecast")
async def forecast(data: DataModel):
    # TODO: Implement forecasting logic
    return {"forecast": "result"}
