from pathlib import Path

import pandas as pd
import pytest

from app.tools.visualization_tool import create_bar_chart


def test_create_bar_chart(tmp_path, monkeypatch):
    df = pd.DataFrame(
        {
            "region": ["North", "South"],
            "revenue": [100, 200],
        }
    )

    output_dir = tmp_path / "charts"
    monkeypatch.setattr(
        "app.tools.visualization_tool.OUTPUT_DIR",
        output_dir,
    )

    result = create_bar_chart(
        df,
        "region",
        "revenue",
    )

    assert Path(result).exists()
    assert Path(result).suffix == ".png"


def test_unknown_column():
    df = pd.DataFrame(
        {
            "region": ["North"],
            "revenue": [100],
        }
    )

    with pytest.raises(ValueError, match="Unknown column"):
        create_bar_chart(df, "country", "revenue")


def test_non_numeric_value_column():
    df = pd.DataFrame(
        {
            "region": ["North"],
            "revenue": ["100"],
        }
    )

    with pytest.raises(ValueError, match="must be numeric"):
        create_bar_chart(df, "region", "revenue")