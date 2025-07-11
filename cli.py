import typer
from .api import fetch_pubmed_ids, fetch_details
from .filters import extract_non_academic_authors
from .csv_writer import save_to_csv
from .utils import get_first_email

app = typer.Typer()

@app.command()
def get_papers_list(query: str, file: str = "", debug: bool = False):
    if debug:
        typer.echo(f"Fetching papers for query: {query}")

    ids = fetch_pubmed_ids(query)
    records = fetch_details(ids)

    results = []
    for record in records:
        article = record["MedlineCitation"]["Article"]
        authors = article.get("AuthorList", {}).get("Author", [])
        if isinstance(authors, dict):
            authors = [authors]

        names, companies = extract_non_academic_authors(authors)
        if not names:
            continue

        pmid = record["MedlineCitation"]["PMID"]
        if isinstance(pmid, dict):
            pmid = pmid.get("#text", pmid)

        results.append({
            "PubmedID": pmid,
            "Title": article.get("ArticleTitle", ""),
            "Publication Date": article.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", ""),
            "Non-academic Author(s)": ", ".join(names),
            "Company Affiliation(s)": ", ".join(companies),
            "Corresponding Author Email": get_first_email(authors),
        })

    if file:
        save_to_csv(results, file)
        typer.echo(f"Saved to {file}")
    else:
        for row in results:
            typer.echo(row)

if __name__ == "__main__":
    app()
