import pandas as pd

df = pd.read_csv("data/sample_data.csv")

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())