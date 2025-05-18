import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

client = mqtt.Client()
broker = "broker.hivemq.com"
client.connect("localhost", 1883, 60)



while True:
    tire_pressure = [round(random.uniform(28, 35), 1) for _ in range(4)]

    data = {
        "vehicle_id": "car_01",
        "speed": random.randint(50, 120),
        "engine_temp": round(random.uniform(70, 120), 1),
        "tire_front_left": tire_pressure[0],
        "tire_front_right": tire_pressure[1],
        "tire_rear_left": tire_pressure[2],
        "tire_rear_right": tire_pressure[3],
        "timestamp": datetime.utcnow().isoformat()
    }

    client.publish("car/data", json.dumps(data))
    print("Published:", data)
    time.sleep(2)
