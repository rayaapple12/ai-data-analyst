from app.agent.graph import build_graph


def test_agent_graph(monkeypatch):
    def fake_generate_plan(question):
        return type(
            "Plan",
            (),
            {
                "steps": [
                    "group sales by region",
                    "calculate total revenue",
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
            "question": "Which region generated the most revenue?",
        }
    )

    assert result["plan"] == [
        "group sales by region",
        "calculate total revenue",
    ]