from sqlalchemy.orm import Session

from models import Weather
import schemas


def get_weather(db: Session, _id: int):
    return db.query(Weather).filter(Weather.id == _id).first()

def get_weathers(db: Session, skip:int=0, limit:int=100):
    return db.query(Weather).offset(skip).limit(limit).all()
