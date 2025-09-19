import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("data/sample_data.csv")

# Split into 70% train and 30% test
train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)

train_df.to_csv("data/train.csv", index=False, encoding="utf-8-sig")
test_df.to_csv("data/test.csv", index=False, encoding="utf-8-sig")

print("✅ Data has been split and saved!")
print(f"Training samples: {len(train_df)}")
print(f"Testing samples: {len(test_df)}")