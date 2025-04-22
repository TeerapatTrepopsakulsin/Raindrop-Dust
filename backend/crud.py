from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from .models import Weather, KidBright, Hourly
from .schemas import TimeStamp
from .utils import schematise_hourly_response
from datetime import datetime, timedelta


def get_raw_primary(db: Session, limit: int = -1, sort: int = 0):
    query = db.query(KidBright)
    try:
        query = query.order_by(KidBright.ts.desc()) if sort == 1 else query
        query = query.limit(limit) if limit != -1 else query
    except:
        raise HTTPException(status_code=400, detail="Invalid params")
    return query.all()


def get_raw_secondary(db: Session, limit: int = -1, sort: int = 0):
    query = db.query(Weather)
    try:
        query = query.order_by(Weather.ts.desc()) if sort == 1 else query
        query = query.limit(limit) if limit != -1 else query
    except:
        raise HTTPException(status_code=400, detail="Invalid params")
    return query.all()


def get_raw_hourly(db: Session, limit: int = -1, sort: int = 0):
    query = db.query(Hourly)
    try:
        query = query.order_by(Hourly.ts.desc()) if sort == 1 else query
        query = query.limit(limit) if limit != -1 else query
    except:
        raise HTTPException(status_code=400, detail="Invalid params")
    return query.all()


def get_hourly(db: Session, start_date=None, end_date=None, skip: int = 0, limit: int = 1):
    query = db.query(Hourly)
    try:
        query = query.filter(Hourly.ts >= start_date) if start_date else query
        query = query.filter(Hourly.ts < end_date) if end_date else query
        query = query.order_by(Hourly.ts.desc())
        query = query.offset(skip)
        query = query.limit(limit) if limit != -1 else query
        hourly = query.all()
        hourly = schematise_hourly_response(hourly)
    except:
        raise HTTPException(status_code=400, detail="Invalid params")
    return hourly


def get_summary(db: Session, start_date=None, end_date=None, period=None, date=None, sum_type=None):
    end_time = None

    if sum_type == 0:
        if date is None:
            date = db.query(Hourly.ts).order_by(Hourly.ts.desc()).first()[0]
        else:
            try:
                date = datetime.fromisoformat(date)
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid date")

        if period == "weekly":
            end_time = date + timedelta(weeks=1)
        else:
            end_time = date + timedelta(days=1)
    elif sum_type == 1:
        try:
            if start_date is not None:
                date = datetime.fromisoformat(start_date)
            if end_date is not None:
                end_time = datetime.fromisoformat(end_date)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date")

    if not date:
        date = db.query(Hourly.ts).order_by(Hourly.ts.asc()).first()[0]
    if not end_time:
        end_time = db.query(Hourly.ts).order_by(Hourly.ts.desc()).first()[0]

    query = db.query(Hourly).filter(Hourly.ts >= date, Hourly.ts < end_time)

    if not query.all():
        return []

    mean_query = query.with_entities(
        func.round(func.avg(Hourly.temp), 4).label("temp"),
        func.round(func.avg(Hourly.temp_max), 4).label("temp_max"),
        func.round(func.avg(Hourly.temp_min), 4).label("temp_min"),
        func.round(func.avg(Hourly.hum), 4).label("hum"),
        func.round(func.avg(Hourly.light), 4).label("light"),
        func.round(func.avg(Hourly.wind_spd), 4).label("wind_spd"),
        func.round(func.avg(Hourly.cloud), 4).label("cloud"),
        func.round(func.sum(Hourly.rain), 4).label("rain"),
        func.round(func.avg(Hourly.aqi), 4).label("aqi"),
        func.round(func.avg(Hourly.pm1_0_atm), 4).label("pm1_0_atm"),
        func.round(func.avg(Hourly.pm2_5_atm), 4).label("pm2_5_atm"),
        func.round(func.avg(Hourly.pm10_0_atm), 4).label("pm10_0_atm"),
        func.round(func.avg(Hourly.pm1_0), 4).label("pm1_0"),
        func.round(func.avg(Hourly.pm2_5), 4).label("pm2_5"),
        func.round(func.avg(Hourly.pm10_0), 4).label("pm10_0"),
        func.round(func.avg(Hourly.pcnt_0_3), 4).label("pcnt_0_3"),
        func.round(func.avg(Hourly.pcnt_0_5), 4).label("pcnt_0_5"),
        func.round(func.avg(Hourly.pcnt_1_0), 4).label("pcnt_1_0"),
        func.round(func.avg(Hourly.pcnt_2_5), 4).label("pcnt_2_5"),
        func.round(func.avg(Hourly.pcnt_5_0), 4).label("pcnt_5_0"),
        func.round(func.avg(Hourly.pcnt_10_0), 4).label("pcnt_10_0")
    )

    max_query = query.with_entities(
        func.round(func.max(Hourly.temp), 4).label("temp"),
        func.round(func.max(Hourly.temp_max), 4).label("temp_max"),
        func.round(func.max(Hourly.temp_min), 4).label("temp_min"),
        func.round(func.max(Hourly.hum), 4).label("hum"),
        func.round(func.max(Hourly.light), 4).label("light"),
        func.round(func.max(Hourly.wind_spd), 4).label("wind_spd"),
        func.round(func.max(Hourly.cloud), 4).label("cloud"),
        func.round(func.max(Hourly.rain), 4).label("rain"),
        func.round(func.max(Hourly.aqi), 4).label("aqi"),
        func.round(func.max(Hourly.pm1_0_atm), 4).label("pm1_0_atm"),
        func.round(func.max(Hourly.pm2_5_atm), 4).label("pm2_5_atm"),
        func.round(func.max(Hourly.pm10_0_atm), 4).label("pm10_0_atm"),
        func.round(func.max(Hourly.pm1_0), 4).label("pm1_0"),
        func.round(func.max(Hourly.pm2_5), 4).label("pm2_5"),
        func.round(func.max(Hourly.pm10_0), 4).label("pm10_0"),
        func.round(func.max(Hourly.pcnt_0_3), 4).label("pcnt_0_3"),
        func.round(func.max(Hourly.pcnt_0_5), 4).label("pcnt_0_5"),
        func.round(func.max(Hourly.pcnt_1_0), 4).label("pcnt_1_0"),
        func.round(func.max(Hourly.pcnt_2_5), 4).label("pcnt_2_5"),
        func.round(func.max(Hourly.pcnt_5_0), 4).label("pcnt_5_0"),
        func.round(func.max(Hourly.pcnt_10_0), 4).label("pcnt_10_0")
    )

    min_query = query.with_entities(
        func.round(func.min(Hourly.temp), 4).label("temp"),
        func.round(func.min(Hourly.temp_max), 4).label("temp_max"),
        func.round(func.min(Hourly.temp_min), 4).label("temp_min"),
        func.round(func.min(Hourly.hum), 4).label("hum"),
        func.round(func.min(Hourly.light), 4).label("light"),
        func.round(func.min(Hourly.wind_spd), 4).label("wind_spd"),
        func.round(func.min(Hourly.cloud), 4).label("cloud"),
        func.round(func.min(Hourly.rain), 4).label("rain"),
        func.round(func.min(Hourly.aqi), 4).label("aqi"),
        func.round(func.min(Hourly.pm1_0_atm), 4).label("pm1_0_atm"),
        func.round(func.min(Hourly.pm2_5_atm), 4).label("pm2_5_atm"),
        func.round(func.min(Hourly.pm10_0_atm), 4).label("pm10_0_atm"),
        func.round(func.min(Hourly.pm1_0), 4).label("pm1_0"),
        func.round(func.min(Hourly.pm2_5), 4).label("pm2_5"),
        func.round(func.min(Hourly.pm10_0), 4).label("pm10_0"),
        func.round(func.min(Hourly.pcnt_0_3), 4).label("pcnt_0_3"),
        func.round(func.min(Hourly.pcnt_0_5), 4).label("pcnt_0_5"),
        func.round(func.min(Hourly.pcnt_1_0), 4).label("pcnt_1_0"),
        func.round(func.min(Hourly.pcnt_2_5), 4).label("pcnt_2_5"),
        func.round(func.min(Hourly.pcnt_5_0), 4).label("pcnt_5_0"),
        func.round(func.min(Hourly.pcnt_10_0), 4).label("pcnt_10_0")
    )

    mean_result = mean_query.first()
    max_result = max_query.first()
    min_result = min_query.first()

    class DummyHourly:
        def __init__(self, **kwargs):
            self.id = None
            self.ts = date
            self.lat = 0
            self.lon = 0
            self.weather_main = ""
            self.weather_con = ""
            for k, v in kwargs.items():
                setattr(self, k, v)

    mean_record = [DummyHourly(**mean_result._asdict())]
    max_record = [DummyHourly(**max_result._asdict())]
    min_record = [DummyHourly(**min_result._asdict())]

    l_ave = schematise_hourly_response(mean_record)
    l_max = schematise_hourly_response(max_record)
    l_min = schematise_hourly_response(min_record)

    return [
        {
            "start_time": TimeStamp(timestamp=date),
            "end_time": TimeStamp(timestamp=end_time),
            "average": l_ave[0],
            "max": l_max[0],
            "min": l_min[0]
        }
    ]
