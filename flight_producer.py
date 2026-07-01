import time
import json
import stomp
import random

class FlightProducer:
    def __init__(self):
        # Connects to ActiveMQ's STOMP port
        self.conn = stomp.Connection([('localhost', 61613)]) 
        self.conn.connect('admin', 'admin', wait=True)

    def send_data(self):
        print("Starting flight telemetry stream... (Press Ctrl+C to stop)")
        try:
            while True:
                # Generate random flight data
                data = {
                    "speed": round(random.uniform(200.0, 800.0), 2),
                    "altitude": round(random.uniform(10000.0, 35000.0), 2),
                    "roll": round(random.uniform(-45.0, 45.0), 2)
                }
                
                # Send the data to the ActiveMQ queue
                self.conn.send(body=json.dumps(data), destination='/queue/flight_data')
                print(f"Sent to ActiveMQ: {data}")
                
                time.sleep(1) # Send data every 1 second
                
        except KeyboardInterrupt:
            print("\nStopping producer...")
            self.conn.disconnect()

if __name__ == '__main__':
    producer = FlightProducer()
    producer.send_data()