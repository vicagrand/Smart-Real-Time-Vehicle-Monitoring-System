import json
import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "car/data"

# פונקציה לבדיקת אנומליות
def detect_anomaly(data):
    anomalies = []
    # בדיקה לטמפרטורת מנוע
    if data.get("engine_temp", 0) > 110:
        anomalies.append("Engine temperature is too high!")
    # בדיקה ללחץ האוויר בכל צמיג
    tire_pressures = data.get("tire_pressure", [])
    for idx, pressure in enumerate(tire_pressures, start=1):
        if pressure < 30:
            anomalies.append(f"Tire {idx} pressure is too low!")
    return anomalies

# פונקציות callback ל-MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to broker.")
        client.subscribe(topic)
    else:
        print("Connection failed with code:", rc)

def on_message(client, userdata, msg):
    try:
        # המרת ההודעה ממחרוזת ל-JSON
        data = json.loads(msg.payload.decode())
        print(f"Received data: {data}")
        # בדיקת אנומליות
        anomalies = detect_anomaly(data)
        if anomalies:
            print("Anomalies detected:")
            for anomaly in anomalies:
                print("  -", anomaly)
        else:
            print("No anomalies detected.")
    except Exception as e:
        print("Error processing message:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, keepalive=60)
client.loop_forever()
