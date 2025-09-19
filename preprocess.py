import pandas as pd
import re
import unicodedata

#Normalization
def normalize_text(s: str) -> str:
    """Clean and normalize Hindi text."""
    if not isinstance(s, str):
        return s
    
    # Normalize Unicode (important for Devanagari letters)
    s = unicodedata.normalize('NFC', s)

    # Remove extra spaces
    s = re.sub(r'\s+', ' ', s).strip()
    # Remove space before punctuation
    s = re.sub(r'\s+([?!.,])', r'\1', s)
    return s

#Tokenization
def tokenize_text(s: str):
    """Split text into tokens (words + punctuation)."""
    s = normalize_text(s)
    
    # Hindi characters: \u0900-\u097F
    tokens = re.findall(r'[\w\u0900-\u097F]+|[?!.]', s)
    return tokens

#Demo on Train & Test Data
train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

print("✅ Example Preprocessing (Train Data):\n")
for i in range(3):  # first 3 rows
    src = train_df.loc[i, "source"]
    tgt = train_df.loc[i, "target"]
    print(f"Original Source: {src}")
    print(f"Normalized: {normalize_text(src)}")
    print(f"Tokenized: {tokenize_text(src)}\n")