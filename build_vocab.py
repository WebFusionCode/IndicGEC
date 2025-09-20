import pandas as pd
import re
import json

# --- Simple tokenizer function ---
def tokenize_text(text):
    # keep only words (remove punctuations, numbers, etc.)
    tokens = re.findall(r'\w+', str(text))
    return [t.lower() for t in tokens]

# --- Load training data ---
train_df = pd.read_csv("data/train.csv")

# Debugging: print column names
print("Available columns in train.csv:", train_df.columns.tolist())

# --- Detect the correct column for target sentences ---
if "target" in train_df.columns:
    col = "target"
elif "Target" in train_df.columns:
    col = "Target"
else:
    # fallback: pick the last column in case header name differs
    col = train_df.columns[-1]

print(f"Building vocabulary from column: {col}")

# --- Build vocabulary ---
vocab = set()
for sent in train_df[col]:
    tokens = tokenize_text(sent)
    vocab.update(tokens)

# --- Save vocabulary to JSON ---
vocab_list = sorted(list(vocab))
with open("data/vocab.json", "w", encoding="utf-8") as f:
    json.dump(vocab_list, f, ensure_ascii=False, indent=2)

print(f"✅ Vocabulary built! {len(vocab_list)} unique tokens saved to data/vocab.json")