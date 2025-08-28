import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load('model/model.pkl')

st.title("SPX Return Prediction Dashboard")

st.write("Input the following features to predict SPX return:")

# User inputs for all 9 features
spx_close = st.number_input("SPX Close", value=0.070698)
vix = st.number_input("VIX", value=0.387695)
dgs10 = st.number_input("10Y Treasury Yield", value=0.85)
fedfunds = st.number_input("Fed Funds Rate", value=0.09)
cpi = st.number_input("CPI", value=260.319)
unrate = st.number_input("Unemployment Rate", value=6.9)
rv_21d_pct = st.number_input("21d Realized Volatility", value=721.180880)
vrp_ratio = st.number_input("VRP Ratio", value=-0.999462)
rate_shock_5d_bps = st.number_input("5d Rate Shock (bps)", value=9.0)

features = [spx_close, vix, dgs10, fedfunds, cpi, unrate, rv_21d_pct, vrp_ratio, rate_shock_5d_bps]

# Predict button
if st.button("Predict"):
    try:
        pred = model.predict(np.array(features).reshape(1, -1))
        st.success(f"Predicted SPX Return: {pred[0]:.4f}")
    except Exception as e:
        st.error(f"Error in prediction: {str(e)}")

# Simple chart example
st.subheader("Example SPX Return Trend")

dates = pd.date_range(start="2020-10-23", periods=5)
spx_returns = [0.053491,-0.331233,-0.064779,-1.505799,0.763468]

fig, ax = plt.subplots()
ax.plot(dates, spx_returns, marker='o')
ax.set_title("SPX Returns Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("SPX Return")
st.pyplot(fig)
