from sqlmodel import Session, select
from app.models import xenforo_models

def get_roster_by_user_id(session: Session, user_id: int):
    return session.exec(select(xenforo_models.XfNfRostersUser).where(xenforo_models.XfNfRostersUser.user_id == user_id)).first()

def get_field_value_by_relation_id(session: Session, relation_id: int):
    results = session.exec(select(xenforo_models.XfNfRostersFieldValue).where(xenforo_models.XfNfRostersFieldValue.relation_id == relation_id)).all()
    field_values = {result.field_id.decode('utf-8'): result.field_value for result in results}
    join_date = field_values.get('joinDate', "")
    promo_date = field_values.get('promoDate', "")
    return join_date, promo_date

def get_service_record_by_relation_id(session: Session, relation_id: int):
    return session.exec(select(xenforo_models.XfNfRostersServiceRecord).where(xenforo_models.XfNfRostersServiceRecord.relation_id == relation_id)).all()

def get_awards_by_relation_id(session: Session, relation_id: int):
    return session.exec(select(xenforo_models.XfNfRostersUserAward).where(xenforo_models.XfNfRostersUserAward.relation_id == relation_id)).all()