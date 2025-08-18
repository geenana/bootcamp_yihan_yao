
## Data Storage 

### Folder Structure 

- **'data/raw/'** → Used for storing raw input data (CSV files) 
- **'data/processed/'** → Used for storing processed data (Parquet files) 

### Formats Used 

- CSV 
    - Used for raw data storage. 
    - Pros: human-readable, ubiquitous, easy diffs in git  
    - Cons: larger files, no schema, type loss (dates/numbers as text)

- Parquet 
    - Used for processed data storage. 
    - Pros: columnar, compressed, preserves types, very fast reads, supports efficient querying 
    (column pruning, predicate pushdown)
    - Cons: binary format, requires an engine (pyarrow/fastparquet)

### Reads/Writes 

- CSV files → wwritten with pandas.DataFrame.to_csv and read with pandas.read_csv 
- Parquet files → written with pandas.DataFrame.to_parquet and read with pandas.read_parquet 

File paths are automatically created based on environment variables defined in the '.env' file 
(DATA_DIR_RAW and DATA_DIR_PROCESSED). 

### Validation Checks 

After reloading data, the following validations are applied: 
- Shape check → ensures the reloaded DataFrame has the same shape as the original 
- Date type check → confirms that the date column is parsed as datatime64 
- Price type check → confirms that the price column is numeric 
