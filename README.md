# 🚗 Insurance Risk Analytics & Predictive Modeling

This project explores risk modeling and premium optimization for ACIS, an auto insurance provider. Using real-world customer, vehicle, and claims data, we applied machine learning and statistical analysis to better understand risk and improve pricing strategy.

---

## 📦 Project Structure

```
.
├── data/                # Raw and processed datasets
├── src/                 # Core logic (cleaning, visualization, testing)
├── notebooks/           # Jupyter notebooks for exploration and analysis
├── tests/               # Unit and integration tests
├── scripts/             # CLI or automation scripts
├── .github/             # CI/CD configuration
├── dvc_storage/         # Local DVC remote (not versioned by git)
├── config/              # App and environment configs
├── docs/                # Documentation and markdown reports
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project metadata and linting configs
└── README.md
```

---

## 🧪 Tasks Completed

1. **EDA** – Explored missing data, value distributions, and relationships
2. **Data Version Control** – Modular pipeline with DVC-tracked steps
3. **Hypothesis Testing** – Statistical tests across gender, geography, and claims
4. **Modeling** – Predictive modeling of:
   - Claim severity (regression)
   - Premium (regression)
   - Claim occurrence (classification)
5. **Model Explainability** – SHAP-based insights at global and local level

---

## 🧠 Team & Tools

- Python, Pandas, Seaborn, Matplotlib
- DVC for data versioning
- Pytest for unit tests
- GitHub Actions for CI

---

_This README will be updated after Task 4 completion to include final results and model documentation._

Absolutely, Mesfin. Here's your **final polished `README.md`** that combines:

- Your project structure
- All modeling insights
- SHAP interpretation
- Final recommendations
- Clean, professional tone for GitHub or Medium

---

# 🚗 ACIS Insurance Risk Analytics

This project explores risk modeling and premium optimization for ACIS, an auto insurance provider. Using real-world customer, vehicle, and claims data, we applied machine learning and statistical analysis to better understand risk and improve pricing strategy.

---

```

---


## 📊 Model Performance Summary

### 🎯 Claim Severity Prediction (`TotalClaims` > 0)

| Model               | RMSE     | R²     |
|--------------------|----------|--------|
| Linear Regression  | **0.28** | 1.0000 |
| Decision Tree      | 924.49   | 0.9994 |
| Random Forest      | 703.46   | 0.9997 |
| XGBoost            | 3817.73  | 0.9900 |

> ⚠️ Linear regression's perfect score suggests leakage via features like `Margin`.

---

### 💰 Premium Prediction (`CalculatedPremiumPerTerm`)

| Model               | RMSE     | R²     |
|--------------------|----------|--------|
| Linear Regression  | 39.69    | 0.9678 |
| Decision Tree      | 22.92    | 0.9893 |
| Random Forest      | **22.77**| 0.9894 |
| XGBoost            | 25.83    | 0.9864 |

> ✅ Random Forest performed best, capturing non-linear premium dynamics.

---

### 🧾 Claim Occurrence Classification (`ClaimMade`)

| Model               | Accuracy | F1     | AUC    |
|--------------------|----------|--------|--------|
| Logistic Regression| 1.0000   | 1.0000 | 1.0000 |
| Decision Tree      | 1.0000   | 1.0000 | 1.0000 |
| Random Forest      | 0.9999   | 0.9920 | 1.0000 |
| XGBoost            | 1.0000   | 1.0000 | 1.0000 |

> 🚨 Extremely high scores → possible data leakage (investigated using SHAP).

---

## 🧠 SHAP Interpretability

### 🔍 Global Insights:
- `Margin`, `SumInsured`, and vehicle-related features (e.g., `cubiccapacity`, `make`, `bodytype`) were top drivers of claim severity and premium.
- Province and ZipCode also impacted predictions significantly.

### 🔬 Local Insights:
- SHAP waterfall plots helped explain why a given user received a high predicted claim value.
- Features had directional impacts (e.g., `Province=Gauteng` may increase claim risk).

---

## 💡 Recommendations for ACIS

✅ **Use risk-based premium formula**:
*Premium = Predicted Probability × Claim Severity + Loadings*

✅ **Adjust for geographic risk**:
Implement province/zipcode-based pricing strategies.

✅ **Reward low-risk segments**:
Discounts for safer vehicles, tracking devices, or loyal policyholders.

✅ **Avoid target leakage**:
Drop or recalculate synthetic variables like `Margin` in production pipelines.

✅ **Monitor with SHAP**:
Use global + local SHAP outputs to validate model fairness and transparency.

---

## ⚠️ Limitations & Future Enhancements

- **Target leakage** needs strict feature filtering
- **Temporal factors** (e.g., inflation, seasonality) not yet modeled
- Opportunity for **external data enrichment** (e.g., weather, crime rates)
- Future models could incorporate **cost-sensitive learning**

---

## 📅 Submission

**Author:** Mesfin Mulugeta
**Institution:** 10 Academy
**Submission Date:** June 17, 2025 – 8:00 PM UTC

```
