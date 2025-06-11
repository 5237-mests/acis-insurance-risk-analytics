import pandas as pd

def describe_numerical(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()

def compute_loss_ratio(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    return df.groupby(['Province', 'VehicleType', 'Gender'])['LossRatio'].mean().reset_index()
