
# Utility Functions Documentation

This document explains the helper functions provided in `src/utils.py`.  

---

## 1. `clean_column_names(df)`

**Purpose:**  
Cleans column names in a Pandas DataFrame by removing unwanted characters and standardizing formatting.

**Implementation:**
- Converts all column names to lowercase.
- Removes characters that are not letters, numbers, underscores `_`, or dollar signs `$`.
- Replaces spaces with underscores for consistency.

**Future Uses:**
- Ensuring column names are valid Python identifiers.  
- Preparing datasets for machine learning pipelines where standardized column naming reduces preprocessing errors. 
- Keeping special finance-related characters like $ for monetary columns. 

## 2. `parse_dates(df, columns)`

**Purpose:**
Converts specified columns in a DataFrame to datetime objects. 

**Implementation:**
- Takes in a DataFrame and a list of column names to parse. 
- Uses pd.to_datetime() to convert values into datetime. 

**Future Uses:**
- Standardizing messy date formats across multiple data sources. 
- Ensuring temporal features are ready for time-series modeling. 
