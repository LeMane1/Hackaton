from fastapi import (
    APIRouter,
    Depends,
    status,
    Request,
    HTTPException
)

from database.models import BaseUser, ItemType
from database.models import BaseMarketplaceItem
from marketplace.market_base_adapter import MarketDatabaseAdapter
from user.base_adapter import UserDatabaseAdapter
from user.routers import get_user_by_id, get_acc_by_user_id
from crypto.instructions import buy_nft, buy_crypto

router = APIRouter(
    prefix='/marketplace',
    tags=['marketplace'],
)


@router.get('/get_items/')
def get_items():
    items = MarketDatabaseAdapter.get_items()
    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")
    return items


@router.post('/add_item/')
def add_item(
        item: BaseMarketplaceItem,
):
    item_id = MarketDatabaseAdapter.create_item(item_model=item)
    return item_id


@router.get('/get_item_by_id/', status_code=200)
def get_item_by_id(item_id: int):
    item = MarketDatabaseAdapter.get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete('/delete_item_by_id/', status_code=200)
def delete_item_by_id(
        item_id: int,
):
    MarketDatabaseAdapter.delete_item(item_id=item_id)
    return 200


@router.post('/buy_nft/')
def buy_nft_route(
        item_id: int,
        user_id: int,
):
    buyer = get_user_by_id(user_id=user_id)
    item = get_item_by_id(item_id=item_id)
    seller = get_user_by_id(user_id=item.nft_owner_id)

    # transaction here
    buy_nft(nft_id=item.nft_id, buyer_public=buyer.public_key, seller_public=seller.public_key,
            buyer_private=buyer.private_key, seller_private=seller.private_key, roubles=item.cost)
    item.nft_owner_id = user_id  # temporary
    return 200


@router.post('/create_account/')
def create_account_route(
        currency_type: ItemType,
        user_id: int,
):
    account = UserDatabaseAdapter.create_account(user_id, currency_type.value)
    return 200


@router.post('/buy_currency/')
def buy_currency_route(
        currency_type: ItemType,
        amount: float,
        user_id: int,
):
    account = get_acc_by_user_id(user_id, currency_type)
    buy_crypto(account, amount)
    return 200
