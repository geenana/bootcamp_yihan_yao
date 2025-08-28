# Orchestration Plan — SPX Volatility Prediction Project

## 1. Project Jobs/Tasks

| Task Name                  | Description |
|-----------------------------|-------------|
| ingest_data                 | Download or load raw SPX, VIX, realized volatility, and macroeconomic data. |
| clean_data                  | Clean data, handle missing values, engineer features (RV 21-day, VRP ratio, etc.). |
| train_model                 | Train regression model on cleaned features to predict SPX returns. |
| save_model                  | Save the trained model as a serialized artifact (`.pkl`). |
| run_flask_api               | Start Flask API to serve `/predict` and `/plot` endpoints. |
| run_streamlit_dashboard     | Launch interactive Streamlit dashboard for user input and prediction display. |
| generate_report             | Generate analysis report with summary statistics and example plots. |

---

## 2. Task Order & Dependencies (DAG)

ingest_data → clean_data → train_model → save_model → run_flask_api → run_streamlit_dashboard → generate_report

- `generate_report` also depends on `clean_data` for input features.  
- Both dashboards (`Flask` and `Streamlit`) depend on the saved model.

---

## 3. Inputs & Outputs

| Task Name              | Inputs                                      | Outputs                                  |
|------------------------|--------------------------------------------|-----------------------------------------|
| ingest_data             | `/data/raw_market.csv`                     | `data/raw_market.csv`                    |
| clean_data              | `data/raw_market.csv`                      | `data/cleaned_data.csv`                  |
| train_model             | `data/cleaned_data.csv`                    | `trained_model.pkl`                       |
| save_model              | `trained_model.pkl`                        | `trained_model.pkl`                       |
| run_flask_api           | `trained_model.pkl`                        | `flask_api_running.txt`                  |
| run_streamlit_dashboard | `trained_model.pkl`                        | `streamlit_dashboard_running.txt`        |
| generate_report         | `trained_model.pkl`, `data/cleaned_data.csv` | `analysis_report.pdf`                    |

---

## 4. Logging & Checkpoint Strategy

| Task Name              | Log Messages                                           | Checkpoint Artifact                     |
|------------------------|-------------------------------------------------------|----------------------------------------|
| ingest_data             | start/end, rows downloaded, source URI               | `raw_market.csv`                        |
| clean_data              | start/end, rows in/out, null counts, schema check    | `cleaned_data.csv`                      |
| train_model             | start/end, hyperparameters, metrics (R², RMSE)      | `trained_model.pkl`                     |
| save_model              | start/end, model path, file size                     | `trained_model.pkl`                     |
| run_flask_api           | start/end, request count, errors                     | `flask_api_running.txt`                 |
| run_streamlit_dashboard | start/end, user interactions                          | `streamlit_dashboard_running.txt`       |
| generate_report         | start/end, paths of generated plots and tables      | `analysis_report.pdf`                   |

---

## 5. Automation vs Manual Tasks

### Automated

- **Data ingestion**: scheduled downloads to ensure freshness.  
- **Data cleaning & feature engineering**: deterministic transformations.  
- **Model training & saving**: triggered by defined events or schedules.  
- **API and dashboard launches**: reproducible tasks via CLI/scripts.

### Manual

- **Model evaluation & interpretation**: Analysts review residuals, R², and RMSE.  
- **Business KPI monitoring & decision making**: requires domain judgment.  
- **Report generation & insights communication**: review and summarization require human interpretation.

**Rationale:** Automation focuses on repetitive, deterministic steps to reduce errors and save time. Manual work is reserved for tasks requiring judgment, domain expertise, or contextual decision-making.
