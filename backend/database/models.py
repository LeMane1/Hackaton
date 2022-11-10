import datetime
import enum
from typing import List, Optional

from sqlalchemy import (
    Column,
    Integer,
    String,
    BOOLEAN,
    DATETIME,
    Enum, Float
)
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel

from database.database_adapter import engine

Base = declarative_base()


class ItemType(enum.Enum):
    AURC = "AURC"
    PTC = "PDC"
    PRC = "PDC"


class EventType(enum.Enum):
    REQUEST_TO_BANK = "REQUEST_TO_BANK"
    REQUEST_FROM_BANK = "REQUEST_FROM_BANK"


class DataUser(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)

    public_key = Column(String)
    private_key = Column(String)

    name = Column(String)
    email = Column(String)  # unique=True)


class DataEvent(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)

    description = Column(String)
    date_event = Column(DATETIME)
    creator = Column(Integer)  # id of creator user
    type = Column(Enum(EventType), default=None)
    city = Column(String)
    bank = Column(String)


class Account(Base):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True)

    type = Column(Enum(ItemType), default=None)
    amount = Column(Float)
    user_id = Column(Integer)


class DataMarketplaceItem(Base):
    __tablename__ = 'Market'

    id = Column(Integer, primary_key=True)

    type = Column(String)
    title = Column(String)
    description = Column(String)
    date = Column(String)
    cost = Column(Integer)
    currency = Column(String)
    photo = Column(String)
    nft_id = Column(Integer)
    nft_owner_id = Column(Integer)


Base.metadata.create_all(engine)


class CreateUserRequest(BaseModel):
    name: str
    email: str


class BaseUser(BaseModel):
    public_key: str
    private_key: str

    name: str
    email: str

    class Config:
        orm_mode = True


class ResponseUser(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserSeries(BaseModel):
    number_of_users: int = 0
    series: List[ResponseUser] = []


class BaseEvent(BaseModel):
    date_event: Optional[datetime.datetime]
    creator: Optional[int]  # id of creator user
    type: EventType
    city: str
    bank: str

    class Config:
        orm_mode = True


class ResponseEvent(BaseEvent):
    id: int

    class Config:
        orm_mode = True


class EventSeries(BaseModel):
    number_of_events: int = 0
    series: List[ResponseEvent] = []


class MetallicAccount(BaseModel):
    type = ItemType
    amount = float
    user_id = int

    class Config:
        orm_mode = True


class BaseMarketplaceItem(BaseModel):
    type: str
    title: str
    description: str
    date: str
    cost: int
    currency: str
    photo: str

    nft_id: Optional[int]
    nft_owner_id: Optional[int]

    class Config:
        orm_mode = True
