import json

# Load the saved vocab
with open("data/vocab.json", "r", encoding="utf-8") as f:
    vocab = json.load(f)

print(f"Loaded vocabulary with {len(vocab)} tokens")

# Show first 20 tokens for quick check
print("Sample tokens:", vocab[:20])