from sqlalchemy import inspect

from app.data.database import engine


def discover_schema(database_engine=engine) -> dict[str, list[dict[str, str]]]:
    inspector = inspect(database_engine)

    return {
        table_name: [
            {
                "name": column["name"],
                "type": str(column["type"]),
            }
            for column in inspector.get_columns(table_name)
        ]
        for table_name in inspector.get_table_names()
    }