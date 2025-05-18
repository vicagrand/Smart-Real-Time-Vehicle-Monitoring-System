import json
import boto3
import time
import paho.mqtt.client as mqtt
from datetime import datetime

BUCKET_NAME = 'vehicle-data-export'
FOLDER_NAME = 'uploads'

s3 = boto3.client('s3')

data_batch = []

def upload_to_s3(data):
    filename = f"{FOLDER_NAME}/vehicle_data_{int(time.time())}.json"
    with open("vehicle_data.json", "w") as f:
        json.dump(data, f)
    s3.upload_file("vehicle_data.json", BUCKET_NAME, filename)
    print(f"הועלה ל־S3: s3://{BUCKET_NAME}/{filename}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        payload["timestamp"] = datetime.utcnow().isoformat()
        data_batch.append(payload)
        print("התקבל:", payload)
    except Exception as e:
        print("שגיאה בקריאת JSON:", e)

# MQTT setup
client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("car/data")
client.on_message = on_message
client.loop_start()

try:
    while True:
        time.sleep(10)  # כל 10 שניות
        if data_batch:
            upload_to_s3(data_batch[:])  # שליחה של העתק
            data_batch.clear()
except KeyboardInterrupt:
    print("נעצרת תוכנית.")
    client.loop_stop()
