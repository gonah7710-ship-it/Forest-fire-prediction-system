import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="Forest Fire Prediction", page_icon="🔥")

st.title("🔥 Forest Fire Prediction App")
st.write("Enter environmental details to predict forest fire risk.")

# Input fields
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[temperature, humidity, wind_speed, rainfall]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🔥 High Risk of Forest Fire!")
    else:
        st.success("🌿 Low Risk of Forest Fire")
