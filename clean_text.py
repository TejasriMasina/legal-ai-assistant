# clean_text.py
import json
import re

def clean_legal_text(text):
    text = re.sub(r'In\s+The\s+Court.*?District of .*?\n+', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'(Before\s+[A-Z ,.\n]+)+', '', text)
    text = re.sub(r'(\n\s*){2,}', '\n\n', text)
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

with open("legal_cases_dataset.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

for case in cases:
    case["text"] = clean_legal_text(case["text"])

with open("cleaned_legal_cases.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, indent=2)

print("Cleaned cases written to cleaned_legal_cases.json")
