from app.agent.graph import build_graph


def test_agent_graph():
    graph = build_graph()

    result = graph.invoke(
        {
            "question": "What is total revenue?",
        }
    )

    assert result["question"] == "What is total revenue?"
    assert result["answer"] == "Agent graph initialized."