import json

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from app.config.settings import settings


class SQLQuery(BaseModel):
    query: str = Field(
        description="A read-only SQL query that answers the user's question."
    )


def generate_sql(
    question: str,
    schema: dict[str, list[dict[str, str]]],
) -> SQLQuery:
    model = ChatOpenAI(
        model=settings.llm_model,
        temperature=0,
        api_key=settings.openai_api_key,
    ).with_structured_output(SQLQuery)

    return model.invoke(
        f"""
Generate a read-only PostgreSQL query to answer the user's question.

Database schema:
{json.dumps(schema, indent=2)}

Question:
{question}

Rules:
- Only generate SELECT or WITH queries.
- Do not modify database data.
- Use only tables and columns present in the schema.
- Return only the SQL query in the structured output.
"""
    )