"""Helper functions."""
from sqlalchemy import text


def schematise_hourly_response(list_of_hourly):
    """Schematise the hourly object into the desired format."""
    schematised_data = [
        {
            **h.__dict__,
            "timestamp": h.ts,
            "coordinates": {
                "lat": h.lat,
                "lon": h.lon
            },
            "temp": {
                "average": h.temp,
                "max": h.temp_max,
                "min": h.temp_min
            },
            "humidity": h.hum,
            "weather": {
                "main_condition": h.weather_main,
                "description": h.weather_con,
            },
            "pm_atmospheric": {
                "pm1_0": h.pm1_0_atm,
                "pm2_5": h.pm2_5_atm,
                "pm10_0": h.pm10_0_atm
            },
            "pm_factory": {
                "pm1_0": h.pm1_0,
                "pm2_5": h.pm2_5,
                "pm10_0": h.pm10_0
            },
            "particles_count": {
                "pcnt_0_3": h.pcnt_0_3,
                "pcnt_0_5": h.pcnt_0_5,
                "pcnt_1_0": h.pcnt_1_0,
                "pcnt_2_5": h.pcnt_2_5,
                "pcnt_5_0": h.pcnt_5_0,
                "pcnt_10_0": h.pcnt_10_0
            }
        }
        for h in list_of_hourly
    ]
    return schematised_data


DELETE_1 = """
    DELETE FROM hourly
    ORDER BY ts DESC
    LIMIT 1;
"""

GROUP_HOURLY_SQL_STATEMENT = """
    INSERT INTO hourly (ts, lat, lon, temp, temp_max, temp_min, hum,
                        weather_main, weather_con, wind_spd, cloud,
                        rain, light, aqi, pm1_0, pm2_5, pm10_0,
                        pm1_0_atm, pm2_5_atm, pm10_0_atm, pcnt_0_3,
                        pcnt_0_5, pcnt_1_0, pcnt_2_5, pcnt_5_0, pcnt_10_0)
        WITH openweather_hourly AS (
            SELECT
                DATE_ADD(
                    '2025-01-01 00:00:00',
                    INTERVAL FLOOR(
                        TIMESTAMPDIFF(
                            HOUR,
                            '2025-01-01 00:00:00',
                            ts
                        )
                    ) * 1 HOUR
                ) AS ts_start,
                AVG(lat) AS lat,
                AVG(lon) AS lon,
                AVG(temp) AS temp,
                AVG(hum) AS hum,
                COALESCE(MAX(weather_main), 'Unknown') AS weather_main,
                COALESCE(MAX(weather_con), 'Unknown') AS weather_con,
                AVG(wind_spd) AS wind_spd,
                AVG(cloud) AS cloud,
                AVG(rain) AS rain
            FROM openweather
            GROUP BY ts_start
        ),
        raindropdust_hourly AS (
            SELECT
                DATE_ADD(
                    '2025-01-01 00:00:00',
                    INTERVAL FLOOR(
                        TIMESTAMPDIFF(
                            HOUR,
                            '2025-01-01 00:00:00',
                            ts
                        )
                    ) * 1 HOUR
                ) AS ts_start,
                AVG(temp) AS temp,
                MAX(temp) AS temp_max,
                MIN(temp) AS temp_min,
                AVG(light) AS light,
                AVG(hum) AS hum,
                AVG(aqi) AS aqi,
                AVG(pm1_0) AS pm1_0,
                AVG(pm2_5) AS pm2_5,
                AVG(pm10_0) AS pm10_0,
                AVG(pm1_0_atm) AS pm1_0_atm,
                AVG(pm2_5_atm) AS pm2_5_atm,
                AVG(pm10_0_atm) AS pm10_0_atm,
                AVG(pcnt_0_3) AS pcnt_0_3,
                AVG(pcnt_0_5) AS pcnt_0_5,
                AVG(pcnt_1_0) AS pcnt_1_0,
                AVG(pcnt_2_5) AS pcnt_2_5,
                AVG(pcnt_5_0) AS pcnt_5_0,
                AVG(pcnt_10_0) AS pcnt_10_0
            FROM raindropdust
            GROUP BY ts_start
        )
        SELECT
            COALESCE(o.ts_start, r.ts_start) AS ts,
            o.lat,
            o.lon,
            r.temp AS temp,
            r.temp_max,
            r.temp_min,
            r.hum AS hum,
            o.weather_main,
            o.weather_con,
            o.wind_spd,
            o.cloud,
            o.rain,
            r.light,
            r.aqi,
            r.pm1_0,
            r.pm2_5,
            r.pm10_0,
            r.pm1_0_atm,
            r.pm2_5_atm,
            r.pm10_0_atm,
            r.pcnt_0_3,
            r.pcnt_0_5,
            r.pcnt_1_0,
            r.pcnt_2_5,
            r.pcnt_5_0,
            r.pcnt_10_0
        FROM openweather_hourly o
        INNER JOIN raindropdust_hourly r ON o.ts_start = r.ts_start
        WHERE o.ts_start > (SELECT MAX(ts) FROM hourly)
"""


async def db_groupby_hourly(db):
    """Hourly table processing."""
    try:
        db.execute(text(DELETE_1))
        db.commit()
        db.execute(text(GROUP_HOURLY_SQL_STATEMENT))
        db.commit()
    finally:
        db.close()
