from typing import Optional, Union

from database.models import BaseEvent, EventSeries, DataEvent, ResponseEvent
from database.database_adapter import create_session

from sqlalchemy import or_
from sqlalchemy import and_


class EventsDatabaseAdapter:
    @staticmethod
    def create_event(event_model: BaseEvent) -> int:
        print('call create_event fun\n', event_model)
        with create_session() as session:
            event = DataEvent(**event_model.dict())
            session.add(event)
            session.flush()
            event_id = event.id
        return event_id

    @staticmethod
    def update_event(event_id: int) -> None:
        pass

    @staticmethod
    def delete_event(event_id: int) -> None:
        with create_session() as session:
            event = session.query(DataEvent).filter(DataEvent.id == event_id).delete()

    @staticmethod
    def get_events_list(left: int, right: int) -> Union[ResponseEvent, None]:
        with create_session() as session:
            data_list = session.query(DataEvent)[left:right]
            event_series = EventSeries()
            for data_event in data_list:
                event_series.series.append(ResponseEvent.from_orm(data_event))
                event_series.number_of_events += 1

        return event_series
