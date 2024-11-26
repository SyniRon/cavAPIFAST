from sqlmodel import Session, select
from app.models.xf_user import xf_user

def get_user_by_username(session: Session, username: str):
    return session.exec(select(xf_user).where(xf_user.username == username)).first()