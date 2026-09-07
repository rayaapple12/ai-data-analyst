from langgraph.graph import END, START, StateGraph

from app.agent.planner import generate_plan
from app.agent.sql_generator import generate_sql
from app.agent.state import AgentState
from app.agent.tool_selector import select_tool
from app.tools.sql_tool import execute_sql


def planner_node(state: AgentState) -> AgentState:
    plan = generate_plan(state["question"])

    return {
        **state,
        "plan": plan.steps,
        "current_step": 0,
    }


def tool_node(state: AgentState) -> AgentState:
    step = state["plan"][0]
    tool = select_tool(step)

    if tool != "sql":
        raise ValueError(f"Unsupported tool: {tool}")

    schema = state.get(
        "schema",
        "sales(order_id, order_date, region, product, quantity, unit_price, revenue)",
    )

    sql = generate_sql(
        question=state["question"],
        schema=schema,
    )

    result = execute_sql(sql.query)

    return {
        **state,
        "tool_calls": [
            {
                "tool": tool,
                "step": step,
                "query": sql.query,
            }
        ],
        "results": result,
    }


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("tool", tool_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "tool")
    graph.add_edge("tool", END)

    return graph.compile()