from sqlalchemy.orm import Session

from models import Weather, KidBright, Hourly


def get_weather(db: Session, _id: int):
    return db.query(Weather).filter(Weather.id == _id).first()

def get_weathers(db: Session, skip:int=0, limit:int=100):
    return db.query(Weather).offset(skip).limit(limit).all()

def get_hourly(db: Session, skip:int=0, limit:int=100):
    return db.query(Hourly).order_by(Hourly.ts.desc()).offset(skip).limit(limit).all()

