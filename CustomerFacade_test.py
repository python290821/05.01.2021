import pytest
from CustomerFacade import *
from TicketAlreadyExistError import *

@pytest.fixture
def customer_facade_danny():
    # login will get customer_facade
    # return login('danny', '1234')
    return CustomerFacade()

def test_customer_facade_add_ticket(customer_facade_danny):
    ticket = { 'id': 0, 'customer_id': 1, 'flight_id': 2}
    customer_facade_danny.add_ticket(ticket)
    tickets = customer_facade_danny.get_ticket_by_customer({ 'id': 1, 'name': 'ticket'})
    assert ticket in tickets == True

def test_customer_facade_add_ticket_TicketAlreadyExistError(customer_facade_danny):
    ticket = { 'id': 0, 'customer_id': 1, 'flight_id': 2}
    with pytest.raises(TicketAlreadyExistError):
        customer_facade_danny.add_ticket(ticket)
        customer_facade_danny.add_ticket(ticket)



