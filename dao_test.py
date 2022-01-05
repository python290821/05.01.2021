import pytest
from dao import Dao
import time

@pytest.fixture(scope='session', autouse=True)
def dao_init():
    time.sleep(3)
    print('setting up stuff')
    yield()
    print('cleanup')
    time.sleep(3)

@pytest.fixture(scope='session')
def dao_connection():
    print('setting up dao')
    return Dao()

def test_get_all(dao_connection):
    assert dao_connection.get_all() == [1, 2, 3, 4, 5]

def test_get_first(dao_connection):
    assert dao_connection.get_first() == 1]

