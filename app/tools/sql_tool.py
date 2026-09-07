from sqlalchemy import text

from app.data.database import engine
from app.tools.sql_validator import validate_sql


def execute_sql(query: str) -> list[dict]:
    query = validate_sql(query)

    with engine.connect() as connection:
        result = connection.execute(text(query))

        return [
            dict(row._mapping)
            for row in result
        ]