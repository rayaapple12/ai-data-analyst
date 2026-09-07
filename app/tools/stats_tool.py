import pandas as pd


def describe_column(
    df: pd.DataFrame,
    column: str,
) -> dict:
    if column not in df.columns:
        raise ValueError(f"Unknown column: {column}")

    series = df[column]

    if not pd.api.types.is_numeric_dtype(series):
        raise ValueError(f"Column '{column}' must be numeric.")

    return {
        "count": int(series.count()),
        "mean": float(series.mean()),
        "median": float(series.median()),
        "min": float(series.min()),
        "max": float(series.max()),
        "std": float(series.std()),
    }