from fastapi import HTTPException

from fastapi import APIRouter, Depends
from sqlmodel import Session


from app.core.database import get_session
from app.services.query_user import get_user_by_username
from app.schemas.profile import User
router = APIRouter()


@router.get('/username/{username}', response_model=User)
async def get_by_username(username: str, session: Session = Depends(get_session)):
    user = get_user_by_username(session, username)
    if not user:
        raise HTTPException(404, "Username not found")
    return user
