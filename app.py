import streamlit as st
import pandas as pd  # Assuming you're using pandas for data handling

import joblib

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")  # Load only once

model1 = load_model()


st.title("Stock Price Prediction")

# Get user input for each feature
open_price = st.number_input("Enter Open Price:")
high_price = st.number_input("Enter High Price:")
low_price = st.number_input("Enter Low Price:")
close_price = st.number_input("Enter Close Price:")
adj_close_price = st.number_input("Enter Adjusted Close Price:")
volume = st.number_input("Enter Volume:")

# Create a DataFrame from user input
user_input = pd.DataFrame({
    'Open': [open_price],
    'High': [high_price],
    'Low': [low_price],
    'Close': [close_price],
    'Adj Close': [adj_close_price],
    'Volume': [volume]
})

# Make prediction
prediction = model1.predict(user_input)  # Pass the DataFrame directly

st.write("Predicted Stock Movement:", prediction)