from sqlmodel import SQLModel, Field

class xf_nf_rosters_user(SQLModel, table=True):
    relation_id: int = Field(primary_key=True)
    roster_id: int
    user_id: int
    real_name: str
    position_id: int
    secondary_position_ids: int
    rank_id: int
    custom_fields: str

class xf_nf_rosters(SQLModel, table=True):
    roster_id: int = Field(primary_key=True)
    title: str

class xf_nf_rosters_award(SQLModel, table=True):
    award_id: int = Field(primary_key=True)
    title: str

class xf_nf_rosters_field_value(SQLModel, table=True):
    relation_id: int = Field(primary_key=True)
    field_id: str
    field_value: str

class xf_nf_rosters_position(SQLModel, table=True):
    position_id: int = Field(primary_key=True)
    position_title: str
    position_group_id: int

class xf_nf_rosters_position_group(SQLModel, table=True):
    position_group_id: int = Field(primary_key=True)
    title: str

class xf_nf_rosters_rank(SQLModel, table=True):
    rank_id: int = Field(primary_key=True)
    title: str

class xf_nf_rosters_record_type(SQLModel, table=True):
    record_type_id: int = Field(primary_key=True)
    title: str

class xf_nf_rosters_roster_position(SQLModel, table=True):
    roster_id: int = Field(primary_key=True)
    position_id: int

class xf_nf_roxters_service_record(SQLModel, table=True):
    record_id: int = Field(primary_key=True)
    relation_id: int
    details: str
    record_date: int
    citation_date: int
    record_type_id: int

class xf_nf_rosters_user_award(SQLModel, table=True):
    record_id: int = Field(primary_key=True)
    relation_id: int
    award_id: int
    details: str
    award_date: int
    citation_date: int

