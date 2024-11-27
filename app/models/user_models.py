from sqlmodel import SQLModel, Field

class xf_user(SQLModel, table=True):
    user_id: int = Field(primary_key=True)
    username: str

class xf_user_connected_account (SQLModel, Table = True):
    user_id: int = Field(primary_key=True)
    provider: str
    provider_key: str