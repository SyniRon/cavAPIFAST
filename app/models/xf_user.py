from sqlmodel import SQLModel, Field

class xf_user(SQLModel, table=True):
    user_id: int = Field(primary_key=True)
    username: str