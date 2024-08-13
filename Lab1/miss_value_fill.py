import pandas as pd 
import numpy as np

# Example dataframe 
data = { 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 'Age': [25, np.nan, 30, np.nan, 22] }

df = pd.DataFrame(data)

# Calculate the mean age, skipping NaN values 
mean_age = df['Age'].mean()

# Fill missing values in 'Age' column with the mean age 
df['Age'].fillna(mean_age, inplace=True)

print(df)