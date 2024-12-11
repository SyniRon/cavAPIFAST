from sqlmodel import SQLModel, Field, Relationship

# User Models
class XfUser(SQLModel, table=True):
    __tablename__ = 'xf_user'
    # Columns
    user_id: int = Field(primary_key=True)
    username: str
    # Relationships
    roster: "XfNfRostersUser" = Relationship(back_populates="user")
    connected_account: list["XfUserConnectedAccount"] = Relationship(back_populates="user")

class XfUserConnectedAccount (SQLModel, table = True):
    __tablename__ = 'xf_user_connected_account'
    # Columns
    user_id: int = Field(primary_key=True, foreign_key="xf_user.user_id")
    provider: str
    provider_key: str
    # Relationships
    user: "XfUser" = Relationship(back_populates="connected_account")


# Roster Models
class XfNfRostersUser(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_user'
    # Columns
    relation_id: int = Field(primary_key=True)
    roster_id: int
    user_id: int = Field(foreign_key="xf_user.user_id")
    real_name: str
    position_id: int
    secondary_position_ids: bytes
    rank_id: int
    custom_fields: bytes
    # Relationships
    user: "XfUser" = Relationship(back_populates="roster")
    fields: list["XfNfRostersFieldValue"] = Relationship(back_populates="roster_user")
    service_records: list["XfNfRostersServiceRecord"] = Relationship(back_populates="roster_user")
    awards: list["XfNfRostersUserAward"] = Relationship(back_populates="roster_user")

class XfNfRosters(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters'
    # Columns
    roster_id: int = Field(primary_key=True)
    title: str
    # Relationships

class XfNfRostersAward(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_award'
    # Columns
    award_id: int = Field(primary_key=True)
    title: str
    # Relationships

class XfNfRostersFieldValue(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_field_value'
    # Columns
    relation_id: int = Field(primary_key=True, foreign_key="xf_nf_rosters_user.relation_id")
    field_id: bytes = Field(primary_key=True)
    field_value: str
    # Relationships
    roster_user: "XfNfRostersUser" = Relationship(back_populates="fields")

class XfNfRostersPosition(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_position'
    # Columns
    position_id: int = Field(primary_key=True)
    position_title: str
    position_group_id: int
    # Relationships

class XfNfRostersPositionGroup(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_position_group'
    # Columns
    position_group_id: int = Field(primary_key=True)
    title: str
    # Relationships

class XfNfRostersRank(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_rank'
    # Columns
    rank_id: int = Field(primary_key=True)
    title: str
    # Relationships

class XfNfRostersRecordType(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_record_type'
    # Columns
    record_type_id: int = Field(primary_key=True)
    title: str
    # Relationships

class XfNfRostersRosterPosition(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_roster_position'
    # Columns
    roster_id: int = Field(primary_key=True)
    position_id: int
    # Relationships

class XfNfRostersServiceRecord(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_service_record'
    # Columns
    record_id: int = Field(primary_key=True)
    relation_id: int = Field(foreign_key="xf_nf_rosters_user.relation_id")
    details: str
    record_date: int
    citation_date: int
    record_type_id: int
    # Relationships
    roster_user: "XfNfRostersUser" = Relationship(back_populates="service_records")

class XfNfRostersUserAward(SQLModel, table=True):
    __tablename__ = 'xf_nf_rosters_user_award'
    # Columns
    record_id: int = Field(primary_key=True)
    relation_id: int = Field(foreign_key="xf_nf_rosters_user.relation_id")
    award_id: int
    details: str
    award_date: int
    citation_date: int
    # Relationships
    roster_user: "XfNfRostersUser" = Relationship(back_populates="awards")

