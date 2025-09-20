import re

# Simple tokenizer
def tokenize_text(text):
    tokens = re.findall(r'\w+', str(text))
    return [t.lower() for t in tokens]

#Rule-based correction function
def correct_sentence(sentence):
    corrected = sentence
    corrected = corrected.replace("है हूँ", "हूँ")  
    corrected = corrected.replace("खुश है", "खुश हूँ")  
    corrected = corrected.replace("तुम्हे", "तुम्हें")
    corrected = corrected.replace("जायेगा था", "गया था")
    corrected = corrected.replace("लड़के खेल रहा है", "लड़के खेल रहे हैं")

    # Add more rules on need

    return corrected

#Quick test
if __name__ == "__main__":
    test_sentences = [
        "मैं खुश है",
        "तुम्हे पता नहीं है क्या",
        "वह कल स्कूल जायेगा था",
        "लड़के खेल रहा है"
    ]

    for s in test_sentences:
        print(f"{s}")
        print(f"{correct_sentence(s)}\n")