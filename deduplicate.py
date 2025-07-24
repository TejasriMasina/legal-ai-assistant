import json

# Load the original cleaned legal cases
with open("cleaned_legal_cases.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Deduplicate using (case_name, date_filed) as key
unique = {}
for case in data:
    key = (case['case_name'], case['date_filed'])
    if key not in unique:
        unique[key] = case

print(f"Original case count: {len(data)}")
print(f"Unique case count: {len(unique)}")

# Save the de-duplicated dataset
deduped_cases = list(unique.values())
with open("cleaned_legal_cases_deduped.json", "w", encoding="utf-8") as f:
    json.dump(deduped_cases, f, indent=2, ensure_ascii=False)

print("Deduplicated data written to 'cleaned_legal_cases_deduped.json'")
