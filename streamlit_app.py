import streamlit as st
import joblib
import pandas as pd

model = joblib.load("crypto_volatility_model.pkl")

st.title("Crypto Volatility Predictor")

open_price = st.number_input("Open")
high_price = st.number_input("High")
low_price = st.number_input("Low")
close_price = st.number_input("Close")
volume = st.number_input("Volume")
market_cap = st.number_input("Market Cap")

if st.button("Predict"):

    data = pd.DataFrame([[open_price,high_price,low_price,close_price,
                          volume,market_cap,0,0,0]],
        columns=[
            "open","high","low","close",
            "volume","marketCap",
            "liquidity_ratio","MA_7","MA_30"
        ])

    prediction = model.predict(data)

    st.write("Predicted Volatility:",prediction)
