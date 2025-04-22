"""/raw endpoints, raw data from the database."""
from fastapi import APIRouter, Depends
from .. import crud
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/raw",
    tags=["raw"],
    responses={
        404: {"description": "Not found"}
    }
)


@router.get("/primary")
async def get_primary(limit: int = 1, sort: int = 0, db: Session = Depends(get_db)):
    data = crud.get_raw_primary(db, limit=limit, sort=sort)
    return data


@router.get("/secondary")
async def get_secondary(limit: int = 1, sort: int = 0, db: Session = Depends(get_db)):
    data = crud.get_raw_secondary(db, limit=limit, sort=sort)
    return data


@router.get("/hourly")
async def get_hourly(limit: int = 1, sort: int = 0, db: Session = Depends(get_db)):
    data = crud.get_raw_hourly(db, limit=limit, sort=sort)
    return data
