from app.agent.graph import build_graph


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

    monkeypatch.setattr(
        "app.agent.graph.generate_plan",
        fake_generate_plan,
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
    assert result["results"][0]["row_count"] == 10