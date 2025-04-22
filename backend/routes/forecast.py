"""/forecast endpoints, predictive data."""
from fastapi import APIRouter, Depends
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from ..predictor import Predictor


router = APIRouter(
    prefix="/forecast",
    tags=["forecast"],
    responses={
        404: {"description": "Not found"}
    }
)


@router.get("/1day", response_model=list[schemas.ForecastResponse])
async def forecast_1day(limit: int = -1, db: Session = Depends(get_db)):
    forecast = Predictor.get_1day_prediction()
    forecast = forecast[:limit] if limit != -1 else forecast
    return forecast


@router.get("/3day", response_model=list[schemas.ForecastResponse])
async def forecast_3day(limit: int = -1, db: Session = Depends(get_db)):
    forecast = Predictor.get_3day_prediction()
    forecast = forecast[:limit] if limit != -1 else forecast
    return forecast
