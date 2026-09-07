from app.agent.sql_generator import SQLQuery


def test_sql_query_model():
    result = SQLQuery(
        query="SELECT COUNT(*) AS row_count FROM sales"
    )

    assert result.query.startswith("SELECT")
    assert "sales" in result.query