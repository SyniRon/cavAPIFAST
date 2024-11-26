from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models import xf_user
from app.core.database import get_session
from app.services.username import get_user_by_username

router = APIRouter()


@router.get('/username/{username}')
def get_by_username(username: str, session: Session = Depends(get_session)):
    user = get_user_by_username(session, username)
    if not user:
        raise HTTPException(status_code=404, detail="Username not found")
    return user