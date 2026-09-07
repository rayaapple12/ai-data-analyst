from app.agent.tool_selector import select_tool


def test_selects_sql():
    assert select_tool("query the sales table") == "sql"


def test_selects_pandas():
    assert select_tool("filter the dataframe by region") == "pandas"


def test_selects_statistics():
    assert select_tool("calculate the mean and median") == "statistics"


def test_selects_visualization():
    assert select_tool("create a revenue chart") == "visualization"