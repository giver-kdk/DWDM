# Outlier removal using Z-Score Method
import numpy as np
import pandas as pd
from scipy.stats import zscore

# Sample data for milk + bread and milk + salt buying
data = {'Milk + Bread': [10, 12, 13, 12, 14, 10, 11, 120, 13, 15],
'Milk + Salt': [5, 6, 7, 5, 6, 5, 4, 80, 7, 6]}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Calculate Z-Score for each column
z_scores = np.abs(zscore(df))

# Set a threshold for Z-Score (commonly 3 or -3)
threshold = 3

# Remove outliers (those that have Z-Score > 3)
df_cleaned = df[(z_scores < threshold).all(axis=1)]

print("Original Data:\n", df)
print("\nZ-Scores:\n", z_scores)
print("\nCleaned Data (without outliers):\n", df_cleaned)