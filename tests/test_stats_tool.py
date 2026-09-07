import pandas as pd
import pytest

from app.tools.stats_tool import describe_column


@pytest.fixture
def sales_df():
    return pd.DataFrame(
        {
            "revenue": [100, 200, 300, 400],
            "region": ["North", "South", "North", "South"],
        }
    )


def test_describe_column(sales_df):
    result = describe_column(sales_df, "revenue")

    assert result["count"] == 4
    assert result["mean"] == 250.0
    assert result["median"] == 250.0
    assert result["min"] == 100.0
    assert result["max"] == 400.0


def test_unknown_column(sales_df):
    with pytest.raises(ValueError, match="Unknown column"):
        describe_column(sales_df, "profit")


def test_non_numeric_column(sales_df):
    with pytest.raises(ValueError, match="must be numeric"):
        describe_column(sales_df, "region")