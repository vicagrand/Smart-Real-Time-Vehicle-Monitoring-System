from flask import Flask, jsonify
import paho.mqtt.client as mqtt
import json
from datetime import datetime

app = Flask(__name__)
data_log = []

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "car/data"

def on_message(client, userdata, msg):
    global data_log
    try:
        payload = json.loads(msg.payload.decode())
        payload["timestamp"] = datetime.utcnow().isoformat()
        data_log.append(payload)
        print("Raw message:", msg.payload)
        if len(data_log) > 100:
            data_log.pop(0)
        print("Received:", payload)
    except Exception as e:
        print("Error decoding JSON:", e)

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.subscribe(MQTT_TOPIC)
mqtt_client.on_message = on_message
mqtt_client.loop_start()

@app.route("/data")
def get_data():
    return jsonify(data_log)




if __name__ == "__main__":
    app.run(port=5000)
