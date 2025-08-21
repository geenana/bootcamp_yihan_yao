
import pandas as pd
import re

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean column names by:
    - Lowercasing
    - Replacing spaces with underscores
    - Removing special characters
    """
    df_copy = df.copy()
    df_copy.columns = [
        re.sub(r'[^0-9a-zA-Z_$]', '', col.strip().lower().replace(" ", "_"))
        for col in df_copy.columns
    ]
    return df_copy


def parse_dates(df: pd.DataFrame, columns) -> pd.DataFrame:
    """
    Parse specified columns into datetime format.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    columns : list
        List of column names to parse as datetime

    Returns
    -------
    pd.DataFrame
        Copy of df with parsed datetime columns
    """
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = pd.to_datetime(df_copy[col], errors='coerce')
    return df_copy
