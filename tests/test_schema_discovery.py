from app.data.schema import discover_schema


def test_discover_schema(monkeypatch):
    class FakeInspector:
        def get_table_names(self):
            return ["sales"]

        def get_columns(self, table_name):
            assert table_name == "sales"
            return [
                {"name": "order_id", "type": "INTEGER"},
                {"name": "revenue", "type": "NUMERIC(10, 2)"},
            ]

    monkeypatch.setattr(
        "app.data.schema.inspect",
        lambda database_engine: FakeInspector(),
    )

    assert discover_schema(object()) == {
        "sales": [
            {"name": "order_id", "type": "INTEGER"},
            {"name": "revenue", "type": "NUMERIC(10, 2)"},
        ]
    }