from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class Weather(Base):
    __tablename__ = "openweather"

    id = Column(Integer, primary_key=True, index=True)
    ts = Column(DateTime, index=True)
    lat = Column(Float)
    lon = Column(Float)
    temp = Column(Float)
    hum = Column(Integer)
    weather_main = Column(String(255))
    weather_con = Column(String(255))
    wind_spd = Column(Float)
    cloud = Column(Float)
    rain = Column(Float)

    def __repr__(self):
        return f"<WeatherData(id={self.id}, ts={self.ts})>"


class KidBright(Base):
    __tablename__ = "raindropdust"

    id = Column(Integer, primary_key=True, index=True)
    ts = Column(DateTime, index=True)
    temp = Column(Float)
    light = Column(Float)
    hum = Column(Integer)
    aqi = Column(Float, nullable=True)
    pm1_0 = Column(Float)
    pm2_5 = Column(Float)
    pm10_0 = Column(Float)
    pm1_0_atm = Column(Float)
    pm2_5_atm = Column(Float)
    pm10_0_atm = Column(Float)
    pcnt_0_3 = Column(Integer)
    pcnt_0_5 = Column(Integer)
    pcnt_1_0 = Column(Integer)
    pcnt_2_5 = Column(Integer)
    pcnt_5_0 = Column(Integer)
    pcnt_10_0 = Column(Integer)

    def __repr__(self):
        return f"<KidBright(id={self.id}, ts={self.ts})>"


class Hourly(Base):
    __tablename__ = "hourly"
    id = Column(Integer, primary_key=True, index=True)
    ts = Column(DateTime, index=True)
    lat = Column(Float)
    lon = Column(Float)
    temp = Column(Float)
    temp_max = Column(Float)
    temp_min = Column(Float)
    hum = Column(Float)
    weather_main = Column(String(255))
    weather_con = Column(String(255))
    wind_spd = Column(Float)
    cloud = Column(Float)
    rain = Column(Float)
    light = Column(Float)
    aqi = Column(Float, nullable=True)
    pm1_0 = Column(Float)
    pm2_5 = Column(Float)
    pm10_0 = Column(Float)
    pm1_0_atm = Column(Float)
    pm2_5_atm = Column(Float)
    pm10_0_atm = Column(Float)
    pcnt_0_3 = Column(Float)
    pcnt_0_5 = Column(Float)
    pcnt_1_0 = Column(Float)
    pcnt_2_5 = Column(Float)
    pcnt_5_0 = Column(Float)
    pcnt_10_0 = Column(Float)

    def __repr__(self):
        return f"<Hourly(id={self.id}, ts={self.ts})>"
