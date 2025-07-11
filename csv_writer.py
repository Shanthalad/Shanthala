import csv
from typing import List, Dict

def save_to_csv(data: List[Dict], filename: str):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "PubmedID", "Title", "Publication Date",
            "Non-academic Author(s)", "Company Affiliation(s)",
            "Corresponding Author Email"
        ])
        writer.writeheader()
        writer.writerows(data)
