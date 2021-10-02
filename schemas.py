from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(ge=-9223372036854775808, le=9223372036854775807)
    name: str
    coord: str = Field(regex=r"\(\d+\.?\d*, *\d+\.?\d*\)", )

    class Config:
        orm_mode = True
