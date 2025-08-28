# Model Deployment Reflection

## 1. Credible Failure Modes

1. **Feature Schema Drift**  
   - *Risk*: Changes in data types, missing columns, or new features may break the model.  
   - *Monitoring Metric*: Schema hash comparison; alert if hash differs from baseline.  
   - *Threshold*: Any deviation triggers alert.  
   - *Alert Recipient*: Data Engineering Team.  
   - *Runbook First Step*: Verify incoming data schema and reconcile missing columns.

2. **Increased Null Rates**  
   - *Risk*: Upstream data issues could introduce missing values, reducing prediction accuracy.  
   - *Monitoring Metric*: Percentage of nulls per feature.  
   - *Threshold*: Null rate > 5% for any critical feature.  
   - *Alert Recipient*: Data Owner / Analyst.  
   - *Runbook First Step*: Check source tables and fill or remove nulls; pause downstream predictions if critical.

3. **Model Performance Degradation**  
   - *Risk*: Predictive quality may drop due to concept drift.  
   - *Monitoring Metric*: 2-week rolling RMSE or AUC for validation data.  
   - *Threshold*: RMSE increase > 10% or AUC < 0.60.  
   - *Alert Recipient*: ML Team.  
   - *Runbook First Step*: Compare recent predictions against ground truth; schedule retraining if needed.

4. **System Latency / Failures**  
   - *Risk*: API or batch inference delays can impact business decisions.  
   - *Monitoring Metric*: p95 API latency or job success rate.  
   - *Threshold*: p95 latency > 250ms or < 95% job success.  
   - *Alert Recipient*: Platform On-Call.  
   - *Runbook First Step*: Restart service or batch job; check logs for errors.

5. **Business KPI Deviation**  
   - *Risk*: Model outputs may negatively affect financial metrics (e.g., approval rates, risk exposure).  
   - *Monitoring Metric*: Approval rate or portfolio volatility.  
   - *Threshold*: Deviation > 5% from expected.  
   - *Alert Recipient*: Business Analysts / Product Owner.  
   - *Runbook First Step*: Pause automated decisions; review model outputs with business team.

## 2. Monitoring Layers

- **Data**: Schema hash, null rate, data freshness (max minutes since last batch).  
- **Model**: Rolling RMSE/AUC with 2-week window, PSI on key features > 5%.  
- **System**: p95 latency, job success rate, error logs.  
- **Business**: Approval rate, portfolio volatility, or other relevant KPIs.

## 3. Ownership and Handoffs

- **Data**: Data Engineering Team ensures freshness and integrity.  
- **Model**: ML Team monitors performance; retrains and validates.  
- **System**: Platform On-Call manages deployment uptime and latency.  
- **Business**: Analysts and Product Owners review KPIs.  
- **Handoffs**: Issues logged in Jira/Slack; model retraining requires ML Team approval; dashboard updates coordinated weekly by Analysts.
