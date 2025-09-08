import streamlit as st
import pandas as pd
import pickle

# Loading the trained model
MODEL_PATH = "D:\\Machine learning\\rainfallmodel.pkl"  
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

#  UI
st.title("🌧️ Rainfall Prediction System")
st.markdown("Enter the details below to predict rainfall.")

# User inputs
col1, col2, col3 = st.columns(3)
with col1:
    pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1013.0, step=0.1)
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
with col2:
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
    cloud = st.number_input("Cloud Cover (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
with col3:
    sunshine = st.number_input("Sunshine Duration (hours)", min_value=0.0, max_value=24.0, value=5.0, step=0.1)
    wind_direction = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, value=180.0, step=0.1)
    wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)

# Predict button
if st.button("Predict Rainfall ☁️"):
    input_data = pd.DataFrame([[pressure, temperature, humidity, cloud, sunshine, wind_direction, wind_speed]], 
                               columns=["pressure", "temparature", "humidity", "cloud", "sunshine", "winddirection", "windspeed"])
    if isinstance(model, dict):
        model = model.get("model")  

    if model:
        prediction = model.predict(input_data)
    else:
        print("Model not found in the dictionary.")

    if(prediction==1):
        st.success("Yes, there will be rainfall")
    else:
        st.success("No rainfall !")

st.markdown("---")

