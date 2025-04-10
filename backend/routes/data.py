from fastapi import APIRouter, Depends
from .. import schemas, crud
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={
        404: {"description": "Not found"}
    }
)


@router.get("/latest", response_model=list[schemas.HourlyResponse], response_description="Get the latest collected data with the given limit.")
async def get_latest_data(limit:int=1, db: Session = Depends(get_db)):
    data = crud.get_hourly(db, limit=limit)
    return data


@router.get("/", response_model=list[schemas.HourlyResponse])
async def get_data(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data


@router.get("/pm", response_model=list[schemas.PMResponse])
async def get_pm(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data


@router.get("/aqi", response_model=list[schemas.AQIResponse])
async def get_aqi(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data


@router.get("/particle", response_model=list[schemas.ParticlesResponse])
async def get_particle(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    data = crud.get_hourly(db, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
    return data


@router.get("/summary") #TODO response_model
async def get_summary(db: Session = Depends(get_db)):
    pass


@router.get("/summary/custom") #TODO response_model
async def get_custom_summary(db: Session = Depends(get_db)):
    pass
