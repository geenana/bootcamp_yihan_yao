# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|---------------------|-------------------|
| **1. Problem Framing & Scoping** | Defined the goal to forecast near-term SPX volatility using VIX and macro indicators. | Financial markets are unpredictable; macro data has reporting lags; multiple stakeholders with different KPIs. | Focused on near-term volatility prediction; defined metrics like predicted volatility and confidence intervals; aligned scope with PM needs. | Incorporate scenario-based or stress-testing objectives earlier. |
| **2. Tooling Setup** | Installed Python, Pandas, NumPy, Scikit-learn, yfinance, FRED API, Streamlit, Flask. | Dependency versions varied across environments; initial data loading scripts were slow. | Used virtual environments; structured scripts in `/src/`; documented package versions in `requirements.txt`. | Automate environment setup with Docker or conda environment files. |
| **3. Python Fundamentals** | Applied Pandas for cleaning, NumPy for calculations, Matplotlib/Seaborn for plots. | Handling time series alignment, missing data, and feature engineering required iterative debugging. | Reviewed documentation, experimented in notebooks, modularized functions for reusability. | Continue practicing modular design and vectorized operations. |
| **4. Data Acquisition / Ingestion** | Downloaded S&P 500, VIX from Yahoo Finance; macro data from FRED. | FRED macro data is monthly; SPX/VIX is daily, so alignment was tricky. | Created ingestion pipeline with resampling and interpolation; versioned raw CSVs in `/data/raw/`. | Implement automated scheduling and integrity checks for new data. |
| **5. Data Storage** | Stored raw CSVs in `/data/raw/` and processed Parquet files in `/data/processed/`. | Potential schema changes in CSV or API. | Used Parquet for processed data; added validation for columns, types, and missing values. | Consider cloud storage for scalability and historical snapshots. |
| **6. Data Preprocessing** | Converted dates to datetime; filled missing values; calculated returns and rolling volatility. | Handling missing macro values and outliers in SPX returns. | Imputed or forward-filled missing macro values; capped extreme outliers. | Automate preprocessing pipeline; integrate checks for new data anomalies. |
| **7. Outlier Analysis** | Detected spikes in SPX returns, extreme VIX movements. | Hard to distinguish market shocks from data errors. | Used capping and logging instead of removing; flagged extreme events for review. | Explore automated anomaly detection models. |
| **8. Exploratory Data Analysis (EDA)** | Plotted SPX returns, VIX, realized volatility; computed correlations. | Some correlations unstable over crisis vs calm periods. | Focused on time-varying patterns; visualized rolling correlations. | Add interactive EDA dashboards for better exploration. |
| **9. Feature Engineering** | Created `rv_21d_pct`, `vrp_ratio`, `rate_shock_5d_bps`. | Choosing window sizes and transformations; lag selection. | Validated with domain knowledge and correlation analysis; tested model sensitivity. | Experiment with regime-switching features or macro factor composites. |
| **10. Modeling (Regression / Time Series / Classification)** | Built linear regression on engineered features for realized volatility; tried simple tree-based models. | Small dataset, risk of overfitting; non-stationarity. | Selected regularized linear regression; tested backtesting performance; documented assumptions. | Evaluate ensemble and probabilistic forecasting models. |
| **11. Evaluation & Risk Communication** | Used RMSE, R², and visual backtests; tracked error bands. | Communicating uncertainty to PM; low confidence during regime shifts. | Displayed prediction intervals; provided alerts when thresholds breached. | Automate confidence interval recalibration; incorporate stress scenarios. |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Created Streamlit dashboard and Flask API for model access; summary report in Markdown. | Explaining technical metrics to non-technical stakeholders. | Provided intuitive charts, thresholds, and clear explanations; used scenario visualizations. | Include email or Slack notifications for risk alerts. |
| **13. Productization** | Packaged model and preprocessing functions; saved artifacts in `/model/` and `/src/`. | Maintaining reproducibility across environments. | Pickled trained models; documented dependencies in `requirements.txt`. | Containerize with Docker for reproducible deployments. |
| **14. Deployment & Monitoring** | Deployed Flask API and Streamlit dashboard locally; set up basic error handling. | No production-grade monitoring; potential data drift. | Implemented logging and checkpoints for inputs and outputs. | Integrate monitoring for model drift, missing data, latency; consider cloud deployment. |
| **15. Orchestration & System Design** | Defined DAG for tasks: ingest → clean → train → report; organized scripts in `/src/`. | Dependencies between tasks and file outputs need manual coordination. | Added logging, checkpoint artifacts, and idempotent task design. | Automate scheduling via Airflow or Prefect; add notifications on failure. |
| **16. Lifecycle Review & Reflection** | End-to-end process from data ingestion to dashboard visualization completed. | Struggled with integrating macroeconomic lags and regime shifts; keeping pipeline reproducible. | Modularized code, documented assumptions, versioned data. | Explore automated retraining, better scenario analysis, and cloud deployment. |

---

## Reflection Prompts

- **Most difficult stage:** Feature engineering and modeling due to volatility regime shifts, macro lags, and overfitting risk.  
- **Most rewarding stage:** Deployment and visualization; seeing predictions on the dashboard and Flask API work in real-time.  
- **Stage connections:** Decisions in data preprocessing, EDA, and feature engineering directly influenced model performance and interpretability; deployment required modular code.  
- **Do differently:** Integrate automated monitoring, data versioning, and cloud deployment from the start; use probabilistic or ensemble forecasting methods.  
- **Skills to strengthen:** Time-series analysis, probabilistic forecasting, automated monitoring, cloud deployment, and interactive dashboard design.  
