import pytest
from sqlalchemy import text

from app.data.database import engine


@pytest.mark.integration
def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1