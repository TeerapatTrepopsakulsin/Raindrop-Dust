from sqlalchemy.orm import Session

from models import Weather, KidBright, Hourly

from utils import schematise_hourly_response


def get_weather(db: Session, _id: int):
    return db.query(Weather).filter(Weather.id == _id).first()

def get_weathers(db: Session, skip:int=0, limit:int=100):
    return db.query(Weather).offset(skip).limit(limit).all()

def get_hourly(db: Session, start_date=None, end_date=None, skip:int=0, limit:int=100):
    query = db.query(Hourly)
    query = query.filter(Hourly.ts >= start_date) if start_date else query
    query = query.filter(Hourly.ts <= end_date) if end_date else query
    query = query.order_by(Hourly.ts.desc())
    query = query.offset(skip)
    query = query.limit(limit) if limit != -1 else query
    hourly = query.all()
    hourly = schematise_hourly_response(hourly)
    return hourly
