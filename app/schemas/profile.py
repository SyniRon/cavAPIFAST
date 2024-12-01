from typing import List
from pydantic import BaseModel, Field
from app.schemas.schema_enums import RecordType, RosterType

class User(BaseModel):
    userId: int = Field(..., validation_alias="user_id")
    username: str

class Rank(BaseModel):
    rankShort: str
    rankFull: str
    rankImageUrl: str
    rankId: int

class Position(BaseModel):
    positionTitle: str
    positionId: int

class Record(BaseModel):
    recordDetails: str
    recordType: RecordType = RecordType.RECORD_TYPE_UNSPECIFIED
    recordDate: str

class Award(BaseModel):
    awardDetails: str
    awardName: str
    awardDate: str
    awardImageUrl: str

class Profile(BaseModel):
    user: User
    rank: Rank
    realName: str
    uniformUrl: str
    roster: RosterType = RosterType.ROSTER_TYPE_UNSPECIFIED
    primary: Position
    secondaries: List[Position] = Field(default_factory=list)
    records: List[Record] = Field(default_factory=list)
    awards: List[Award] = Field(default_factory=list)
    joinDate: str
    promotionDate: str
    keycloakId: str
