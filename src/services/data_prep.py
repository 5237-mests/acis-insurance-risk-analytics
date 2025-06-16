import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Define useful modeling columns
USEFUL_COLUMNS = [
    "IsVATRegistered", "LegalType", "MaritalStatus", "Gender", "Province", "PostalCode",
    "MainCrestaZone", "SubCrestaZone", "ItemType", "VehicleType", "RegistrationYear",
    "make", "Model", "Cylinders", "cubiccapacity", "kilowatts", "bodytype", "NumberOfDoors",
    "CustomValueEstimate", "SumInsured", "CalculatedPremiumPerTerm", "TotalPremium", "TotalClaims"
]

def prepare_model_data(
    df: pd.DataFrame,
    target: str,
    dropna_cols=None,
    categorical_cols=None,
    test_size: float = 0.2,
    random_state: int = 42
):
    """
    Prepare dataset for ML modeling:
    - Keeps only relevant columns
    - Filters out rows with missing targets
    - Encodes categorical variables
    - Returns clean train/test splits and a pipeline preprocessor
    """
    df = df.copy()

    # Add engineered columns BEFORE column filtering
    df["ClaimMade"] = (df["TotalClaims"] > 0).astype(int)
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    # Now drop to useful columns (which includes engineered ones)
    columns_to_keep = USEFUL_COLUMNS + [target, "ClaimMade", "Margin"]
    df = df[[col for col in columns_to_keep if col in df.columns]]

    #  ensure no duplicate columns
    df = df.loc[:, ~df.columns.duplicated()]

    # Drop rows where the target or required columns are missing
    df = df[df[target].notna()]
    if dropna_cols:
        df = df.dropna(subset=dropna_cols)

    # Split into features and target
    X = df.drop(columns=[target])
    y = df[target]

    # Detect categorical columns
    if categorical_cols is None:
        categorical_cols = X.select_dtypes(include="object").columns.tolist()
    numeric_cols = X.select_dtypes(include=["int64", "float64", "bool"]).columns.tolist()

    # Preprocessing pipeline
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="mean"))
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])
    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, numeric_cols),
        ("cat", categorical_pipeline, categorical_cols)
    ])

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test, preprocessor
