import re


FORBIDDEN_SQL = {
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
}


def validate_sql(query: str) -> str:
    query = query.strip()

    if not query:
        raise ValueError("SQL query cannot be empty.")

    if not re.match(r"^(SELECT|WITH)\b", query, re.IGNORECASE):
        raise ValueError("Only SELECT and WITH queries are allowed.")

    for keyword in FORBIDDEN_SQL:
        if re.search(rf"\b{keyword}\b", query, re.IGNORECASE):
            raise ValueError(f"Forbidden SQL operation: {keyword}")

    return query