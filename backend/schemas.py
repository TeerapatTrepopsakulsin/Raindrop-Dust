from datetime import datetime
from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    lon: float
    lat: float

class Hourly(BaseModel):
    timestamp: datetime
    coordinates: Coordinates
    temp: float
    temp_max: float
    temp_min: float
    hum: float
    weather_main: str
    weather_con: str
    wind_spd: float
    cloud: float
    rain: float
    light: float
    aqi: float
    pm1_0: float
    pm2_5: float
    pm10_0: float
    pm1_0_atm: float
    pm2_5_atm: float
    pm10_0_atm: float
    pcnt_0_3: float
    pcnt_0_5: float
    pcnt_1_0: float
    pcnt_2_5: float
    pcnt_5_0: float
    pcnt_10_0: float


    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #             }
    #         ]
    #     }
    # }

