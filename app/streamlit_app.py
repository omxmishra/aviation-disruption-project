import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predict import predict_disruption

st.set_page_config(
    page_title="Aviation Disruption Intelligence",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    background-color: #0e1117;
}

h1, h2, h3 {
    color: #c084fc;
    font-weight: 700;
}

p {
    font-size: 16px;
    color: #d1d5db;
}

.stButton>button {
    background: linear-gradient(135deg, #7c3aed, #a855f7);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: 600;
    font-size: 16px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #6d28d9, #9333ea);
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("✈️ Navigation")

page = st.sidebar.radio("Go to", ["Prediction", "Analytics"])

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/master_aviation_disruptions.csv")

data = load_data()

# -------------------- PREDICTION --------------------
if page == "Prediction":

    st.title("✈️ Aviation Disruption Prediction System")
    st.write("Predict whether a flight will be **Cancelled or Rerouted** during geopolitical disruptions.")

    col1, col2, col3 = st.columns(3)

    with col1:
        airline = st.selectbox("Select Airline", sorted(data["airline"].dropna().unique()))

    with col2:
        origin = st.selectbox("Origin Airport", sorted(data["origin"].dropna().unique()))

    with col3:
        destination = st.selectbox("Destination Airport", sorted(data["destination"].dropna().unique()))

    col4, col5, col6 = st.columns(3)

    with col4:
        severity = st.selectbox("Conflict Severity", ["Low", "Medium", "High", "Very High", "None"])

    with col5:
        severity_level = st.selectbox("Disruption Severity Level", ["Low", "Moderate", "Severe", "Critical", "None"])

    with col6:
        disruption_type = st.selectbox("Disruption Type", ["None", "Ground Stop", "Fuel Shortage", "Security Lockdown", "Flight Cancellations"])

    st.markdown("---")

    if st.button("🚀 Predict Disruption"):

        input_dict = {
            "airline": airline,
            "origin": origin,
            "destination": destination,
            "severity": severity,
            "severity_level": severity_level,
            "disruption_type": disruption_type
        }

        prediction = predict_disruption(input_dict)

        if prediction == 1:
            st.error("⚠️ Flight is likely to be CANCELLED")
        else:
            st.success("✅ Flight is likely to be REROUTED")

# -------------------- ANALYTICS --------------------
elif page == "Analytics":

    st.title("📊 Aviation Disruption Analytics")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top Disrupted Airlines")
        st.bar_chart(data["airline"].value_counts().head(10))

    with col2:
        st.subheader("Most Affected Airports")
        st.bar_chart(data["origin"].value_counts().head(10))

    st.markdown("---")

    st.subheader("Severity Distribution")
    st.bar_chart(data["severity"].value_counts())

    st.markdown("---")

    st.subheader("Dataset Overview")
    st.dataframe(data.head(50))