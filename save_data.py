import json
import boto3
import time
import random
from datetime import datetime

# === הגדרות אישיות שלך ===
BUCKET_NAME = 'vehicle-data-export'  # השם של הבאקט שיצרת
FOLDER_NAME = 'uploads'              # תיקייה בתוך הבאקט

# === יצירת נתונים לדוגמה (כמו מהרכב) ===
data = {
    "vehicle_id": "car_01",
    "speed": random.randint(50, 120),
    "engine_temp": round(random.uniform(70, 110), 1),
    "tire_pressure": [round(random.uniform(28, 35), 1) for _ in range(4)],
    "timestamp": datetime.utcnow().isoformat()
}

# === הפיכת הנתונים ל-JSON ===
json_data = json.dumps(data)

# === שמירה זמנית לקובץ מקומי ===
with open("vehicle_data.json", "w") as f:
    f.write(json_data)

# === העלאה ל-S3 ===
s3 = boto3.client('s3')
filename = f"{FOLDER_NAME}/vehicle_data_{int(time.time())}.json"
s3.upload_file("vehicle_data.json", BUCKET_NAME, filename)

print(f"הקובץ הועלה ל-S3: s3://{BUCKET_NAME}/{filename}")
