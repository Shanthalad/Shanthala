from typing import List, Tuple
import re

COMPANY_KEYWORDS = ['pharma', 'biotech', 'therapeutics', 'inc', 'ltd', 'gmbh']

def is_company(affil: str) -> bool:
    affil = affil.lower()
    return any(word in affil for word in COMPANY_KEYWORDS)

def extract_non_academic_authors(authors):
    names, companies = [], []
    for author in authors:
        affil_info = author.get("AffiliationInfo", {})
        
        # Handle both list and dict
        if isinstance(affil_info, list):
            affil_text = affil_info[0].get("Affiliation", "")
        elif isinstance(affil_info, dict):
            affil_text = affil_info.get("Affiliation", "")
        else:
            affil_text = ""

        name = author.get("ForeName", "") + " " + author.get("LastName", "")

        if is_company(affil_text):  # You can improve this logic later
            companies.append(name.strip())
        else:
            names.append(name.strip())
    
    return names, companies

