SELECT 
    TO_CHAR(TO_TIMESTAMP(MIN(timestamp) / 1000), 'DD-MM-YYYY') AS min_date,
    TO_CHAR(TO_TIMESTAMP(MAX(timestamp) / 1000), 'DD-MM-YYYY') AS max_date 
FROM 
    sensor_data;
