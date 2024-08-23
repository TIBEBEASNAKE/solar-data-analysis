import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df1 = pd.read_csv('../data/benin-malanville.csv')  # Replace with actual file names
df2 = pd.read_csv('../data/sierraleone-bumbuna.csv')
df3 = pd.read_csv('../data/togo-dapaong_qc.csv')

# Display the first few rows of each dataset
print("Dataset 1:")
print(df1.head())
print("\nDataset 2:")
print(df2.head())
print("\nDataset 3:")
print(df3.head())
# Summary statistics for each dataset
print("Dataset 1 Summary Statistics:")
print(df1.describe())

print("\nDataset 2 Summary Statistics:")
print(df2.describe())

print("\nDataset 3 Summary Statistics:")
print(df3.describe())

# Check for missing values
print("Dataset 1 Missing Values:")
print(df1.isnull().sum())

print("\nDataset 2 Missing Values:")
print(df2.isnull().sum())

print("\nDataset 3 Missing Values:")
print(df3.isnull().sum())
print(df1.columns)
print(df2.columns)
print(df3.columns)

