import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load pipe-delimited .txt data into a DataFrame."""
    try:
        df = pd.read_csv(filepath, delimiter="|", low_memory=False)
        print(f"✅ Loaded data with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        raise
