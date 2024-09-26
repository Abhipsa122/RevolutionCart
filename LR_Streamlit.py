# prompt: generate code for streamlit to deploy the app

%%writefile app.py
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'linear_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a Streamlit app
st.title("Monthly Revenue Prediction")

# Input features
st.header("Enter the following information:")
total_orders = st.number_input("Total Orders", min_value=0)
avg_order_value = st.number_input("Average Order Value", min_value=0.0)
customer_acquisition_cost = st.number_input("Customer Acquisition Cost", min_value=0.0)
marketing_spend = st.number_input("Marketing Spend", min_value=0.0)
average_customer_lifetime_value = st.number_input("Average Customer Lifetime Value", min_value=0.0)
website_traffic = st.number_input("Website Traffic", min_value=0)


# Make prediction when the user clicks the button
if st.button("Predict"):
    input_data = pd.DataFrame([[total_orders, avg_order_value, customer_acquisition_cost, marketing_spend, average_customer_lifetime_value, website_traffic]],
                            columns=['total_orders', 'avg_order_value', 'customer_acquisition_cost', 'marketing_spend', 'average_customer_lifetime_value', 'website_traffic'])

    prediction = loaded_model.predict(input_data)[0]

    st.header("Predicted Monthly Revenue:")
    st.write(f"${prediction:.2f}")

