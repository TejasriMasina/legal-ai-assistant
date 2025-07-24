# summarizer.py

import json
from transformers import pipeline
from tqdm import tqdm

# Load cleaned and unique cases
with open("cleaned_legal_cases_deduped.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")

# Summarize each case (truncate to 1024 tokens for BART)
for case in tqdm(cases, desc="Summarizing cases"):
    text = case["text"]
    if len(text) > 300:
        try:
            summary = summarizer(text[:1024], max_length=150, min_length=40, do_sample=False)[0]["summary_text"]
            case["summary"] = summary
        except Exception as e:
            print("❌", case.get("case_name"), e)
            case["summary"] = "Summarization failed."
    else:
        case["summary"] = "Too short to summarize."

# Save summaries
with open("summaries.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, indent=2)

print("All summaries saved.")
