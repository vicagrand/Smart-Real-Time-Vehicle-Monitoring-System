import paho.mqtt.client as mqtt
import ssl
import time
import json
import random

# נתונים קבועים
ENDPOINT = "afqbo2w24c9s6-ats.iot.eu-north-1.amazonaws.com"
PORT = 8883
CLIENT_ID = "car_01"
TOPIC = "car/data"

# קבצי האישורים
CA_PATH = "AmazonRootCA1.pem"
CERT_PATH = "certificate.pem.crt"
KEY_PATH = "private.pem.key"

# יצירת לקוח MQTT עם הצפנת TLS
client = mqtt.Client(client_id=CLIENT_ID)
client.tls_set(ca_certs=CA_PATH,
               certfile=CERT_PATH,
               keyfile=KEY_PATH,
               tls_version=ssl.PROTOCOL_TLSv1_2)

# התחברות לשרת
client.connect(ENDPOINT, PORT)
client.loop_start()

# שליחת נתונים כל 3 שניות
try:
    while True:
        data = {
            "vehicle_id": "car_01",
            "speed": random.randint(0, 160),
            "engine_temp": round(random.uniform(70, 120), 1),
            "tire_pressure": [round(random.uniform(28, 35), 1) for _ in range(4)]
        }
        json_data = json.dumps(data)
        client.publish(TOPIC, json_data)
        print("Published to AWS:", json_data)
        time.sleep(3)

except KeyboardInterrupt:
    print("Stopped by user")
    client.loop_stop()
    client.disconnect()
