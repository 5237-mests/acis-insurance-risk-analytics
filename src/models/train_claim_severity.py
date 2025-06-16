from src.services.model_inputs import get_claim_severity_data
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, root_mean_squared_error
import numpy as np

def train_and_evaluate_claim_severity_models(df):
    """
    Train Linear, RF, XGB models to predict TotalClaims on rows where claim > 0.
    Prints RMSE and R² for each model.
    """
    # Load and prepare data
    X_train, X_test, y_train, y_test, preprocessor = get_claim_severity_data(df)

    # Define models
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=100, random_state=42)
    }

    # Train and evaluate each model
    for name, model in models.items():
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("regressor", model)
        ])
        pipe.fit(X_train, y_train)
        preds = pipe.predict(X_test)

        rmse = root_mean_squared_error(y_test, preds)

        r2 = r2_score(y_test, preds)

        print(f"📊 {name}")
        print(f"✅ RMSE: {rmse:.2f}")
        print(f"✅ R²:   {r2:.4f}")
        print("-" * 40)
