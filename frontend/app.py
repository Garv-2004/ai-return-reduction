import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/return_model.pkl")

st.title("AI Return Prediction")

price = st.number_input("Price")
rating = st.number_input("Rating")
returns = st.number_input("Previous Returns")

if st.button("Predict"):
    sample = pd.DataFrame([{
        'user_id': 1,
        'product_id': 1,
        'category': 1,
        'price': price,
        'size': 1,
        'rating': rating,
        'previous_returns': returns,
        'purchase_frequency': 5
    }])

    pred = model.predict(sample)

    if pred[0] == 1:
        st.error("High return probability")
    else:
        st.success("Low return probability")