# test_wallet.py
import pytest
from Wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet_with_20():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

@pytest.mark.set_empty_wallet
def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet_with_20):
    assert wallet_with_20.balance == 20

def test_wallet_add_cash(wallet_with_20):
    wallet_with_20.add_cash(80)
    assert wallet_with_20.balance == 100

def test_wallet_spend_cash(wallet_with_20):
    wallet_with_20.spend_cash(10)
    assert wallet_with_20.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)