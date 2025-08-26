# Model Report

## Executive Summary

- **Objective**: Translate model results into decisions; expose assumptions and sensitivity.

## Charts with Interpretation

Below are the key charts from the analysis:

![](../deliverables/images/risk_return.png)

*Chart 1: Risk-Return by Scenario*

→ The chart is a scatter plot showing volatility in x-axis and return in y-axis. The volatility of the     outliers removing method, which is about 0.19, is the highest; but the return of it is also the highest, which is     about 0.135. The imputation by mean method has middle volatility and the lowest return. It assumes missing data are     not systematically biased.

![](../deliverables/images/return_by_scenario.png)

*Chart 2: Return by Scenario*

→ The chart is a bar plot comparing returns of different scenarios. The outlier removing method has the     highest return, which is 0.135; the baseline has the second highest return, which is 0.12; and the imputation by mean     method has the lowest return, which is 0.11. This confirms the model is sensitive to data treatment choices. It assumes     that stability of results depends on data quality and standardize preprocessing is needed to avoid inconsistent outcomes.

![](../deliverables/images/metricA_over_time.png)

*Chart 3: MetricA Over Time by Category*

→ The chart is a line chart, though because of limited data, it only shows dots there. It compared     MetricA over time across scenarios. MetricA rises for category Y (about 67) and rises more for category X (about 72)     as time goes by.

## Assumptions & Risks

- Assumes missing data are random and not systematically biased.

- Assumes extreme outliers represent noise rather than meaningful stress events.

- Results sensitive to preprocessing; careless choices can materially change outcomes.

## Sensitivity Summary

| Assumption          |   Baseline Return |   Alt Scenario Return |
|:--------------------|------------------:|----------------------:|
| Fill Nulls: Median  |              0.12 |                  0.1  |
| Remove Outliers: 3σ |              0.12 |                  0.14 |


**Interpretation:**

- Median imputation slightly lowers return (0.12 → 0.10).

- Outlier removal improves return (0.12 → 0.14).

## Decision Implications

- Use median imputation for reliability.

- Outlier removal helps, but balance risk of discarding stress data.

- Model results shift with data assumptions, so governance on preprocessing is     essential before production use.
