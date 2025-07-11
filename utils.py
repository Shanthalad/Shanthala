def get_first_email(authors: list) -> str:
    for author in authors:
        if isinstance(author, dict) and "ElectronicAddress" in author:
            return author["ElectronicAddress"]
    return ""
