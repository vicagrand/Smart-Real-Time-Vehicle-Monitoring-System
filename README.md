# Smart Real-Time Vehicle Monitoring System 🚗📡

This project simulates and monitors real-time data from a virtual vehicle, using MQTT for data transfer, edge processing for anomaly detection, and a full cloud integration with AWS and Grafana for visualization and alerting.

## 👩‍💻 Authors

- Victoria Grand — ID: 211856208
- Noa Rofe — ID: 208328286

## 🎯 Project Goals

- Simulate vehicle telemetry data (speed, engine temperature, tire pressure).
- Send data via MQTT to both local and cloud brokers.
- Detect anomalies at the edge and send alerts back via MQTT.
- Store data in AWS S3 and analyze with Athena.
- Visualize data using Grafana (real-time) and QuickSight (historical).
- Send notifications via AWS SNS (email or SMS).

## 🛠️ Technologies Used

### Edge:

- `main.py` – Simulates vehicle data and publishes to MQTT.
- `edge_listener.py` – Detects anomalies and triggers alerts.

### Cloud (AWS):

- **IoT Core** – MQTT broker in the cloud.
- **Lambda** – Processes incoming messages (optional).
- **S3** – Stores raw data.
- **Glue & Athena** – Structures and queries data.
- **QuickSight** – BI visualization.
- **SNS** – Sends notifications.
- **Webhook** – Optional integration for external alerts.

### Real-time pipeline:

- **Mosquitto** – Local MQTT broker.
- **Telegraf** – Collects MQTT messages and pushes to InfluxDB.
- **InfluxDB** – Time-series database.
- **Grafana** – Real-time dashboard.

## 🧱 System Architecture

```
📡 main.py (Simulator)
   ⬇️
🟦 MQTT Broker (Mosquitto / IoT Core)
   ⬇️
🛠 Telegraf
   ⬇️
📦 InfluxDB
   ⬇️
📊 Grafana Dashboard
   ⬇️
☁️ AWS Lambda
   ⬇️
🔗 AWS SNS / Webhook
```

## 📈 Example Dashboards

- Engine temperature over time
- Speed trends
- Tire pressure per wheel
- Real-time anomaly alerts

## 🔐 Security

- IAM roles used to restrict AWS resources
- Option to upgrade MQTT to use TLS
- Topic separation for cleaner message flow

## 📦 Scalability

- System supports high-throughput via S3 + InfluxDB
- Additional vehicles/sensors can be added easily
- Architecture supports fleet-wide expansion

## 🔮 Future Enhancements

- Add GPS data
- Deploy with Docker
- Integrate predictive maintenance
- Use SES or Twilio for advanced notifications

## 📂 File Structure

```
├── main.py
├── edge_listener.py
├── mqtt_to_s3.py
├── mqtt_to_grafana.py
├── telegraf.conf
└── README.md
```

## 🧪 Screenshots

Include:

- Grafana dashboard
- QuickSight panel
- S3 data files
- SNS email alert example

## 📚 References

- [AWS Documentation](https://docs.aws.amazon.com/)
- [Grafana](https://grafana.com)
- [InfluxDB](https://www.influxdata.com/)
- [HiveMQ MQTT](https://www.hivemq.com/mqtt/)
- [Telegraf](https://docs.influxdata.com/telegraf/)

> **Note:** This project is part of our final academic submission. See full documentation in `Smart_Car_Monitoring_Report.docx`.

