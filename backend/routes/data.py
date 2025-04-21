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


@router.get("", response_model=list[schemas.HourlyResponse])
async def get_data(start_date: str | None = None, end_date: str | None = None, skip:int=0, limit:int=1, db:Session=Depends(get_db)):
    """ Return records response of the data, sorting from the latest record.

    :param start_date: yyyy-MM-dd, indicate the beginning of the period/interval (Inclusive)
    :param end_date: yyyy-MM-dd, indicate the ending of the period/interval (Exclusive)
    :param skip: number of records to skip
    :param limit: number of records to return
    :param db: Session
    """
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


@router.get("/summary", response_model=schemas.SummaryResponse, response_model_exclude_none=True)
async def get_summary(period: str | None = None, date: str | None = None, db: Session = Depends(get_db)):
    """ Return a descriptive summary response of the data.

    :param period: weekly or daily, indicate the summary period/interval
    :param date: yyyy-MM-dd, the date that will be included in the summary response
    :param db: Session
    """
    data = crud.get_summary(db, period=period, date=date, sum_type=0)
    return data


@router.get("/summary/custom", response_model=schemas.SummaryResponse, response_model_exclude_none=True)
async def get_custom_summary(start_date: str | None = None, end_date: str | None = None, db: Session = Depends(get_db)):
    """ Return a descriptive summary response of the data.

    :param start_date: yyyy-MM-dd, indicate the beginning of the summary period/interval (Inclusive)
    :param end_date: yyyy-MM-dd, indicate the ending of the summary period/interval (Exclusive)
    :param db: Session
    """
    data = crud.get_summary(db, start_date=start_date, end_date=end_date, sum_type=1)
    return data
