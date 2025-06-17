from src.services.model_inputs import get_claim_probability_data
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

def train_and_evaluate_claim_probability_models(df):
    """
    Train classifiers to predict ClaimMade.
    Prints Accuracy, F1-score, and AUC for each model.
    Returns a dictionary of fitted pipelines.
    """
    X_train, X_test, y_train, y_test, preprocessor = get_claim_probability_data(df)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(max_depth=6, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=50, max_depth=10, n_jobs=-1, random_state=42),
        "XGBoost": XGBClassifier(n_estimators=50, max_depth=6, subsample=0.8, n_jobs=-1, use_label_encoder=False, eval_metric="logloss")
    }

    fitted_pipes = {}

    for name, model in models.items():
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", model)
        ])
        pipe.fit(X_train, y_train)
        preds = pipe.predict(X_test)
        probs = pipe.predict_proba(X_test)[:, 1]  # For AUC

        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds)
        auc = roc_auc_score(y_test, probs)

        print(f"📊 {name}")
        print(f"✅ Accuracy:  {acc:.4f}")
        print(f"✅ F1 Score:  {f1:.4f}")
        print(f"✅ ROC AUC:   {auc:.4f}")
        print("-" * 40)

        fitted_pipes[name] = pipe  # ✅ Store pipeline

    return fitted_pipes
