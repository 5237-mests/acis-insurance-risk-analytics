import pandas as pd

def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.isnull().sum()[df.isnull().sum() > 0].sort_values(ascending=False)

def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    if 'TransactionMonth' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    return df
def drop_useless_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Drop columns that are completely or nearly completely null."""
    df = df.drop(columns=columns, axis=1, errors='ignore')
    return df
def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    original_shape = df.shape
    print(f"📥 Original shape: {original_shape}")

    categorical_cols = [
        'Converted', 'Rebuilt', 'WrittenOff', 'NewVehicle',
        'Bank', 'AccountType', 'Gender', 'MaritalStatus'
    ]
    df[categorical_cols] = df[categorical_cols].fillna('Unknown')

    df['CustomValueEstimate'] = df['CustomValueEstimate'].fillna(0)

    df = df.dropna(subset=[
        'make', 'Model', 'Cylinders', 'cubiccapacity', 'kilowatts',
        'NumberOfDoors', 'VehicleIntroDate', 'mmcode', 'VehicleType', 'bodytype',
        'CapitalOutstanding'
    ])

    new_shape = df.shape
    print(f"✅ Cleaned shape: {new_shape}")
    print(f"🧹 Rows removed during cleaning: {original_shape[0] - new_shape[0]}")
    
    return df
def remove_invalid_premiums(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove records with TotalPremium <= 0.
    These distort financial metrics like loss ratio and margin.
    """
    original = df.shape[0]
    df = df[df['TotalPremium'] > 0]
    removed = original - df.shape[0]
    print(f"🧹 Removed {removed} rows with TotalPremium <= 0")
    return df
