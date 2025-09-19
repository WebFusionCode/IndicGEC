import pandas as pd

# Load the dataset
df = pd.read_csv("data/sample_data.csv")

print("First 5 rows of the dataset:")
print(df.head())

# Show dataset info
print("\nDataset info:")
print(df.info())