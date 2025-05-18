import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime
import os

CSV_FILE = "realtime_data.csv"
HEADER = ["timestamp", "vehicle_id", "speed", "engine_temp", "tire_1", "tire_2", "tire_3", "tire_4"]

# אם הקובץ לא קיים - נכתוב כותרת
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("car/data")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    data["timestamp"] = datetime.utcnow().isoformat()

    # לפרק את הלחצים
    tire = data.get("tire_pressure", [0,0,0,0])
    row = [
        data["timestamp"],
        data["vehicle_id"],
        data["speed"],
        data["engine_temp"],
        tire[0], tire[1], tire[2], tire[3]
    ]

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    print("Saved row:", row)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
