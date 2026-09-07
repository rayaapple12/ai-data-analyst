from langgraph.graph import END, START, StateGraph

from app.agent.planner import generate_plan
from app.agent.sql_generator import generate_sql
from app.agent.state import AgentState
from app.data.schema import discover_schema
from app.agent.tool_selector import select_tool
from app.tools.sql_tool import execute_sql


def planner_node(state: AgentState) -> AgentState:
    plan = generate_plan(state["question"])
    schema = discover_schema()

    return {
        **state,
        "plan": plan.steps,
        "schema": schema,
        "current_step": 0,
        "tool_calls": [],
        "results": [],
    }


def tool_node(state: AgentState) -> AgentState:
    current_step = state["current_step"]
    step = state["plan"][current_step]
    tool = select_tool(step)

    if tool != "sql":
        raise ValueError(f"Unsupported tool: {tool}")

    sql = generate_sql(
        question=state["question"],
        schema=state["schema"],
    )

    result = execute_sql(sql.query)

    return {
        **state,
        "current_step": current_step + 1,
        "tool_calls": [
            *state.get("tool_calls", []),
            {
                "tool": tool,
                "step": step,
                "query": sql.query,
            }
        ],
        "results": [*state.get("results", []), *result],
    }


def route_after_tool(state: AgentState) -> str:
    if state["current_step"] < len(state["plan"]):
        return "tool"

    return END


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("tool", tool_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "tool")
    graph.add_conditional_edges(
        "tool",
        route_after_tool,
        {
            "tool": "tool",
            END: END,
        },
    )

    return graph.compile()