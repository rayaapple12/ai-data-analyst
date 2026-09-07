from langgraph.graph import END, START, StateGraph

from app.agent.planner import generate_plan
from app.agent.state import AgentState


def planner_node(state: AgentState) -> AgentState:
    plan = generate_plan(state["question"])

    return {
        **state,
        "plan": plan.steps,
    }


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", END)

    return graph.compile()