
## Data Cleaning Strategy

### Overview
This project uses a raw dataset located in `data/raw/` and applies a series of cleaning steps to prepare it for analysis. The cleaned dataset is saved to `data/processed/`. All data cleaning operations are implemented in `src/cleaning.py`.

---

### Cleaning Functions

1. **`fill_missing_median(df, columns=None)`**
   - Fills missing values (`NaN`) in numeric columns with the **median** of each column.
   - If `columns` is not specified, all numeric columns are filled.
   - **Assumption:** Missing values in numeric columns are missing at random (MAR/MCAR) and can be reasonably imputed using the median.

2. **`drop_missing(df, columns=None, threshold=None)`**
   - Drops rows based on missingness criteria:
     - If `columns` is provided: drops rows with missing values in these columns.
     - If `threshold` is provided: drops rows with fewer than `threshold * total_columns` non-missing values.
     - If neither is provided: drops rows with any missing values.
   - **Assumption:** Rows with insufficient data are less informative and can be removed without biasing the dataset.

3. **`normalize_data(df, columns=None, method='minmax')`**
   - Scales numeric columns for analysis or machine learning:
     - `'minmax'`: rescales values to the `[0, 1]` range.
     - `'standard'`: standardizes values to have mean 0 and standard deviation 1.
   - If `columns` is not specified, all numeric columns are scaled.
   - **Assumption:** Features with vastly different ranges need normalization to improve comparability and algorithm performance.
