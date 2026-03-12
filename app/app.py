import streamlit as st
import pandas as pd
import joblib

# Set the page configuration
st.set_page_config(page_title="Kenya Car Price Predictor", page_icon="🚗", layout="centered")

# 1. Load the AI Brain (Cached so it only loads once)
@st.cache_resource
def load_model():
    try:
        return joblib.load('kenya_car_price_model.pkl')
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# 2. Frontend Title and Description
st.title("🚗 Kenya Used Car Price Predictor")
st.write("Enter the vehicle specifications below to instantly calculate its estimated market value in KES.")

# 3. Create the Input Form using Columns for a clean UI
st.markdown("### Vehicle Details")
col1, col2 = st.columns(2)

wit…
