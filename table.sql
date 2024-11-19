CREATE TABLE IF NOT EXISTS public.sensor_data
(
    "time" timestamp without time zone,
    "Date_time" timestamp without time zone,
    "Timestamp" bigint,
    aqi integer,
    ch2o real,
    co real,
    co2 integer,
    "devID" text COLLATE pg_catalog."default",
    light real,
    no real,
    no2 integer,
    o3 real,
    pm1 integer,
    pm10 integer,
    pm2p5 integer,
    pressure real,
    rain real,
    rain_d timestamp without time zone,
    rain_total real,
    rh real,
    so2 real,
    sound real,
    temperature real,
    "timestamp" bigint,
    ts bigint,
    uva real,
    uvb real,
    voc real
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sensor_data
    OWNER to postgres;