from sqlmodel import Session, select
from app.models import xenforo_models

def get_user_by_username(session: Session, username: str):
    return session.exec(select(xenforo_models.xf_user).where(xenforo_models.xf_user.username == username)).first()

def get_user_by_id(session: Session, user_id: int):
    return session.exec(select(xenforo_models.xf_user).where(xenforo_models.xf_user.user_id == user_id)).first()