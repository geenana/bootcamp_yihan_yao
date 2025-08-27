# Model Report

## Problem Statement

Financial markets are highly unpredictable, and volatility is one of the most critical measures of     risk for portfolio managers, traders, and risk officers. Anticipating periods of high volatility allows investors     to adjust portfolio allocations and manage risks. The challenge is that volatility is influenced by both market     dynamics and macroeconomic shocks, making it difficult to predict accurately.

This project seeks to forecast near-term stock market volatility by analyzing VIX index and realized     volatility of the S&P 500 and incorporating macroeconomic indicators such as interest rates, inflation, and     unemployment. By understanding the drivers of volatility and building predictive models, we can provide actionable     insights for investment decision-making and risk management.

## Methods

### Data Sources & Storage

- Market data (S&P 500, VIX) retrieved via Yahoo Finance (yfinance).

- Macro data (interest rates, CPI, unemployment) from FRED.

- Data pipeline organized into data/raw/ (CSV) and data/processed/ (Parquet).

- Validation checks ensure column consistency, datetime formatting, and absence of missing values.

### Feature Engineering

- **rv_21d_pct**: 21-day realized volatility (annualized).

- **vrp_ratio**: Volatility risk premium, calculated as (VIX / realized volatility) - 1.

- **rate_shock_5d_bps**: Five-day change in the 10-year yield (bps).

### Modeling Approach

- Start with baseline linear models between volatility and returns.

- Handle missing data via median imputation and outlier treatment via 3σ rule.

- Evaluate predictive performance using Mean Absolute Error (MAE) and scenario sensitivity.

## Results with Charts

![](../deliverables/images/risk_return.png)

*Chart 1: Risk-Return Relationship*

- **Description**: The chart shows the relationship between VIX (volatility) on the x-axis     and S&P returns on the y-axis. Most data points cluster near the origin, but at higher volatility levels the     distribution of returns widens, showing occasional extreme losses (–1.5) and rare outsized gains (~+0.6).

- **Key Takeaway**: Volatility is strongly associated with increased dispersion of returns.     High volatility environments tend to carry downside risk with occasional positive spikes, confirming     volatility’s asymmetry as a risk indicator.

| Assumption                    |   Baseline Mean Return |   Alternative Scenario Mean Return |
|:------------------------------|-----------------------:|-----------------------------------:|
| Fill Nulls: Median (spx_ret)  |             0.00227331 |                        0.000280029 |
| Remove Outliers: 3σ (spx_ret) |             0.00222559 |                        0.00445082  |


**Interpretation**:

- When missing values are filled by the median, baseline returns are stable (~0.23%), but     in stress scenarios they nearly vanish (~0.03%).

- After removing outliers (3σ rule), the alternative scenario mean return rises (~0.45%),     suggesting that extreme volatility-driven shocks bias results downward.

**Key Takeaway**:

- Results are sensitive to assumptions about missing data and outlier treatment.

- Conservative assumptions (keeping outliers) highlight downside risk; robust assumptions     (removing extremes) suggest stronger average performance.

## Assumptions & Risks

- **Stationarity**: Relationships between macro indicators and volatility are assumed stable     in the short term. Regime shifts (crises vs calm) may break this.

- **Macro lag**: Macroeconomic indicators update monthly, creating a lag relative to daily market moves.

- **Model risk**: Overfitting to past shocks may reduce predictive accuracy. Bootstrap     resampling is needed to calibrate confidence intervals.

- **Data reliability**: Free data sources (e.g., Yahoo Finance, FRED) may introduce outages or changes.

## Implications for Business Decisions

- **Portfolio Risk Management**: Volatility spikes widen the range of potential outcomes,     reinforcing the need for dynamic hedging and risk alerts.

- **Model Development**: Baseline models should evolve into multivariate frameworks that     include VIX, realized volatility, and macro shocks. Scenario analysis (e.g., rate shock vs neutral) provides     context-specific guidance.

- **Next Steps**: Expand feature set with regime-switching indicators; validate models with     bootstrap confidence intervals to quantify uncertainty; develop dashboard prototypes for weekly updates     with scenario-driven forecasts.
