import requests
import time
import json
from tqdm import tqdm

search_url = "https://www.courtlistener.com/api/rest/v4/search/"
opinion_base_url = "https://www.courtlistener.com"

search_params = {
    "type": "o",                  # o = opinions
    "search": "contract breach",  # or any keyword
    "page_size": 20
}

cases = []
max_cases = 100  

print("Fetching full legal opinions from CourtListener...")

while len(cases) < max_cases and search_url:
    response = requests.get(search_url, params=search_params)
    data = response.json()

    for item in tqdm(data["results"]):
        try:
            if not item["opinions"]:
                continue  # no opinion linked

            # FIX: each opinion is a dict; extract "id"
            opinion_id = item["opinions"][0]["id"]

            opinion_api_url = f"https://www.courtlistener.com/api/rest/v4/opinions/{opinion_id}/"
            op_res = requests.get(opinion_api_url)
            op_data = op_res.json()

           
            full_text = op_data.get("plain_text") or op_data.get("html_with_citations", "")

            if len(full_text.strip()) < 500:
                continue  # skip short ones

            cases.append({
                "case_name": item.get("caseNameFull") or item.get("caseName"),
                "date_filed": item.get("dateFiled"),
                "court": item.get("court_id"),
                "citation": item.get("citation"),
                "text": full_text.strip()
            })

            print(f"✔ Collected: {item.get('caseName')}")

            if len(cases) >= max_cases:
                break

            time.sleep(0.5)

        except Exception as e:
            print("Error:", e)
            continue

    # Move to next page if available
    search_url = data.get("next")

# Save to JSON
with open("legal_cases_dataset.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, indent=2)

print(f"\n Total downloaded: {len(cases)} cases.")



