from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


OUTPUT_DIR = Path("outputs/charts")


def create_bar_chart(
    df: pd.DataFrame,
    category_column: str,
    value_column: str,
    filename: str = "bar_chart.png",
) -> str:
    if category_column not in df.columns:
        raise ValueError(f"Unknown column: {category_column}")

    if value_column not in df.columns:
        raise ValueError(f"Unknown column: {value_column}")

    if not pd.api.types.is_numeric_dtype(df[value_column]):
        raise ValueError(f"Column '{value_column}' must be numeric.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    path = OUTPUT_DIR / filename

    fig, ax = plt.subplots()
    ax.bar(df[category_column].astype(str), df[value_column])
    ax.set_xlabel(category_column)
    ax.set_ylabel(value_column)
    ax.set_title(f"{value_column} by {category_column}")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)

    return str(path)