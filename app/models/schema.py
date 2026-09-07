from pydantic import BaseModel


class ColumnInfo(BaseModel):
    name: str
    dtype: str
    nullable: bool


class DatasetSchema(BaseModel):
    columns: list[ColumnInfo]
    row_count: int