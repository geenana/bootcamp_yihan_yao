
# Predicting Stock Market Volatility using Macroeconomic Indicators
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Financial markets are highly unpredictable, and volatility is one of the most critical measures of risk for portfolio managers, traders, and risk officers. Anticipating periods of high volatility allows investors to adjust portfolio allocations and manage risks. The challenge is that volatility is influenced by both market dynamics and macroeconomic shocks, making it difficult to predict accurately. 

## Project Purpose 
This project seeks to forecast near-term stock market volatility by analyzing VIX index and realized volatility of the S&P 500 and incorporating macroeconomic indicators such as interest rates, inflation, and unemployment. By understanding the drivers of volatility and building predictive models, we can provide actionable insights for investment decision-making and risk management. 

## Stakeholder & User
Decision owner: a portfolio manager (PM) responsible for asset allocation and risk exposure decisions 
Users: portfolio manager + risk analysts who operate forecasting tools and generate weekly market reports 
The workflow requires a weekly or monthly updates to adjust portfolios in anticipation of volatility spikes. 

## Useful Answer & Decision
Predictive: estimating near-term volatility levels with confidence intervals 
Metric: predicted near-term volatility, confidence bands, probability of breaking thresholds 
Artifact: forecasting model, scenario-based dashboards, risk alerts that indicate when defined thresholds are breached 

## Assumptions & Constraints
- Data availability: market data (S&P 500, VIX) is accessible via Yahoo Finance; macro data via FRED 
- Stationarity: assumes stable data pipeline and statistical properties of volatility are reasonably stable within the analysis horizon; crisis or calm periods 
(regime shifts) may break this assumption 
- Stable relationships: assumes macroeconomic indicators have stable and interpretable relationships with volatility over time; the correlation may change during 
crisis or calm periods 
- Capacity: assumes analysis is feasible with publicly available data and academic computing resources 
- Compliance: data sources are public and do not raise compliance issues 
- Runtime: computation should run on local machine without requiring large clusters 
- Latency: market data is available with minimal delay; macro indicators are published monthly and introduce reporting lags; assumes weekly refresh is sufficient 
for decision-making 

## Known Unknowns / Risks
- Macro data publication lag (monthly vs daily frequency)
- Model overfitting to past volatility shocks 
- Uncertainty in macro due to market volatility causal linkage; monitor by re-estimaing causal coefficients quarterly 
- Regime shifts may break some of the assumptions mentioned above; monitor by checking regime probability from Markov-switching model and setting criteria for 
switching to "crisis" mode and inflating prediction interval width by a chosen factor 
- Potentially missing data; monitor by creating a daily dashboard recording %missing, %zeros, duplicate rows 

## Data Storage

### Folder Structure
The `data/` directory is organized as follows:
- **'data/raw/'** → Contains timestamped CSV files of downloaded market data  
- **'data/processed/'** → Contains cleaned and standardized Parquet files created from raw CSVs 

### File Formats
- **CSV (`.csv`)**  
    - used for raw data storage. 
    - Pros: human-readable, ubiquitous, easy diffs in git 
    - Cons: larger fils, no schema, type loss (dates/numbers as text)

- **Parquet (`.parquet`)**  
    - Used for processed data storage. 
    - Pros: columnar, compressed, preserves types, very fast reads, supports efficient querying 
    - Cons: binary format, requires an engine (pyarrow/fastparquet)

### Reads/Writes 

- Market data is fetched with `yfinance`. 
- Saved into `data/raw/` using the utility function `save_csv()`. 
- Raw CSV files are reloaded in notebooks, then saved into `data/processed/` as Parquet. 
- File paths are automatically created based on environment variables defined in the '.env' file 
(DATA_DIR_RAW and DATA_DIR_PROCESSED). 

### Validation Checks 

- Shape equality between original CSV and reloaded Parquet. 
- `date` column is in datetime format. 
- `adj_close` column is numeric. 
- Additional validation includes checking for missing values and required columns. 

### Assumptions
- Yahoo Finance (`yfinance`) provides sufficient historical market and volatility data for the project.  
- Required columns (`date`, `adj_close`) are always present in raw data.  
- Date columns can be parsed into datetime format, and price columns can be parsed into numeric types.  

### Risks
- `yfinance` is a free service and may experience outages, rate limits, or API changes.  
- Column names in the source data may change, breaking downstream processing or validation.   
- Parquet compatibility can vary across Python environments if different versions of `pyarrow` or `fastparquet` are used.  

## Feature Engineering

This project generates additional features based on raw SPX, VIX, and macroeconomic datasets to improve predictive modeling.  
Below are the engineered features.

- **`rv_21d_pct`**: Rolling standard deviation of daily log returns over approximately 1 trading month, annualized and expressed in percent. 

- **`vrp_ratio`**: Ratio of implied volatility (VIX) to realized volatility minus 1. 

- **`rate_shock_5d_bps`**: 5-business-day change in the 10-year yield, expressed in basis points. 

## Lifecycle Mapping
Goal → Stage → Deliverable
- Goal: Define volatility forecasting problem → Problem Framing & Scoping → Scoping paragraph + stakeholder context artifact + repo skeleton 
- Goal: Collect and clean data → Data Acquisition/Ingestion & Data Storage → Clean + aligned datasets in /data/
- Goal: Explore data and engineer features → Exploratory Data Analysis & Feature Engineering → Realized volatility metrics and regime indicators 
- Goal: Build and evaluate models → Modeling & Evaluation → Forecasting models for realized volatility + backtesting results 
- Goal: Communicate insights to stakeholders → Results Reporting & Delivery Design → Dashboards + risk alerts + summary report 

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates 
