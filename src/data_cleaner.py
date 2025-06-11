import pandas as pd

def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.isnull().sum()[df.isnull().sum() > 0].sort_values(ascending=False)

def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    if 'TransactionMonth' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    return df
