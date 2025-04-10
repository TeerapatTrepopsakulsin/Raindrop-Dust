from datetime import datetime
from pydantic import BaseModel, Field


class Coordinates(BaseModel):
    lat: float
    lon: float


class Temperature(BaseModel):
    average: float
    max: float
    min: float


class WeatherCondition(BaseModel):
    main_condition: str
    description: str


class PMFactory(BaseModel):
    pm1_0: float
    pm2_5: float
    pm10_0: float

class PMAtmospheric(BaseModel):
    pm1_0: float
    pm2_5: float
    pm10_0: float

class ParticlesCount(BaseModel):
    pcnt_0_3: float
    pcnt_0_5: float
    pcnt_1_0: float
    pcnt_2_5: float
    pcnt_5_0: float
    pcnt_10_0: float


class Hourly(BaseModel):
    timestamp: datetime
    coordinates: Coordinates
    temp: Temperature
    humidity: float
    light: float
    weather: WeatherCondition
    wind_spd: float
    cloud: float
    rain: float
    aqi: float
    pm_atmospheric: PMAtmospheric
    pm_factory: PMFactory
    particles_count: ParticlesCount

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "timestamp": "Timestamp",
                    "coordinates": {
                        "lon": "Longitude",
                        "lat": "Latitude",
                    },
                    "temp": {
                        "average": "Average temperature within the hour interval",
                        "max": "Maximum temperature within the hour interval",
                        "min": "Minimum temperature within the hour interval"
                    },
                    "humidity": "Humidity, %",
                    "light": "Light level, Lux",
                    "weather": {
                        "main_condition": "Vague weather condition",
                        "description": "Descriptive weather condition",
                    },
                    "wind_spd": "Wind speed, m/s",
                    "cloud": "Cloud, %",
                    "rain": "Total Rainfall, mm",
                    "aqi": "Air Quality Index",
                    "pm_atmospheric": {
                        "description": "Particulate Matter concentration μ g/m3 (atmospheric environment)",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5",
                        "pm10_0": "PM 10"
                    },
                    "pm_factory": {
                        "description": "Particulate Matter concentration μ g/m3 (factory environment)",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5",
                        "pm10_0": "PM 10"
                    },
                    "particles_count": {
                        "description": "Particle count in 0.1 liter or air",
                        "pcnt_0_3": "Diameter beyond 0.3 um",
                        "pcnt_0_5": "Diameter beyond 0.5 um",
                        "pcnt_1_0": "Diameter beyond 1 um",
                        "pcnt_2_5": "Diameter beyond 2.5 um",
                        "pcnt_5_0": "Diameter beyond 5 um",
                        "pcnt_10_0": "Diameter beyond 10 um"
                    }
                }
            ]
        }
    }
