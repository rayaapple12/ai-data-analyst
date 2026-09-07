from langgraph.graph import END, START, StateGraph

from app.agent.state import AgentState


def analyst_node(state: AgentState) -> AgentState:
    return {
        **state,
        "answer": "Agent graph initialized.",
    }


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("analyst", analyst_node)

    graph.add_edge(START, "analyst")
    graph.add_edge("analyst", END)

    return graph.compile()