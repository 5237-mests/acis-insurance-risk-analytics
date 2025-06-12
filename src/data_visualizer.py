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
    """Plot top and bottom models by claims."""
    top = top_models_by_claims(df)
    bottom = bottom_models_by_claims(df)

    print("Top Claiming Models:")
    sns.barplot(x="Model", y="TotalClaims", data=top)
    plt.figure(figsize=(12, 6))
    plt.xticks(rotation=45)
    plt.title("Top Claiming Models")
    plt.tight_layout()
    plt.show()
    print(" Top Claiming Models:")
    print(top)

    print("\nLowest Claiming Models:")
    sns.barplot(x="Model", y="TotalClaims", data=bottom)
    plt.figure(figsize=(12, 6))
    plt.xticks(rotation=45)
    plt.title("Lowest Claiming Models*")
    plt.tight_layout()
    plt.show()
    print("\n Lowest Claiming Models:")
    print(bottom)

