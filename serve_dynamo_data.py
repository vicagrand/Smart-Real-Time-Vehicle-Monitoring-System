from flask import Flask, jsonify
import pandas as pd
import ast

app = Flask(__name__)

@app.route("/data")
def get_data():
    df = pd.read_csv("results.csv")
    # המרת מחרוזת לרשימה
    df["tire_pressure"] = df["tire_pressure"].apply(ast.literal_eval)
    # פיצול ללחצי אוויר בודדים
    for i in range(4):
        df[f"tire_{i+1}"] = df["tire_pressure"].apply(lambda x: x[i])

    df = df.drop(columns=["tire_pressure"])
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(port=5001)
