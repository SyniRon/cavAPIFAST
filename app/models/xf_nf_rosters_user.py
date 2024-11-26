from sqlmodel import SQLModel, Field

class xf_nf_rosters_user(SQLModel):
    relation_id: int = Field(primary_key=True)
    roster_id: int
    user_id: int
    real_name: str
    position_id: int
    secondary_position_ids: int
    rank_id: int
    custom_fields: str