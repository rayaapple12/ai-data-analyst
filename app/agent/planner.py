from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from app.config.settings import settings


class AnalysisPlan(BaseModel):
    steps: list[str] = Field(
        description="Ordered steps required to answer the user's question."
    )


def create_planner() -> ChatOpenAI:
    return ChatOpenAI(
        model=settings.llm_model,
        temperature=0,
        api_key=settings.openai_api_key,
    )


def generate_plan(question: str) -> AnalysisPlan:
    planner = create_planner().with_structured_output(AnalysisPlan)

    return planner.invoke(
        f"""
Create a concise analysis plan for this data question.

Question: {question}

Only describe the analysis steps.
Do not calculate the answer.
"""
    )