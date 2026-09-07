import pandas as pd

from app.data.database import engine


def main() -> None:
    df = pd.read_csv("app/data/sample_sales.csv")

    df.to_sql(
        "sales",
        engine,
        if_exists="replace",
        index=False,
    )

    print(f"Loaded {len(df)} rows into the sales table.")


if __name__ == "__main__":
    main()