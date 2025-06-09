import pytest
from main import ReservableItem, Event, Ticket, ReservationSystem

@pytest.fixture
def sample_event():
    return Event("Concert", 2, "2025-12-31")

@pytest.fixture
def ticket(sample_event):
    return Ticket("Alice", sample_event)

def test_reservable_item_str():
    item = ReservableItem("Room A", 10)
    assert str(item) == "Room A (10)"

def test_event_inheritance(sample_event):
    assert isinstance(sample_event, ReservableItem)

def test_event_add_ticket(sample_event):
    ticket1 = Ticket("Bob", sample_event)
    result = sample_event.add_ticket(ticket1)
    assert result is True
    assert len(sample_event) == 1

def test_event_add_ticket_overflow(sample_event):
    sample_event.add_ticket(Ticket("A", sample_event))
    sample_event.add_ticket(Ticket("B", sample_event))
    result = sample_event.add_ticket(Ticket("C", sample_event))
    assert result is False  # event capacity is 2

def test_ticket_equality(ticket, sample_event):
    same_ticket = Ticket("Alice", sample_event)
    other_ticket = Ticket("Bob", sample_event)
    assert ticket == same_ticket
    assert ticket != other_ticket

def test_reservation_system_add_and_find():
    system = ReservationSystem()
    event = Event("Workshop", 50, "2025-08-01")
    system.add_event(event)
    found = system.find_event("Workshop")
    assert found is event
    assert system.find_event("Nonexistent") is None
