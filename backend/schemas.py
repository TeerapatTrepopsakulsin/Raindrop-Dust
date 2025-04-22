"""Schemas for the API response model."""
from datetime import datetime
from pydantic import BaseModel


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


class TimeStamp(BaseModel):
    timestamp: datetime


class EnvironmentalElements(BaseModel):
    coordinates: Coordinates
    temp: Temperature
    humidity: float
    light: float
    weather: WeatherCondition
    wind_spd: float
    cloud: float
    rain: float


class AQI(BaseModel):
    aqi: float


class PMAtmosphericShort(BaseModel):
    pm2_5: float
    pm10_0: float


class PMAtmospheric(BaseModel):
    pm1_0: float
    pm2_5: float
    pm10_0: float


class PMFactory(BaseModel):
    pm1_0: float
    pm2_5: float
    pm10_0: float


class PM(BaseModel):
    pm_atmospheric: PMAtmospheric
    pm_factory: PMFactory


class ParticlesCount(BaseModel):
    pcnt_0_3: float
    pcnt_0_5: float
    pcnt_1_0: float
    pcnt_2_5: float
    pcnt_5_0: float
    pcnt_10_0: float


class Particles(BaseModel):
    particles_count: ParticlesCount


class HourlyResponse(Particles, PM, AQI, EnvironmentalElements, TimeStamp):

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
                        "description": "Particulate Matter concentration μg/m3 (atmospheric environment)",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5",
                        "pm10_0": "PM 10"
                    },
                    "pm_factory": {
                        "description": "Particulate Matter concentration μg/m3 (factory environment)",
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


class PMResponse(PM, TimeStamp):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "timestamp": "Timestamp",
                    "pm_atmospheric": {
                        "description": "Particulate Matter concentration μg/m3 (atmospheric environment)",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5",
                        "pm10_0": "PM 10"
                    },
                    "pm_factory": {
                        "description": "Particulate Matter concentration μg/m3 (factory environment)",
                        "pm1_0": "PM 1.0",
                        "pm2_5": "PM 2.5",
                        "pm10_0": "PM 10"
                    }
                }
            ]
        }
    }


class AQIResponse(AQI, TimeStamp):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "timestamp": "Timestamp",
                    "aqi": "Air Quality Index"
                }
            ]
        }
    }


class ParticlesResponse(Particles, TimeStamp):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "timestamp": "Timestamp",
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


class SummaryResponse(BaseModel):
    start_time: TimeStamp
    end_time: TimeStamp
    average: HourlyResponse
    max: HourlyResponse
    min: HourlyResponse


class ForecastResponse(PMAtmosphericShort, AQI, TimeStamp):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "timestamp": "Timestamp",
                    "aqi": "AQI at the corresponding timestamp",
                    "pm2_5": "PM 2.5 concentration at the corresponding timestamp",
                    "pm10_0": "PM 10 concentration at the corresponding timestamp"
                }
            ]
        }
    }
