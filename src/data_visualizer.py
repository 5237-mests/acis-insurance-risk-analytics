import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
