from typing import Literal


ToolName = Literal[
    "sql",
    "pandas",
    "statistics",
    "visualization",
]


def select_tool(step: str) -> ToolName:
    step_lower = step.lower()

    if any(
        keyword in step_lower
        for keyword in ["sql", "query", "database", "table"]
    ):
        return "sql"

    if any(
        keyword in step_lower
        for keyword in ["filter", "dataframe", "pandas", "transform"]
    ):
        return "pandas"

    if any(
        keyword in step_lower
        for keyword in ["mean", "median", "standard deviation", "statistics"]
    ):
        return "statistics"

    if any(
        keyword in step_lower
        for keyword in ["chart", "plot", "visualization", "graph"]
    ):
        return "visualization"

    return "sql"