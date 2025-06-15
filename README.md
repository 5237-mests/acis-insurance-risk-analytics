
# 🚗 Insurance Risk Analytics & Predictive Modeling

This project is part of a data analytics pipeline to support decision-making in the insurance domain. The goal is to analyze historical claim and policy data to identify risk patterns, optimize pricing strategies, and prepare for downstream machine learning modeling.

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

## ✅ Completed Tasks

### 📊 Task 1: Exploratory Data Analysis (EDA)

- Cleaned and preprocessed dataset (handled nulls, outliers, invalid premiums/claims)
- Performed univariate, bivariate, and multivariate analysis
- Generated visualizations for:
  - Distributions and outliers
  - Loss ratios by region and vehicle
  - Claims over time
  - Correlation heatmap of financial metrics
- Documented findings in `eda_summary.md` and `interim_report.md`

### 🔁 Task 2: Data Version Control with DVC

- Initialized DVC and tracked raw dataset
- Configured local remote storage
- Pushed `.dvc` metadata and set up project reproducibility

---

## 🔬 In Progress

### 🧪 Task 3: A/B Hypothesis Testing

- Implemented hypothesis testing functions for:
  - Gender vs claim frequency
  - Province vs severity
  - Zipcode vs margin and risk
- Currently analyzing results and writing business recommendations

---

## 🔜 Upcoming

### 🤖 Task 4: Modeling & Predictive Analytics

- Prepare dataset for training
- Build models for claim severity and premium estimation
- Evaluate with RMSE and interpret using SHAP/LIME
- Document insights and recommendations

---

## 🧠 Team & Tools

- Python, Pandas, Seaborn, Matplotlib
- DVC for data versioning
- Pytest for unit tests
- GitHub Actions for CI

---

*This README will be updated after Task 4 completion to include final results and model documentation.*
