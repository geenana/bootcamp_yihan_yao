import pandas as pd 

def get_summary_stats(df):
    print(df.describe())
    print()
    summary = df.groupby('category').mean(numeric_only=True).reset_index()
    print(summary)