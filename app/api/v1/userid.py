from fastapi import HTTPException

from fastapi import APIRouter, Depends
from sqlmodel import Session


from app.core.database import get_session
from app.services.query_user import get_user_by_id
from app.services.query_rosters import get_roster_by_user_id, get_service_record_by_relation_id,\
    get_awards_by_relation_id, get_field_value_by_relation_id

from app.schemas.profile import Profile
router = APIRouter()

# response_model=Profile
@router.get('/id/{userId}')
async def get_by_id(user_id: int, session: Session = Depends(get_session)):
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(404, "User id not found")
    roster = get_roster_by_user_id(session, user_id)
    if not roster:
        raise HTTPException(404, "User found but not associated with any rosters")
    join_date, promo_date = get_field_value_by_relation_id(session, roster.relation_id)
    service_record = get_service_record_by_relation_id(session, roster.relation_id)
    awards = get_awards_by_relation_id(session, roster.relation_id)
    # TODO: build out return to match response model
    return {"username": user.username, "joinDate": join_date, "promoDate": promo_date, "serviceRecord": service_record, "awards": awards}
