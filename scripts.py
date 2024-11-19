import requests
import json
import psycopg2
from apscheduler.schedulers.background import BackgroundScheduler

url = "http://103.146.217.82:1028/last"
device_ids = [
    {"devId": "EMS003"},
    {"devId": "EMS005"},
    {"devId": "EMS0011"},
    {"devId": "EMS0012"},
    {"devId": "EMS0013"},
    {"devId": "EMS0014"},
    {"devId": "EMS0015"},
    {"devId": "EMS0016"},
    {"devId": "EMS0017"},
    {"devId": "EMS0018"}
]

db_params = {
    "host": "localhost",
    "database": "sensor_values",
    "user": "postgres",
    "password": "preetham28",
    "port": "5433"
}

def fetch_data_from_api():
    try:
        response = requests.get(url, params={"devIds": json.dumps(device_ids)})
        response.raise_for_status()
        data = response.json()
        
        filtered_data = [item for item in data if item.get("devID") in [d["devId"] for d in device_ids]]
        
        return filtered_data
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")


def insert_data_to_db(data_list):
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        for dev_data in data_list:
            dev_id = dev_data.get("devID", "")
            time = dev_data.get("time", "'1970-01-01 00:00:00'")
            date_time = dev_data.get("Date_time")
            Timestamp = dev_data.get("Timestamp", 0) or 0
            aqi = dev_data.get("aqi", 0) or 0
            ch2o = dev_data.get("ch2o", 0) or 0
            co = dev_data.get("co", 0) or 0
            co2 = dev_data.get("co2", 0) or 0
            light = dev_data.get("light", 0) or 0
            no = dev_data.get("no", 0) or 0
            no2 = dev_data.get("no2", 0) or 0
            o3 = dev_data.get("o3", 0) or 0
            pm1 = dev_data.get("pm1", 0) or 0
            pm10 = dev_data.get("pm10", 0) or 0
            pm2p5 = dev_data.get("pm2p5", 0) or 0
            pressure = dev_data.get("pressure", 0) or 0
            rain = dev_data.get("rain", 0) or 0
            rain_total = dev_data.get("rain_total", 0) or 0
            rain_d = dev_data.get("rain_d", "'1970-01-01 00:00:00'")
            rh = dev_data.get("rh", 0) or 0
            so2 = dev_data.get("so2", 0) or 0
            sound = dev_data.get("sound", 0) or 0
            temperature = dev_data.get("temperature", 0) or 0
            timestamp = dev_data.get("timestamp", 0) or 0  
            ts = dev_data.get("ts", 0) or 0
            uva = dev_data.get("uva", 0) or 0
            uvb = dev_data.get("uvb", 0) or 0
            voc = dev_data.get("voc", 0) or 0

            query = f"""
                INSERT INTO sensor_data ("time", "Date_time", "Timestamp", "aqi", "ch2o", "co", "co2", "devID", "light", "no", "no2", "o3", "pm1", "pm10", "pm2p5", "pressure", "rain", "rain_total", "rain_d", "rh", "so2", "sound", "temperature", "timestamp", "ts", "uva", "uvb", "voc")
                VALUES ('{time}', {date_time if date_time is not None else 'NULL'}, {Timestamp}, {aqi}, {ch2o}, {co}, {co2}, '{dev_id}', {light}, {no}, {no2}, {o3}, {pm1}, {pm10}, {pm2p5}, {pressure}, {rain}, {rain_total}, {rain_d if rain_d is not None else 'NULL'}, {rh}, {so2}, {sound}, {temperature}, {timestamp}, {ts}, {uva}, {uvb}, {voc});
            """
            
            print(f"Executing query: {query}") 
            cursor.execute(query)
            print(f"Inserted data for devID: {dev_id}")

        conn.commit()
        print("Data inserted successfully")
    except psycopg2.Error as e:
        print(f"Database Error: {e}")
        conn.rollback()  
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def scheduled_job():
    print("Running script....................")
    data_list = fetch_data_from_api()
    if data_list:
        insert_data_to_db(data_list)
    print("Script finished.")

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, 'interval', minutes=5)
    scheduler.start()

    try:
        print("Press Ctrl+C to exit")
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping scheduler......................")
        scheduler.shutdown()
