from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)
from events.base_adapter import EventsDatabaseAdapter
from database.models import BaseEvent, ResponseEvent

router = APIRouter(
    prefix='/events', tags=['events']
)


@router.post('/create_bank_request/', status_code=201)
def create_post(event_model: BaseEvent):
    event_id = EventsDatabaseAdapter.create_event(event_model=event_model)
    return event_id


@router.post('/create_event/', status_code=201)
def create_post(event_model: BaseEvent):
    event_id = EventsDatabaseAdapter.create_event(event_model=event_model)
    return event_id


@router.get('/get_events/', status_code=201)
def get_events(left: int, right: int):
    return EventsDatabaseAdapter.get_events_list(left, right)


@router.put('/update_event/', status_code=201)
def update_post():
    return 'test'


@router.delete('/delete_event/', status_code=201)
def delete_post(evnet_id: int):
    EventsDatabaseAdapter.delete_event(evnet_id)
    return {'status': 'deleted'}
