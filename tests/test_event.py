import pytest
from datetime import datetime
from scheduler.event import Event, EventNode


def test_event():
    # General event
    event = Event(
        title="A Sample Event!",
        date="2025-10-15",
        time="23:59",
        location="Education Building, Miramontes Baca 157",
    )
    assert event.title == "A Sample Event!"
    assert event.date == "2025-10-15"
    assert event.time == "23:59"
    assert event.start_time == datetime(2025, 10, 15, 23, 59)
    assert event.end_time == datetime(2025, 10, 16, 00, 59)
    assert event.location == "Education Building, Miramontes Baca 157"
    assert hasattr(event, "_id") is False

    # Setting an ID
    event.id = 1234
    assert event.id == 1234

    # Setting an invalid ID
    with pytest.raises(TypeError) as exception:
        event.id = "1234"
    assert f"Cannot set ID to type {str}" == str(exception.value)

    # Passing in an incorrectly formatted date
    with pytest.raises(ValueError) as exception:
        Event(
            title="A Sample Event!",
            date="20251015",
            time="23:59",
            location="Education Building, Miramontes Baca 157",
        )
    assert "Invalid date '20251015' or time '23:59'" == str(exception.value)

    # Passing in an incorrectly formatted time
    with pytest.raises(ValueError) as exception:
        Event(
            title="A Sample Event!",
            date="2025-10-15",
            time="2359",
            location="Education Building, Miramontes Baca 157",
        )
    assert "Invalid date '2025-10-15' or time '2359'" == str(exception.value)

    # Equality
    another_event = Event(
        title="A Sample Event!",
        date="2025-10-15",
        time="23:59",
        location="Education Building, Miramontes Baca 157",
    )
    assert event == another_event


def test_eventnode():
    # General event
    event = EventNode(
        title="A Sample Event!",
        date="2025-10-15",
        time="23:59",
        location="Education Building, Miramontes Baca 157",
    )
    assert event.title == "A Sample Event!"
    assert event.date == "2025-10-15"
    assert event.time == "23:59"
    assert event.start_time == datetime(2025, 10, 15, 23, 59)
    assert event.end_time == datetime(2025, 10, 16, 00, 59)
    assert event.location == "Education Building, Miramontes Baca 157"
    assert event.next is None
    assert hasattr(event, "_id") is False

    # Setting an ID
    event.id = 1234
    assert event.id == 1234

    # Setting an invalid ID
    with pytest.raises(TypeError) as exception:
        event.id = "1234"
    assert f"Cannot set ID to type {str}" == str(exception.value)

    # Passing in an incorrectly formatted date
    with pytest.raises(ValueError) as exception:
        EventNode(
            title="A Sample Event!",
            date="20251015",
            time="23:59",
            location="Education Building, Miramontes Baca 157",
        )
    assert "Invalid date '20251015' or time '23:59'" == str(exception.value)

    # Passing in an incorrectly formatted time
    with pytest.raises(ValueError) as exception:
        EventNode(
            title="A Sample Event!",
            date="2025-10-15",
            time="2359",
            location="Education Building, Miramontes Baca 157",
        )
    assert "Invalid date '2025-10-15' or time '2359'" == str(exception.value)

    # Equality
    another_event = EventNode(
        title="A Sample Event!",
        date="2025-10-15",
        time="23:59",
        location="Education Building, Miramontes Baca 157",
    )
    assert event == another_event

    # Copy
    copied_event = event.copy()
    copied_event.next = another_event
    assert event == copied_event
    assert event.next is not copied_event.next


def test_collides_with():
    event1 = Event(
        title="A Sample Event!",
        date="2025-10-15",
        time="23:59",
        location="Education Building, Miramontes Baca 157",
    )
    event2 = Event(
        title="Another Sample Event!",
        date="2025-10-16",
        time="00:58",
        location="Education Building, Miramontes Baca 157",
    )
    event3 = Event(
        title="A Sample Event!",
        date="2025-10-16",
        time="00:59",
        location="Education Building, Miramontes Baca 157",
    )
    assert event1.collides_with(event2)
    assert not event1.collides_with(event3)
