import pandas as pd

def describe_numerical(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()

def compute_loss_ratio(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Avoid division by zero
    df = df[df['TotalPremium'] != 0]

    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    result = df.groupby(['Province', 'VehicleType', 'Gender'])['LossRatio'].mean().reset_index()
    
    return result.sort_values(by='LossRatio', ascending=False)
def claims_over_time(df):
    df = df.copy()
    monthly = df.groupby(df['TransactionMonth'].dt.to_period('M')).agg({
        'TotalClaims': ['sum', 'count', 'mean'],
        'TotalPremium': 'sum'
    }).reset_index()
    monthly.columns = ['Month', 'ClaimsSum', 'ClaimsCount', 'ClaimsAvg', 'PremiumSum']
    return monthly
def claims_by_vehicle_type(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    vehicle_claims = df.groupby('VehicleType').agg({
        'TotalClaims': 'sum',
        'TotalPremium': 'sum'
    }).reset_index()
    vehicle_claims['LossRatio'] = vehicle_claims['TotalClaims'] / vehicle_claims['TotalPremium']
    return vehicle_claims.sort_values(by='LossRatio', ascending=False)
def top_models_by_claims(df, top_n=10):
    return df.groupby(['make', 'Model'])['TotalClaims'].mean().sort_values(ascending=False).head(top_n).reset_index()

def bottom_models_by_claims(df, bottom_n=10):
    return df.groupby(['make', 'Model'])['TotalClaims'].mean().sort_values(ascending=True).head(bottom_n).reset_index()
