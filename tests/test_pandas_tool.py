import pandas as pd
import pytest

from app.tools.pandas_tool import filter_rows, group_and_aggregate


@pytest.fixture
def sales_df():
    return pd.DataFrame(
        {
            "region": ["North", "North", "South"],
            "revenue": [100, 200, 300],
        }
    )


def test_filter_rows(sales_df):
    result = filter_rows(sales_df, "region", "North")

    assert len(result) == 2
    assert result["revenue"].tolist() == [100, 200]


def test_group_and_aggregate(sales_df):
    result = group_and_aggregate(
        sales_df,
        "region",
        "revenue",
        "sum",
    )

    assert result.to_dict("records") == [
        {"region": "North", "revenue": 300},
        {"region": "South", "revenue": 300},
    ]


def test_unknown_column(sales_df):
    with pytest.raises(ValueError, match="Unknown column"):
        filter_rows(sales_df, "country", "India")


def test_invalid_operation(sales_df):
    with pytest.raises(ValueError, match="Unsupported operation"):
        group_and_aggregate(sales_df, "region", "revenue", "median")