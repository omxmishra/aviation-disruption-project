import joblib
import json
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "aviation_disruption_model.pkl")
columns_path = os.path.join(BASE_DIR, "models", "model_columns.json")

model = joblib.load(model_path)

with open(columns_path) as f:
    columns = json.load(f)


def predict_disruption(input_dict):
    df = pd.DataFrame([input_dict])

    df = pd.get_dummies(df)

    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return prediction