import requests
import xmltodict
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_ids(query: str) -> List[str]:
    response = requests.get(f"{BASE_URL}esearch.fcgi", params={
        "db": "pubmed", "term": query, "retmode": "json"
    })
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    ids_str = ",".join(pubmed_ids)
    response = requests.get(f"{BASE_URL}efetch.fcgi", params={
        "db": "pubmed", "id": ids_str, "retmode": "xml"
    })
    response.raise_for_status()
    records = xmltodict.parse(response.text)["PubmedArticleSet"]["PubmedArticle"]
    return records if isinstance(records, list) else [records]

# ✅ Add this test block so it runs something
if __name__ == "__main__":
    query = "cancer AND drug"
    ids = fetch_pubmed_ids(query)
    print(f"Found {len(ids)} PubMed IDs")
    
    details = fetch_details(ids[:5])  # Limit to first 5 for speed
    print(f"Sample Title: {details[0]['MedlineCitation']['Article']['ArticleTitle']}")
