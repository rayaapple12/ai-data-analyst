from typing import Any, TypedDict


class AgentState(TypedDict, total=False):
    question: str
    dataset_name: str
    schema: dict[str, Any]
    plan: list[str]
    current_step: int
    tool_calls: list[dict[str, Any]]
    results: list[dict[str, Any]]
    answer: str
    error: str