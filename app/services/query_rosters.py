from sqlmodel import Session, select
from app.models import nf_roster_models

def get_roster_by_user_id(session: Session, user_id: int):
    return session.exec(select(nf_roster_models.xf_nf_rosters_user).where(nf_roster_models.xf_nf_rosters_user.user_id == user_id)).first()

def get_field_value_by_relation_id(session: Session, relation_id: int):
    results = session.exec(select(nf_roster_models.xf_nf_rosters_field_value).where(nf_roster_models.xf_nf_rosters_field_value.relation_id == relation_id)).all()
    print(results)
    field_values = {result.field_id.decode('utf-8'): result.field_value for result in results}
    print(field_values)
    join_date = field_values.get('joinDate', "")
    promo_date = field_values.get('promoDate', "")
    print(join_date)
    print(promo_date)
    return join_date, promo_date

def get_service_record_by_relation_id(session: Session, relation_id: int):
    return session.exec(select(nf_roster_models.xf_nf_rosters_service_record).where(nf_roster_models.xf_nf_rosters_service_record.relation_id == relation_id)).all()

def get_awards_by_relation_id(session: Session, relation_id: int):
    return session.exec(select(nf_roster_models.xf_nf_rosters_user_award).where(nf_roster_models.xf_nf_rosters_user_award.relation_id == relation_id)).all()