import pandas as pd
from src.services.ab_testing import (
    test_gender_difference,
    test_province_difference,
    test_zipcode_margin_difference,
    test_zipcode_risk_difference
)

def load_sample_data():
    return pd.read_csv("data/processed/cleaned_insurance_data.csv")

def test_gender():
    df = load_sample_data()
    result = test_gender_difference(df)
    assert "p_value" in result

def test_province():
    df = load_sample_data()
    result = test_province_difference(df)
    assert "p_value" in result

def test_zipcode_margin():
    df = load_sample_data()
    result = test_zipcode_margin_difference(df)
    assert "p_value" in result

def test_zipcode_risk():
    df = load_sample_data()
    result = test_zipcode_risk_difference(df)
    assert "p_value" in result
