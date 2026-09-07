from pathlib import Path

import pandas as pd

from app.models.schema import ColumnInfo, DatasetSchema


SUPPORTED_EXTENSIONS = {".csv"}


def load_dataset(path: str | Path) -> pd.DataFrame:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {path.suffix}. "
            f"Supported types: {sorted(SUPPORTED_EXTENSIONS)}"
        )

    if path.stat().st_size == 0:
        raise ValueError("Dataset file is empty.")

    return pd.read_csv(path)


def inspect_schema(df: pd.DataFrame) -> DatasetSchema:
    columns = [
        ColumnInfo(
            name=column,
            dtype=str(df[column].dtype),
            nullable=bool(df[column].isna().any()),
        )
        for column in df.columns
    ]

    return DatasetSchema(
        columns=columns,
        row_count=len(df),
    )