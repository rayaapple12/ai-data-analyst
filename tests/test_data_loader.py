import pandas as pd
import pytest

from app.data.loader import inspect_schema, load_dataset


def test_load_dataset(tmp_path):
    dataset = tmp_path / "sales.csv"
    dataset.write_text(
        "id,region,revenue\n"
        "1,North,100\n"
        "2,South,200\n"
    )

    df = load_dataset(dataset)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["id", "region", "revenue"]


def test_missing_dataset():
    with pytest.raises(FileNotFoundError):
        load_dataset("missing.csv")


def test_schema_inspection():
    df = pd.DataFrame(
        {
            "id": [1, 2],
            "region": ["North", "South"],
            "revenue": [100.0, 200.0],
        }
    )

    schema = inspect_schema(df)

    assert schema.row_count == 2
    assert len(schema.columns) == 3
    assert schema.columns[0].name == "id"
    assert schema.columns[0].nullable is False