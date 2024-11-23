from email.policy import default
from enum import Enum

from fastapi import FastAPI

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

@app.get("/api/v1/milpac/keycloak/{keycloakId}")
async def say_hello(keycloakId: str):
    return {"message": f"Hello, {keycloakId}"}

@app.get("/api/v1/milpacs/profile/id/{userId}")
async def say_hello(userId: str):
    return {"message": f"Hello, {userId}"}

@app.get("/api/v1/milpacs/profile/username/{username}")
async def say_hello(username: str):
    return {"message": f"Hello, {username}"}

@app.get("/api/v1/roster/{roster}")
async def get_a_given_roster(roster_type: RosterType):
    return {"roster": roster_type}