from sqlmodel import Session, select
from app.models import user_models

def get_user_by_username(session: Session, username: str):
    return session.exec(select(user_models.xf_user).where(user_models.xf_user.username == username)).first()