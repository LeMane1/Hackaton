import json

from fastapi import (
    APIRouter
)
from bitcoinaddress import Wallet

import requests

from database.database_adapter import create_session
from database.models import Account

router = APIRouter(
    prefix='/marketplace',
    tags=['marketplace'],
)

MAIN_WALLET_KEYS = (
    '0x23079e657e898398c12e54D79BC191a193fA0e3b', 'e74439709384312484b9a545ae3d0cd55ca8f302b901e3446a30c3b30481ba72')


def create_wallet() -> (str, str):  # public key, private key
    wallet = Wallet()

    return wallet.address.pubkey, wallet.key.hex


def get_nft_balance(address: str) -> str:
    url = f"https://hackathon.lsp.team/hk/v1/wallets/{address}/nft/balance"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def transfer_nft(from_private: str, to_public: str, nft_id: int):
    pass


def buy_nft(nft_id: int, buyer_private: str, seller_public: str, seller_private: str, buyer_public: str,
            roubles: float):
    transfer_nft(nft_id=nft_id, to_public=buyer_public, from_private=seller_private)
    return 200


def buy_crypto(account_id: int, amount: float):
    with create_session() as session:
        account = session.query(Account).get(account_id)
        account.amount += amount
        session.commit()
