import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_analyzer import bottom_models_by_claims, claims_over_time, top_models_by_claims

def plot_hist(df: pd.DataFrame, column: str):
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def plot_box(df: pd.DataFrame, column: str):
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot of {column}')
    plt.show()

def plot_correlation(df: pd.DataFrame):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
def plot_hist_and_box(df, column):
    """Plot histogram and boxplot side by side."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    sns.histplot(df[column].dropna(), kde=True, ax=axes[0])
    axes[0].set_title(f"Distribution of {column}")
    
    sns.boxplot(x=df[column].dropna(), ax=axes[1])
    axes[1].set_title(f"Boxplot of {column}")
    
    plt.tight_layout()
    plt.show()
def plot_loss_ratio(df: pd.DataFrame):
    """Plot the loss ratio by Province, VehicleType, and Gender."""
    loss_ratio = df.groupby(['Province', 'VehicleType', 'Gender'])['LossRatio'].mean().reset_index()
    sns.barplot(x='Province', y='LossRatio', hue='Gender', data=loss_ratio)
    plt.title('Loss Ratio by Province, VehicleType, and Gender')
    plt.show()

def plot_claims_over_time(df: pd.DataFrame):
    """Plot total claims and premium over time."""
    trend = claims_over_time(df)
    trend['Month'] = trend['Month'].astype(str)

    plt.figure(figsize=(12, 5))
    sns.lineplot(data=trend, x='Month', y='ClaimsSum', label='Total Claims')
    sns.lineplot(data=trend, x='Month', y='PremiumSum', label='Total Premiums')
    plt.xticks(rotation=45)
    plt.title("Claim and Premium Trends Over Time")
    plt.tight_layout()
    plt.show()

def plot_top_and_bottom_models_by_claims(df: pd.DataFrame):
    """Plot top and bottom vehicle models by average claims."""

    top = top_models_by_claims(df)
    bottom = bottom_models_by_claims(df)

    # Top models
    print("🚗 Top Claiming Models:")
    print(top)

    plt.figure(figsize=(12, 6))
    sns.barplot(x="Model", y="TotalClaims", data=top, palette="Reds_r")
    plt.xticks(rotation=45)
    plt.title("Top Claiming Vehicle Models")
    plt.tight_layout()
    plt.show()

    # Bottom models
    print("\n🚙 Lowest Claiming Models:")
    print(bottom)

    plt.figure(figsize=(12, 6))
    sns.barplot(x="Model", y="TotalClaims", data=bottom, palette="Blues")
    plt.xticks(rotation=45)
    plt.title("Lowest Claiming Vehicle Models")
    plt.tight_layout()
    plt.show()

def plot_top_loss_ratios(loss_df: pd.DataFrame, top_n=10):
    """
    Plot top N province-vehicle-gender combinations by average loss ratio.
    """
    top = loss_df.sort_values('LossRatio', ascending=False).head(top_n)

    # Combine fields for clean Y-labels
    top['Group'] = top.apply(lambda row: f"{row['Province']} - {row['VehicleType']} - {row['Gender']}", axis=1)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=top, x="LossRatio", y="Group", palette="coolwarm")
    plt.xlabel("Average Loss Ratio")
    plt.ylabel("Group (Province - VehicleType - Gender)")
    plt.title(f"Top {top_n} Groups by Loss Ratio")
    plt.tight_layout()
    plt.show()
# def correlation_heatmap(df: pd.DataFrame):
#     """
#     Plot a heatmap of correlations between numeric columns.
#     """
#     plt.figure(figsize=(12, 8))
#     numeric_df = df.select_dtypes(include=['float64', 'int64'])
#     corr = numeric_df.corr()

#     sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
#     plt.title("Correlation Heatmap of Numerical Features")
#     plt.tight_layout()
#     plt.show()

def correlation_heatmap(df: pd.DataFrame):
    """
    Plot a heatmap of correlations between selected important numeric features.
    """
    important_numeric_cols = [
        "TotalPremium",
        "TotalClaims",
        "SumInsured",
        "CustomValueEstimate",
        "CalculatedPremiumPerTerm"
    ]

    numeric_df = df[important_numeric_cols].copy()
    numeric_df = numeric_df.dropna(how="all")  # drop rows with all NaNs

    if numeric_df.empty or numeric_df.shape[1] < 2:
        print("⚠️ Not enough valid numeric data to compute correlations.")
        return

    corr = numeric_df.corr()

    if corr.isnull().all().all():
        print("⚠️ Correlation matrix is empty or NaN.")
        return

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap of Key Financial Features")
    plt.tight_layout()
    plt.show()
