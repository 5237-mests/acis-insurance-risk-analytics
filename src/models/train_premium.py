from sklearn.metrics import root_mean_squared_error, r2_score
from src.services.model_inputs import get_premium_prediction_data
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def train_and_evaluate_premium_models(df):
    """
    Train regression models to predict CalculatedPremiumPerTerm.
    Prints RMSE and R² for each model.
    Returns a dictionary of fitted pipelines for interpretation.
    """
    X_train, X_test, y_train, y_test, preprocessor = get_premium_prediction_data(df)

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=50, max_depth=10, n_jobs=-1, random_state=42),
        "XGBoost": XGBRegressor(n_estimators=50, max_depth=6, subsample=0.8, n_jobs=-1, random_state=42)
    }

    fitted_pipes = {}

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

        fitted_pipes[name] = pipe  # ✅ Save the model

    return fitted_pipes
# Return the fitted pipelines for further use