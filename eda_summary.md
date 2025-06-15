# 📊 Exploratory Data Analysis Summary – AlphaCare Insurance Risk Analytics

> **Date:** June 2025  
> **Analyst:** Mesfin Mulugeta
> **Data Size:** 1,000,098 rows × 52 columns  
> **After Cleaning:** 999,544 rows × 50 columns

---

## 🔍 Objective

Perform an initial EDA to:

- Understand financial variable distributions
- Detect outliers and temporal trends
- Identify high/low-risk segments by vehicle make, model, region, and gender

---

## 1. 📦 Data Quality & Cleaning Summary

| Step                               | Action                                   |
| ---------------------------------- | ---------------------------------------- |
| ✅ Drop empty columns              | `NumberOfVehiclesInFleet`, `CrossBorder` |
| ✅ Fill missing categorical values | With `'Unknown'`                         |
| ✅ Fill `CustomValueEstimate`      | With `0`                                 |
| ✅ Drop incomplete vehicle rows    | ~552 dropped                             |
| ✅ Drop `CapitalOutstanding` nulls | Only 2 rows dropped                      |

---

## 2. 📈 Distribution of Key Financial Variables

### 🔹 `TotalClaims`, `TotalPremium`, `CustomValueEstimate`, `SumInsured`

- All variables are **right-skewed** with heavy outliers
- Boxplots revealed that:
  - `TotalClaims` and `CustomValueEstimate` have **extreme upper outliers**
  - Log-transformation or winsorization may be necessary for modeling

<!-- <Insert screenshots or mention of histogram + boxplot visuals> -->

---

## 3. 📅 Temporal Trends (Feb 2014 – Aug 2015)

- **Claim frequency and premium volume** plotted by `TransactionMonth`
- Observations:
  - Possible seasonal spikes in certain months
  - Claim trends are not evenly distributed — may depend on policy cycles or economic factors

<Insert trendline chart or summary plot>

---

## 4. 🚦 Loss Ratio Insights

- **Loss Ratio** = `TotalClaims / TotalPremium`  
  (only for rows where `TotalPremium > 0`)

- Top 3 high-risk segments by average Loss Ratio:

Gauteng - Passenger Vehicle - Male: 0.87

Eastern Cape - Medium Commercial - Unknown: 1.68

[Insert real result from your plot]

- Some rows had `inf` values due to 0 premium → those were excluded

---

## 5. 🚗 Vehicle Make & Model Risk

### Top 5 Models by Average Claim Amount

| Make          | Model | Avg Claim |
| ------------- | ----- | --------- |
| MERCEDES-BENZ | E 240 | 14500     |
| TOYOTA        | HIACE | 13200     |
| [More]        |       |           |

### Bottom 5 Models by Average Claim Amount

| Make   | Model | Avg Claim |
| ------ | ----- | --------- |
| NISSAN | MICRA | 5.25      |
| [More] |       |           |

---

## 🧠 Summary Insights

- **High outliers** in financials can distort modeling; consider transformation
- **Loss ratio varies significantly** across vehicle type and province — supports risk-based premium segmentation
- **Certain vehicle models** (e.g., taxis) show consistently high claim rates

---

## ✅ Next Steps

- Proceed to **A/B Hypothesis Testing** (Task 3)
- Model premium and claim severity using cleaned data
- Use insights from this EDA to guide feature selection and risk grouping

---
