from email.policy import default

from sqlmodel import SQLModel, Field, create_engine, Session, select
from enum import Enum
import os
from dotenv import load_dotenv

from fastapi import FastAPI, Depends, HTTPException

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"mariadb+mariadbconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class RosterType(str, Enum):
    ROSTER_TYPE_UNSPECIFIED = "ROSTER_TYPE_UNSPECIFIED"
    ROSTER_TYPE_COMBAT = "ROSTER_TYPE_COMBAT"
    ROSTER_TYPE_RESERVE ="ROSTER_TYPE_RESERVE"
    ROSTER_TYPE_ELOA = "ROSTER_TYPE_ELOA"
    ROSTER_TYPE_WALL_OF_HONOR = "ROSTER_TYPE_WALL_OF_HONOR"
    ROSTER_TYPE_ARLINGTON = "ROSTER_TYPE_ARLINGTON"
    ROSTER_TYPE_PAST_MEMBERS = "ROSTER_TYPE_PAST_MEMBERS"

app = FastAPI(
    title="FAST cavAPI",
    docs_url="/",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

class xf_user(SQLModel):
    user_id: int = Field(primary_key=True)
    username: str

class xf_nf_rosters_user(SQLModel):
    relation_id: int = Field(primary_key=True)
    roster_id: int
    user_id: int
    real_name: str
    position_id: int
    secondary_position_ids: int
    rank_id: int
    custom_fields: str

class UserResponse(SQLModel):
    user: xf_user
    rosters_user: xf_nf_rosters_user

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/api/v1/milpac/keycloak/{keycloakId}")
async def say_hello(keycloakId: str):
    return {"message": f"Hello, {keycloakId}"}

@app.get("/api/v1/milpacs/profile/id/{userId}")
async def say_hello(userId: str):
    return {"message": f"Hello, {userId}"}

@app.get("/api/v1/milpacs/profile/username/{username}", response_model=UserResponse)
async def get_a_given_user(username: str, session: Session = Depends(get_session)):
    xf_user_statement = select(xf_user).where(xf_user.username == username)
    xf_user_results = session.exec(xf_user_statement).first()
    xf_nf_rosters_user_statement = select(xf_nf_rosters_user).where(xf_nf_rosters_user.user_id == xf_user_results.user_id)
    xf_nf_rosters_user_results = session.exec(xf_nf_rosters_user_statement).first()
    if not xf_user_results:
           raise HTTPException(404, "Username not found")
    user_data = xf_user(
        username=xf_user_results.username,
        user_id=xf_user_results.user_id,
    )
    roster_data = xf_nf_rosters_user(
        relation_id=xf_nf_rosters_user_results.relation_id,
        roster_id=xf_nf_rosters_user_results.roster_id,
        real_name=xf_nf_rosters_user_results.real_name,
        position_id=xf_nf_rosters_user_results.position_id,
        secondary_position_ids=xf_nf_rosters_user_results.secondary_position_ids,
        rank_id=xf_nf_rosters_user_results.rank_id,
        custom_fields=xf_nf_rosters_user_results.custom_fields,
    )

    return UserResponse(user=user_data, roster=roster_data)

@app.get("/api/v1/roster/{roster}")
async def get_a_given_roster(roster_type: RosterType):
    return {"roster": roster_type}



