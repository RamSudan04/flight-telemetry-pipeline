import json
import stomp
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB Credentials (matching your docker-compose.yml)
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "super-secret-auth-token"
INFLUX_ORG = "internship"
INFLUX_BUCKET = "flight_data"

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN)
write_api = client.write_api(write_options=SYNCHRONOUS)

class FlightListener(stomp.ConnectionListener):
    def on_message(self, frame):
        # Read data from ActiveMQ
        data = json.loads(frame.body)
        print(f"Received & Saving to InfluxDB: {data}")
        
        # Format data for InfluxDB
        point = Point("telemetry") \
            .field("speed", data["speed"]) \
            .field("altitude", data["altitude"]) \
            .field("roll", data["roll"]) \
            .time(time.time_ns(), WritePrecision.NS)
        
        # Write to database
        write_api.write(INFLUX_BUCKET, INFLUX_ORG, point)

# Connect to ActiveMQ
conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', FlightListener())
conn.connect('admin', 'admin', wait=True)
conn.subscribe(destination='/queue/flight_data', id=1, ack='auto')

print("Listening for flight data... (Press Ctrl+C to stop)")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDisconnecting...")
    conn.disconnect()