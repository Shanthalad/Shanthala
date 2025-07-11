# PubMed Paper Fetcher

Fetch PubMed research papers with non-academic (biotech/pharma) authors.

## 🚀 Features

- Query PubMed using any keyword
- Extract titles, publication dates, PubMed IDs
- Detect non-academic authors and company affiliations
- Export results to CSV

---

## ⚙️ Installation Guide (Step-by-Step)

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/pubmed-fetcher
cd pubmed-fetcher
```

### 2. Install Python (if not installed)

Make sure you have Python 3.8 or higher installed:

```bash
python --version
```

Download from: https://www.python.org/downloads/

> ✅ On Windows: During Python install, enable "Add Python to PATH"

### 3. Install Poetry

```bash
# Windows
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# macOS/Linux
curl -sSL https://install.python-poetry.org | python3 -
```

Then restart your terminal and check:

```bash
poetry --version
```

### 4. Install Project Dependencies

```bash
poetry install
```

---

## ✅ Run the Project

### Example Command

```bash
poetry run get-papers-list "covid vaccine" --debug --file=results.csv
```

---

## ✅ Quick Test Command

```bash
# Try this after installation to check it's working
poetry run get-papers-list "covid vaccine" --file=test_output.csv
```

---

## 📂 Optional: Use pip/venv Instead of Poetry

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python pubmed_fetcher/main.py "covid vaccine"
```

---

## 🧪 Sample Output

Example CSV output (results.csv):

```
PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s),Corresponding Author Email
40640805,The Mirror of Erised: a retrospective population-wide study...,2025,"Ondrej Vencalek, Tomas Furst, ...",,
...
```

Include a real sample results.csv in the repo for reference.

---

## 📞 Contact

For issues or contributions, feel free to open an issue or PR on GitHub.

---

## 💡 Credits

Developed by [Your Name]. Uses BioPython, Entrez, pandas, and regex for extraction.
