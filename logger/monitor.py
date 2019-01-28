import time
import os
import random
from influxdb import InfluxDBClient

influx_host = os.getenv("INFLUX_HOST")
port = 8086
dbname = "environment"
user = "root"
password = "root"
host = os.getenv("PI_HOST")
sleep_time = os.getenv("SAMPLE_PAUSE")
fake_sensor = os.getenv("FAKE_SENSOR")

client = InfluxDBClient(influx_host, port, user, password, dbname)
client.create_database(dbname)

def get_cpu_temp():
    path="/sys/class/thermal/thermal_zone0/temp"
    f = open(path, "r")
    temp_raw = int(f.read().strip())
    temp_cpu = float(temp_raw / 1000.0)
    return temp_cpu

def get_data_points():
    if fake_sensor:
        humidity, temperature = random.randint(400, 600) * 1.0/10, random.randint(150, 200) * 1.0/10
    else:
        import Adafruit_DHT
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    iso = time.ctime()
    json_body = [{
                    "measurement": "ambient_celcius",
                    "tags": {"host": host},
                    "time": iso,
                    "fields": {
                        "value": temperature,
                        }
                    },
                {
                    "measurement": "humidity_percent",
                    "tags": {"host": host},
                    "time": iso,
                    "fields": {
                        "value": humidity,
                    }
                }]
    return json_body

try:
    sleep_duration = float(sleep_time)
    while True:
        json_body = get_data_points()
        client.write_points(json_body)
        print (".")
        time.sleep(sleep_duration)

except KeyboardInterrupt:
    pass
