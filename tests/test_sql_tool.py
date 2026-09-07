import pytest

from app.tools.sql_tool import execute_sql


@pytest.mark.integration
def test_execute_sql():
    result = execute_sql(
        "SELECT COUNT(*) AS row_count FROM sales"
    )

    assert result[0]["row_count"] == 10


@pytest.mark.integration
def test_blocks_write_operations():
    with pytest.raises(ValueError, match="Only SELECT and WITH queries are allowed"):
        execute_sql("DELETE FROM sales")


@pytest.mark.integration
def test_blocks_dangerous_sql():
    with pytest.raises(ValueError, match="Forbidden SQL operation: DROP"):
        execute_sql("SELECT * FROM sales; DROP TABLE sales")