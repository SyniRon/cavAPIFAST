from sqlmodel import SQLModel, Field


# User Models
class XfUser(SQLModel, table=True):
    __tablename__ = 'xf_user'
    user_id: int = Field(primary_key=True)
    username: str

class XfUserConnectedAccount (SQLModel, Table = True):
    __tablename__ = 'xf_user_connected_account'
    user_id: int = Field(primary_key=True)
    provider: str
    provider_key: str


# Roster Models
class XfNfRostersUser(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_user'
    relation_id: int = Field(primary_key=True)
    roster_id: int
    user_id: int
    real_name: str
    position_id: int
    secondary_position_ids: int
    rank_id: int
    custom_fields: str

class XfNfRosters(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters'
    roster_id: int = Field(primary_key=True)
    title: str

class XfNfRostersAward(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_award'
    award_id: int = Field(primary_key=True)
    title: str

class XfNfRostersFieldValue(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_field_value'
    relation_id: int = Field(primary_key=True)
    field_id: str = Field(primary_key=True)
    field_value: str

class XfNfRostersPosition(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_position'
    position_id: int = Field(primary_key=True)
    position_title: str
    position_group_id: int

class XfNfRostersPositionGroup(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_position_group'
    position_group_id: int = Field(primary_key=True)
    title: str

class XfNfRostersRank(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_rank'
    rank_id: int = Field(primary_key=True)
    title: str

class XfNfRostersRecordType(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_record_type'
    record_type_id: int = Field(primary_key=True)
    title: str

class XfNfRostersRosterPosition(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_roster_position'
    roster_id: int = Field(primary_key=True)
    position_id: int

class XfNfRostersServiceRecord(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_service_record'
    record_id: int = Field(primary_key=True)
    relation_id: int
    details: str
    record_date: int
    citation_date: int
    record_type_id: int

class XfNfRostersUserAward(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_user_award'
    record_id: int = Field(primary_key=True)
    relation_id: int
    award_id: int
    details: str
    award_date: int
    citation_date: int

