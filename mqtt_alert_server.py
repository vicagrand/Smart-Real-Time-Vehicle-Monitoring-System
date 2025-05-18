from flask import Flask, request
import paho.mqtt.publish as publish
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/mqtt-alert", methods=['POST'])
def mqtt_alert():
    try:
        alert_data = request.json
        print("📥 קיבלנו התראה מ-Grafana:", json.dumps(alert_data, indent=2))

        mqtt_payload = {
            "vehicle_id": "car_01",
            "alert": "HIGH_ENGINE_TEMP",
            "value": alert_data.get("evalMatches", [{}])[0].get("value", "N/A"),
            "timestamp": datetime.utcnow().isoformat()
        }

        print("🔁 שולחת ל-MQTT:", json.dumps(mqtt_payload, indent=2))

        publish.single("car/alert", json.dumps(mqtt_payload), hostname="localhost", port=1883)

        print("✅ MQTT נשלח בהצלחה!")
        return "OK", 200

    except Exception as e:
        print("❌ שגיאה כללית בטיפול בהתראה:", e)
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

