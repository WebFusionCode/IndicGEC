import pandas as pd
from rule_based_gec import correct_sentence

#Load test data correctly
test_df = pd.read_csv("data/test.csv", sep=",", encoding="utf-8")

# Clean column names (remove spaces, BOM, etc.)
test_df.columns = [c.strip() for c in test_df.columns]

print("Available columns after cleaning:", test_df.columns.tolist())
print("Sample rows:")
print(test_df.head())

#Detect correct column names
if "source" in test_df.columns and "target" in test_df.columns:
    source_col, target_col = "source", "target"
else:
    # fallback: assume first = source, second = target
    source_col, target_col = test_df.columns[0], test_df.columns[1]

print(f"Using columns: source={source_col}, target={target_col}")

#Apply corrections
test_df["predicted"] = test_df[source_col].apply(correct_sentence)

#Save results
test_df.to_csv("data/test_results.csv", index=False, encoding="utf-8")

print("\n Corrections completed! Results saved in data/test_results.csv")
print(test_df[[source_col, target_col, "predicted"]])