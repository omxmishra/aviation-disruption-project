import streamlit as st
import pandas as pd
import joblib
import json

# Load model
model = joblib.load("models/aviation_disruption_model.pkl")

# Load column names
with open("models/model_columns.json") as f:
    columns = json.load(f)

st.title("✈️ Aviation Disruption Prediction System")

st.write("Predict whether a flight will be **Cancelled or Rerouted** during disruptions.")

# Inputs
airline = st.text_input("Airline")
origin = st.text_input("Origin Airport")
destination = st.text_input("Destination Airport")
severity = st.selectbox("Conflict Severity", ["Low","Medium","High"])
severity_level = st.selectbox("Disruption Severity Level", ["Low","Medium","High"])
disruption_type = st.text_input("Disruption Type")

# Prediction button
if st.button("Predict Disruption"):

    input_data = pd.DataFrame({
        "airline":[airline],
        "origin":[origin],
        "destination":[destination],
        "severity":[severity],
        "severity_level":[severity_level],
        "disruption_type":[disruption_type]
    })

    input_encoded = pd.get_dummies(input_data)

    input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_encoded)[0]

    if prediction == 1:
        st.error("Prediction: Flight likely CANCELLED")
    else:
        st.success("Prediction: Flight likely REROUTED")