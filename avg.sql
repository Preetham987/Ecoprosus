WITH HourlyAverage AS (
    SELECT
        date_trunc('hour', "time") AS hour_start,
        AVG(aqi) AS avg_aqi,
        AVG(ch2o) AS avg_ch2o,
        AVG(co) AS avg_co,
        AVG(co2) AS avg_co2,
        AVG(light) AS avg_light,
        AVG(no) AS avg_no,
        AVG(no2) AS avg_no2,
        AVG(o3) AS avg_o3,
        AVG(pm1) AS avg_pm1,
        AVG(pm10) AS avg_pm10,
        AVG(pm2p5) AS avg_pm2p5,
        AVG(pressure) AS avg_pressure,
        AVG(rain) AS avg_rain,
        AVG(EXTRACT(EPOCH FROM rain_d)) AS avg_rain_d,
        AVG(rain_total) AS avg_rain_total,
        AVG(rh) AS avg_rh,
        AVG(so2) AS avg_so2,
        AVG(sound) AS avg_sound,
        AVG(temperature) AS avg_temperature,
        AVG(ts) AS avg_ts,
        AVG(uva) AS avg_uva,
        AVG(uvb) AS avg_uvb,
        AVG(voc) AS avg_voc
    FROM sensor_data
    GROUP BY hour_start
)

SELECT
    ha.hour_start,
    ha.avg_aqi,
    ha.avg_ch2o,
    ha.avg_co,
    ha.avg_co2,
    ha.avg_light,
    ha.avg_no,
    ha.avg_no2,
    ha.avg_o3,
    ha.avg_pm1,
    ha.avg_pm10,
    ha.avg_pm2p5,
    ha.avg_pressure,
    ha.avg_rain,
    to_timestamp(ha.avg_rain_d) AS avg_rain_d,
    ha.avg_rain_total,
    ha.avg_rh,
    ha.avg_so2,
    ha.avg_sound,
    ha.avg_temperature,
    ha.avg_ts,
    ha.avg_uva,
    ha.avg_uvb,
    ha.avg_voc
FROM HourlyAverage ha
ORDER BY ha.hour_start DESC;
