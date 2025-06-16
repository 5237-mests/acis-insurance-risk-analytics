from src.services.data_prep import prepare_model_data

def get_claim_severity_data(df):
    """
    Prepare data for Claim Severity Prediction (Regression)
    Filters rows with TotalClaims > 0
    """
    df = df.copy()
    df = df[df["TotalClaims"] > 0]
    df = df.drop(columns=["UnderwrittenCoverID", "PolicyID", "TransactionMonth"], errors="ignore")

    return prepare_model_data(
        df=df,
        target="TotalClaims",
        dropna_cols=["TotalPremium", "CalculatedPremiumPerTerm", "SumInsured"]
    )

def get_premium_prediction_data(df):
    """
    Prepare data for Premium Prediction (Regression)
    """
    df = df.copy()
    df = df[df["CalculatedPremiumPerTerm"] > 0]
    df = df.drop(columns=["UnderwrittenCoverID", "PolicyID", "TransactionMonth"], errors="ignore")

    return prepare_model_data(
        df=df,
        target="CalculatedPremiumPerTerm",
        dropna_cols=["TotalClaims", "SumInsured"]
    )

def get_claim_probability_data(df):
    """
    Prepare data for Claim Probability Classification (Binary)
    """
    df = df.copy()
    df = df.drop(columns=["UnderwrittenCoverID", "PolicyID", "TransactionMonth"], errors="ignore")

    return prepare_model_data(
        df=df,
        target="ClaimMade",
        dropna_cols=["TotalPremium", "CalculatedPremiumPerTerm", "SumInsured"]
    )
