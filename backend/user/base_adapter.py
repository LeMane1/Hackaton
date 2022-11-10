from typing import Optional, Union

from database.models import BaseUser, UserSeries, DataUser, ResponseUser, Account
from database.database_adapter import create_session

from sqlalchemy import or_
from sqlalchemy import and_


class UserDatabaseAdapter:
    @staticmethod
    def create_user(user_model: BaseUser) -> int:
        print('call create_user fun\n', user_model)
        with create_session() as session:
            user = DataUser(**user_model.dict())
            session.add(user)
            session.flush()
            user_id = user.id
        return user_id

    @staticmethod
    def delete_user(user_id: int) -> None:
        with create_session() as session:
            session.query(DataUser).filter(DataUser.id == user_id).delete()

    @staticmethod
    def add_event(user_id: int):
        with create_session() as session:
            user_model = session.query(DataUser).get(user_id)
            user_model.events_count += 1
            session.commit()
            return user_model

    @staticmethod
    def update_user(user_id: int) -> None:
        pass

    @staticmethod
    def get_user_by_id(post_id: int) -> Union[BaseUser, None]:
        with create_session() as session:
            user_model = session.query(DataUser).get(post_id)
            if user_model is None:
                post = None
            else:
                post = BaseUser.from_orm(user_model)
        return post

    @staticmethod
    def create_account(user_id: int, currency: str) -> Union[Account, None]:
        with create_session() as session:
            acc = Account(**{"user_id": user_id, "type": currency, "amount": 0})
            session.add(acc)
            session.flush()
            acc_id = acc.id
        return acc_id

    @staticmethod
    def get_acc_by_user_id(user_id: int, currency: str) -> int:
        with create_session() as session:
            acc = session.query(Account).filter(Account.user_id==user_id, Account.type==currency).first()
            if acc is None:
                return None
            acc_id = acc.id
        return acc_id

    def get_acc_balance(user_id: int, currency: str) -> (float, str):
        with create_session() as session:
            acc = session.query(Account).filter(Account.user_id==user_id, Account.type==currency).first()
            if acc is None:
                return None
            acc_balance = acc.amount
            acc_cur = acc.type
        return acc_balance, acc_cur

    @staticmethod
    def get_users_list(left: int, right: int) -> Union[ResponseUser, None]:
        with create_session() as session:
            data_list = session.query(DataUser)[left:right]
            user_series = UserSeries()
            for data_user in data_list:
                user_series.series.append(ResponseUser.from_orm(data_user))
                user_series.number_of_users += 1

        return user_series
