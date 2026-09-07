from app.agent.graph import build_graph
from app.agent.sql_generator import SQLQuery


def test_agent_graph(monkeypatch):
    def fake_generate_plan(question):
        return type(
            "Plan",
            (),
            {
                "steps": [
                    "query the sales table",
                ]
            },
        )()

    def fake_generate_sql(question, schema):
        return SQLQuery(
            query="SELECT COUNT(*) AS row_count FROM sales"
        )

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
        "query the sales table",
    ]
    assert result["tool_calls"][0]["tool"] == "sql"
    assert result["tool_calls"][0]["query"] == (
        "SELECT COUNT(*) AS row_count FROM sales"
    )
    assert result["results"][0]["row_count"] == 10