# SPX Volatility Prediction Project

## Project Overview

Financial markets are inherently unpredictable, and volatility is one of the most critical risk measures for investors, traders, and risk managers. This project focuses on **forecasting near-term stock market volatility** by analyzing the S&P 500 index (SPX) returns, VIX index, realized volatility, and macroeconomic indicators including interest rates, inflation, and unemployment.  

By building predictive models and providing interactive dashboards, this project aims to help portfolio managers anticipate periods of high volatility, adjust allocations, and manage risk effectively.

---

## Project Objectives

- Analyze the relationship between SPX returns, VIX, realized volatility, and macroeconomic factors.  
- Train a **predictive model** for near-term SPX returns using these features.  
- Deploy a **Flask API** and/or **Streamlit dashboard** for user interaction.  
- Provide **visualizations** of SPX returns and volatility trends.  
- Ensure **reproducibility** through a `requirements.txt` file.

---

## How to Rerun Scripts/Notebooks

1. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt

2. **Train Model (Optional)**
If no pre-trained model exists: 
    ```bash
    python notebooks/train_model.py

3. **Run Flask API**
    ```bash
    python app_flask.py
- Endpoints:
    - POST /predict → send JSON with 9 features to get predicted SPX return
    - GET /plot → view example financial plots

4. **Run Streamlit Dashboard**
    ```bash
    streamlit run app_streamlit.py
- Interactive UI for entering features and seeing predicted SPX returns.
- Displays example charts for SPX return trends.

---

## Assumptions

- Historical relationships between SPX returns, VIX, realized volatility, and macroeconomic indicators are informative for near-term predictions.
- The 9 selected features capture the primary drivers of short-term SPX volatility.
- Predictive model performance is evaluated on limited historical data; results may vary in real-time conditions.

---

## Risks

- Financial markets are influenced by unforeseen macroeconomic shocks, geopolitical events, or market sentiment that may not be captured in the model.
- Model predictions should not be used as the sole basis for investment decisions.
- Deployment is currently in a development environment; not production-ready.

---

## Lifecycle Mapping 

- Data Collection: SPX returns, VIX, realized volatility, macroeconomic indicators.
- Data Cleaning & Feature Engineering: Handle missing values, compute derived features (e.g., volatility ratios).
- Model Training: Train regression model (Linear Regression or other algorithms).
- Model Evaluation: Check R², RMSE, residual plots.
- Deployment: Flask API and/or Streamlit dashboard.
- Monitoring & Updating: Future enhancements include retraining with new data and expanding input features.

---

## Instructions for Using APIs or Dashboards

- **Flask API**: 
    - POST /predict: 
        - Request: 
        ```json 
        {"features": [spx_close, vix, dgs10, fedfunds, cpi, unrate, rv_21d_pct, vrp_ratio, rate_shock_5d_bps]}
        ```
        - Response:
        ```json
        {"prediction": 0.12345}
        ```
    - GET /plot: Returns example plots for SPX returns, VIX, and realized volatility embedded as images in HTML.

- **Streamlit Dashboard**: 
    - Launch: 
    ```bash
    streamlit run app_streamlit.py
    ```
    - Enter all 9 features in the number input fields.
    - Click Predict to see the predicted SPX return.
    - View example charts under the “Example SPX Return Trend” section.
