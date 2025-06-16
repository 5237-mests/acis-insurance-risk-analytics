# 📊 Task 3 Report – A/B Hypothesis Testing

## Project: Insurance Risk Analytics

**Analyst:** Mesfin Mulugeta
**Date:** June 2025

---

## 🎯 Objective

The objective of this task is to validate whether key customer, geographic, and policy attributes influence insurance **risk** and **profitability**. The KPIs evaluated include:

- **Claim Frequency**: Proportion of policies that had at least one claim
- **Claim Severity**: Average claim amount for customers who submitted claims
- **Margin**: Profit per policy (TotalPremium - TotalClaims)

We tested four null hypotheses (H₀) using Welch’s t-test at a 5% significance level (α = 0.05).

---

## ✅ Results Summary

| Hypothesis                                       | Metric          | Test Used  | Groups                   | p-value  | Decision             | Interpretation                                         |
| ------------------------------------------------ | --------------- | ---------- | ------------------------ | -------- | -------------------- | ------------------------------------------------------ |
| **H₀₁** No risk difference across provinces      | Claim Severity  | T-Test     | Gauteng vs KwaZulu-Natal | 0.0012   | ❌ Reject H₀         | Provinces differ significantly in avg. claim amount    |
| H₀₁ (Extended)                                   | Claim Severity  | ANOVA      | All 9 provinces          | 1.09e-05 | ❌ Reject H₀         | Strong evidence of regional claim severity differences |
| **H₀₂** No risk difference between zip codes     | Claim Frequency | T-Test     | Zip 2000 vs 122          | 0.0030   | ❌ Reject H₀         | Zip codes influence claim frequency                    |
| H₀₂ (Extended)                                   | Claim Frequency | Chi-square | Top 10 zip codes         | 8.69e-08 | ❌ Reject H₀         | Clear association between zip and claim behavior       |
| **H₀₃** No margin difference between zip codes   | Margin          | T-Test     | Zip 2000 vs 122          | 0.5226   | ✅ Fail to Reject H₀ | No margin difference found                             |
| H₀₃ (Extended)                                   | Margin          | ANOVA      | Top 10 zip codes         | 0.4842   | ✅ Fail to Reject H₀ | Margin remains stable across zip codes                 |
| **H₀₄** No risk difference between women and men | Claim Frequency | T-Test     | Male vs Female           | 0.5847   | ✅ Fail to Reject H₀ | No gender-based risk difference                        |

---

## 🔍 Detailed Analysis

### 🧪 H₀₁: Province vs Claim Severity

- Compared: **Gauteng** vs **KwaZulu-Natal**
- **p = 0.0012** → Statistically significant
- ✔ Claim amounts vary significantly by province
- **Implication:** Region should be a pricing and risk factor in underwriting models

---

### 🧪 H₀₂: Zip Code vs Claim Frequency

- Compared: Postal codes **2000** vs **122**
- **p = 0.0030** → Statistically significant
- ✔ Zip code location affects how often customers file claims
- **Implication:** Use geolocation to improve fraud detection or premium segmentation

---

### 🧪 H₀₃: Zip Code vs Margin

- Compared: Same top two zip codes
- **p = 0.5226** → Not statistically significant
- ✘ No difference in profit margin between these areas
- **Implication:** Premium calculations might already account for this risk

---

### 🧪 H₀₄: Gender vs Claim Frequency

- Compared: **Male** vs **Female**
- **p = 0.5847** → Not statistically significant
- ✘ Gender is not a meaningful predictor of claim behavior
- **Implication:** Avoid using gender in pricing or decision systems to maintain fairness

---

## 🔍 Interpretation

- ✅ **Provinces** influence **claim severity** → location is a key underwriting factor
- ✅ **Zip codes** significantly affect **claim frequency** → localized risk modeling is needed
- ❌ **Margin** does not vary significantly across top zip codes → pricing seems balanced
- ❌ **Gender** has no impact on claim likelihood → do not use gender in risk scoring

---

## 🧠 Business Recommendations

- 🎯 Incorporate **province** and **zipcode** into pricing and risk segmentation models
- 🚫 Avoid using **gender** in pricing — no evidence of predictive power
- 💡 Further explore margin stability — may reflect strong pricing policy
- 📈 Consider building **zip-level risk profiles** for fraud detection and personalized marketing

---
