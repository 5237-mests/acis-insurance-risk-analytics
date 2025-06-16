import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency
# ----------------------------------
# 🧮 Metric Calculations
# ----------------------------------

def claim_frequency(df: pd.DataFrame) -> pd.DataFrame:
    """Add claim frequency column (1 if TotalClaims > 0)."""
    df = df.copy()
    df["ClaimMade"] = df["TotalClaims"] > 0
    return df


def claim_severity(df: pd.DataFrame) -> pd.DataFrame:
    """Filter only rows with claims and calculate severity."""
    df = df[df["TotalClaims"] > 0].copy()
    return df


def calculate_margin(df: pd.DataFrame) -> pd.DataFrame:
    """Add margin column (TotalPremium - TotalClaims)."""
    df = df.copy()
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    return df

# ----------------------------------
# 📊 Hypothesis Testing
# ----------------------------------

def run_ttest(group_a: pd.Series, group_b: pd.Series) -> dict:
    """Perform Welch’s t-test and return result."""
    t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False, nan_policy='omit')
    return {
        "t_statistic": t_stat,
        "p_value": p_value,
        "reject_null": p_value < 0.05,
        "n_A": len(group_a),
        "n_B": len(group_b)
    }

# ----------------------------------
# 🧪 Gender Risk Difference Test
# ----------------------------------

def test_gender_difference(df: pd.DataFrame) -> dict:
    """
    H₀: There is no risk difference between Women and Men.
    Risk = Claim Frequency
    """
    df = claim_frequency(df)
    df = df[df["Gender"].isin(["Male", "Female"])]

    male_freq = df[df["Gender"] == "Male"]["ClaimMade"].astype(int)
    female_freq = df[df["Gender"] == "Female"]["ClaimMade"].astype(int)

    result = run_ttest(male_freq, female_freq)
    result["test"] = "Gender vs Claim Frequency"
    result["group_A"] = "Male"
    result["group_B"] = "Female"

    return result

# ----------------------------------
# 🧪 Province Risk Difference Test
# ----------------------------------

def test_province_difference(df: pd.DataFrame) -> dict:
    """
    H₀: There is no claim severity difference across provinces.
    """
    df = claim_severity(df)
    # Use the top 2 provinces by row count
    top_provinces = df['Province'].value_counts().nlargest(2).index
    df = df[df['Province'].isin(top_provinces)]

    group_a = df[df["Province"] == top_provinces[0]]["TotalClaims"]
    group_b = df[df["Province"] == top_provinces[1]]["TotalClaims"]

    result = run_ttest(group_a, group_b)
    result["test"] = "Province vs Claim Severity"
    result["group_A"] = top_provinces[0]
    result["group_B"] = top_provinces[1]

    return result


# ----------------------------------
# 🧪 Zip Code Margin Difference Test
# ----------------------------------

def test_zipcode_margin_difference(df: pd.DataFrame) -> dict:
    """
    H₀: There is no margin difference between zip codes.
    """
    df = calculate_margin(df)
    top_zips = df['PostalCode'].value_counts().nlargest(2).index
    df = df[df['PostalCode'].isin(top_zips)]

    group_a = df[df["PostalCode"] == top_zips[0]]["Margin"]
    group_b = df[df["PostalCode"] == top_zips[1]]["Margin"]

    result = run_ttest(group_a, group_b)
    result["test"] = "Zipcode vs Margin"
    result["group_A"] = str(top_zips[0])
    result["group_B"] = str(top_zips[1])

    return result


# ----------------------------------
# 🧪 Zip Code Risk Difference Test
# ----------------------------------

def test_zipcode_risk_difference(df: pd.DataFrame) -> dict:
    """
    H₀: There is no risk difference between zip codes.
    Risk = Claim Frequency
    """
    df = claim_frequency(df)
    top_zips = df['PostalCode'].value_counts().nlargest(2).index
    df = df[df['PostalCode'].isin(top_zips)]

    group_a = df[df["PostalCode"] == top_zips[0]]["ClaimMade"].astype(int)
    group_b = df[df["PostalCode"] == top_zips[1]]["ClaimMade"].astype(int)

    result = run_ttest(group_a, group_b)
    result["test"] = "Zipcode vs Claim Frequency"
    result["group_A"] = str(top_zips[0])
    result["group_B"] = str(top_zips[1])

    return result


# ----------------------
# ANOVA: Province vs Severity
# ----------------------
def province_claim_severity_anova(df: pd.DataFrame) -> dict:
    """
    H₀: No difference in claim severity across all provinces.
    """
    df = df[df["TotalClaims"] > 0].copy()
    df = df[df["Province"].notna()]

    grouped = [group["TotalClaims"].dropna() for _, group in df.groupby("Province")]
    f_stat, p_value = stats.f_oneway(*grouped)

    return {
        "test": "ANOVA: Province vs Claim Severity",
        "p_value": p_value,
        "reject_null": p_value < 0.05,
        "num_groups": len(grouped)
    }


# ----------------------
# ANOVA: Zip Code vs Margin
# ----------------------
def zipcode_margin_anova(df: pd.DataFrame) -> dict:
    """
    H₀: No difference in margin across all zip codes.
    """
    df = df.copy()
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    df = df[df["PostalCode"].notna()]

    top_zipcodes = df["PostalCode"].value_counts().nlargest(10).index
    df = df[df["PostalCode"].isin(top_zipcodes)]

    grouped = [group["Margin"].dropna() for _, group in df.groupby("PostalCode")]
    f_stat, p_value = stats.f_oneway(*grouped)

    return {
        "test": "ANOVA: Zip Code vs Margin",
        "p_value": p_value,
        "reject_null": p_value < 0.05,
        "num_groups": len(grouped)
    }


# ----------------------
# Chi-Square: Zip Code vs ClaimMade
# ----------------------
def zipcode_claim_frequency_chisq(df: pd.DataFrame) -> dict:
    """
    H₀: No difference in claim frequency across zip codes.
    """
    df = df.copy()
    df["ClaimMade"] = (df["TotalClaims"] > 0).astype(int)

    top_zipcodes = df["PostalCode"].value_counts().nlargest(10).index
    df = df[df["PostalCode"].isin(top_zipcodes)]

    contingency = pd.crosstab(df["PostalCode"], df["ClaimMade"])
    chi2, p_value, dof, expected = chi2_contingency(contingency)

    return {
        "test": "Chi-square: Zip Code vs Claim Frequency",
        "p_value": p_value,
        "reject_null": p_value < 0.05,
        "num_groups": contingency.shape[0]
    }
