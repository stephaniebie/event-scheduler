import pytest
from random import shuffle
from scheduler.event import Event
from datetime import datetime, timedelta
from scheduler.eventlist import EventList
from scheduler.search import SearchAlgorithm
from scheduler.defaults import INITIAL_CAPACITY, INITIAL_ID


# Initialize event list
event_list = EventList()
num_events = 25

# Create random indices
indices = list(range(num_events))
shuffle(indices)

# Add events to list (unsorted in time)
for i, idx in enumerate(indices):
    dt = datetime.strftime(
        datetime(2025, 10, 15) + timedelta(hours=idx), "%Y-%m-%d %H:%M"
    )
    date, time = dt.split(" ")
    event_list.insert(
        Event(
            title=f"Event {i + 1}", date=date, time=time, location=f"Location {idx + 1}"
        )
    )

new_event = Event(title="", date="2050-10-15", time="23:59", location="")


def test_magic_functions():
    # Length
    assert len(event_list) == num_events

    # Iterator
    for e in event_list:
        assert isinstance(e, Event)

    # Getitem
    assert isinstance(event_list[0], Event)

    # Setitem
    original_event = event_list[2]
    event_list[2] = new_event
    assert event_list.events[2] != original_event
    assert event_list.events[2] == new_event
    event_list[2] = original_event
    # Catch type errors
    with pytest.raises(TypeError) as exception:
        event_list["invalid_index"] = new_event
    assert f"Invalid index type {str}" == str(exception.value)


def test_resize():
    # Initialize event list
    another_event_list = EventList()
    assert len(another_event_list.events) == INITIAL_CAPACITY

    # Resize the array
    another_event_list._resize(new_capacity=INITIAL_CAPACITY + 10)
    assert len(another_event_list.events) == INITIAL_CAPACITY + 10
    assert another_event_list.capacity == INITIAL_CAPACITY + 10


def test_insert():
    # Check the order of the IDs
    expected_ids = sorted([i + 1 for i in indices]) + [None] * 6
    actual_ids = [event.id if event else event for event in event_list.events]
    assert actual_ids == expected_ids

    # Catch conflicts
    with pytest.raises(ValueError) as exception:
        event_list.insert(
            Event(title="Conflicting Event", date=date, time=time, location="Anywhere")
        )
    assert "Conflict detected, cannot insert event" == str(exception.value)

    # Insert at index
    event_list.insert(event=new_event, index=1)
    assert event_list.events[1] == new_event
    assert event_list[1] == new_event
    event_list.delete(event=new_event)
    with pytest.raises(IndexError) as exception:
        event_list.insert(
            event=new_event,
            index=1000,
        )
    assert "Index 1000 is out of range" == str(exception.value)
    event_list.delete(event=new_event)


def test_delete():
    # Delete by index
    index = 5
    original_event = event_list[index]
    event_list.delete(index=index)
    assert event_list[index] != original_event
    assert (
        sum(
            [event == original_event if event else False for event in event_list.events]
        )
        == 0
    )
    event_list.insert(original_event, index=index)

    # Delete by event
    event_list.delete(event=original_event)
    assert event_list[index] != original_event
    assert (
        sum(
            [event == original_event if event else False for event in event_list.events]
        )
        == 0
    )
    event_list.insert(original_event, index=index)


def test_search_by_id():
    event_id = 10
    found_event = event_list.search_by_id(id=event_id, algorithm=SearchAlgorithm.LINEAR)
    dt = datetime.strftime(
        datetime(2025, 10, 15) + timedelta(hours=indices[event_id - 1]),
        "%Y-%m-%d %H:%M",
    )
    date, time = dt.split(" ")
    expected_event = Event(
        title=f"Event {event_id}",
        date=date,
        time=time,
        location=f"Location {indices[event_id-1] + 1}",
    )
    expected_event.id = event_id
    assert found_event == expected_event


def test_list_all():
    # Check unsorted list
    actual = [event.location for event in event_list.list_all(sort=False)]
    expected = [f"Location {i + 1}" for i in indices]
    assert actual == expected

    # Check sorted list
    actual = [event.location for event in event_list.list_all()]
    expected = [f"Location {i + 1}" for i in range(num_events)]
    assert actual == expected
