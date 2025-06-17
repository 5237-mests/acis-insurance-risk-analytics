from src.services.model_inputs import get_claim_severity_data
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.tree import DecisionTreeRegressor

def train_and_evaluate_claim_severity_models(df):
    """
    Train Linear, Tree, RF, and XGBoost models to predict TotalClaims on rows where claim > 0.
    Prints RMSE and R² for each model.
    Returns a dict of fitted pipelines.
    """
    # Load and prepare data
    X_train, X_test, y_train, y_test, preprocessor = get_claim_severity_data(df)

    # Define models
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=100, random_state=42)
    }

    fitted_pipes = {}

    # Train and evaluate
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

        fitted_pipes[name] = pipe  # ✅ Save the fitted model pipeline

    return fitted_pipes
