import pandas as pd


def filter_rows(
    df: pd.DataFrame,
    column: str,
    value: object,
) -> pd.DataFrame:
    if column not in df.columns:
        raise ValueError(f"Unknown column: {column}")

    return df[df[column] == value].copy()


def group_and_aggregate(
    df: pd.DataFrame,
    group_by: str,
    value_column: str,
    operation: str,
) -> pd.DataFrame:
    if group_by not in df.columns:
        raise ValueError(f"Unknown column: {group_by}")

    if value_column not in df.columns:
        raise ValueError(f"Unknown column: {value_column}")

    if operation not in {"sum", "mean", "min", "max", "count"}:
        raise ValueError(f"Unsupported operation: {operation}")

    return (
        df.groupby(group_by)[value_column]
        .agg(operation)
        .reset_index()
    )