from app.agent.graph import build_graph
from app.agent.sql_generator import SQLQuery


def test_agent_graph(monkeypatch):
    def fake_generate_plan(question):
        return type(
            "Plan",
            (),
            {
                "steps": [
                    "query the sales table for row count",
                    "query the sales table for total revenue",
                ]
            },
        )()

    sql_queries = iter(
        [
            "SELECT COUNT(*) AS row_count FROM sales",
            "SELECT SUM(revenue) AS total_revenue FROM sales",
        ]
    )

    def fake_generate_sql(question, schema):
        return SQLQuery(query=next(sql_queries))

    monkeypatch.setattr(
        "app.agent.graph.generate_plan",
        fake_generate_plan,
    )
    monkeypatch.setattr(
        "app.agent.graph.generate_sql",
        fake_generate_sql,
    )

    graph = build_graph()

    result = graph.invoke(
        {
            "question": "How many sales are there?",
        }
    )

    assert result["plan"] == [
        "query the sales table for row count",
        "query the sales table for total revenue",
    ]
    assert result["current_step"] == 2
    assert [call["tool"] for call in result["tool_calls"]] == [
        "sql",
        "sql",
    ]
    assert [call["step"] for call in result["tool_calls"]] == [
        "query the sales table for row count",
        "query the sales table for total revenue",
    ]
    assert [call["query"] for call in result["tool_calls"]] == [
        "SELECT COUNT(*) AS row_count FROM sales",
        "SELECT SUM(revenue) AS total_revenue FROM sales",
    ]
    assert result["results"][0]["row_count"] == 10
    assert result["results"][1]["total_revenue"] == 14500