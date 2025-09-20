import pandas as pd
from rule_based_gec import correct_sentence

#Load test data
test_df = pd.read_csv("data/test.csv")

print("Loaded test data:")
print(test_df.head())

# Apply corrections
predictions = []
for sent in test_df["source"]:
    predictions.append(correct_sentence(sent))

#Add predictions column
test_df["predicted"] = predictions

#Save results
test_df.to_csv("data/test_results.csv", index=False, encoding="utf-8")

print("\n Corrections completed! Results saved in data/test_results.csv")
print(test_df[["source", "target", "predicted"]])