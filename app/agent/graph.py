from langgraph.graph import END, START, StateGraph

from app.agent.planner import generate_plan
from app.agent.state import AgentState
from app.agent.tool_selector import select_tool
from app.tools.sql_tool import execute_sql


def planner_node(state: AgentState) -> AgentState:
    plan = generate_plan(state["question"])

    return {
        **state,
        "plan": plan.steps,
    }


def tool_node(state: AgentState) -> AgentState:
    step = state["plan"][0]
    tool = select_tool(step)

    if tool == "sql":
        result = execute_sql(
            "SELECT COUNT(*) AS row_count FROM sales"
        )

        return {
            **state,
            "tool_calls": [
                {
                    "tool": tool,
                    "step": step,
                }
            ],
            "results": result,
        }

    raise ValueError(f"Unsupported tool: {tool}")


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("tool", tool_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "tool")
    graph.add_edge("tool", END)

    return graph.compile()