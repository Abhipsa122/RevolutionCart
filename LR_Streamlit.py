# prompt: generate code for streamlit to deploy the app

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'linear_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a Streamlit app
st.title("Monthly Revenue Prediction")

# Get input from the user
st.header("Enter Store Information")
total_orders = st.number_input("Total Orders")
avg_order_value = st.number_input("Average Order Value")
customer_acquisition_cost = st.number_input("Customer Acquisition Cost")

# Make a prediction when the user clicks a button
if st.button("Predict"):
  # Create a DataFrame with the user's input
  input_data = pd.DataFrame({
      'total_orders': [total_orders],
      'avg_order_value': [avg_order_value],
      'customer_acquisition_cost': [customer_acquisition_cost]
  })

  # Make a prediction using the loaded model
  prediction = loaded_model.predict(input_data)[0]

  # Display the prediction
  st.header("Predicted Monthly Revenue:")
  st.write(f"${prediction:.2f}")
