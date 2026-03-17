import joblib
import json
import pandas as pd

# Load model
model = joblib.load("models/aviation_disruption_model.pkl")

# Load columns
with open("models/model_columns.json") as f:
    columns = json.load(f)

def predict_disruption(input_dict):
    df = pd.DataFrame([input_dict])

    df = pd.get_dummies(df)

    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)[0]

    return prediction