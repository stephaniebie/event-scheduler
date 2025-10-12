# For use with type hints,,,
from __future__ import annotations

import datetime
from scheduler.defaults import EVENT_DURATION


class Event:
    """
    A unique campus event.
    """

    def __init__(
        self,
        title: str,
        date: str,
        time: str,
        location: str,
    ):
        """
        Parameters
        ----------
        title: str
            The title of the event
        date: str
            The date the event will take place in the form YYYY-MM-DD
        time: str
            The time the event will take place in the form HH:MM
        datetime: tuple | None
            A tuple composed of the inputted date and time
        location: str
            The location of the event
        """
        self.title = title
        self.location = location
        self.date = date
        self.time = time

        # Checks whether date and time are valid inputs
        try:
            self.start_time = datetime.datetime.strptime(
                f"{date} {time}", "%Y-%m-%d %H:%M"
            )
            # Create an event end time
            # TODO: Make duration a customizable parameter
            self.end_time = self.start_time + datetime.timedelta(seconds=EVENT_DURATION)
        except ValueError:
            raise ValueError(f"Invalid date '{date}' or time '{time}'")

        @property
        def id(self):
            """
            A unique event ID.
            """
            return self._id

        @id.setter
        def id(self, value: int):
            """
            Set the unique event ID value.

            Parameters
            ----------
            value: int
                Value to set as the event ID
            """
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"Cannot set ID to type {type(value)}")
            self._id = value

    def collides_with(self, other: Event):
        """
        Checks if two events overlap in time.

        Parameters
        ----------
        other: Event
            Another Event object
        """
        return self.start_time < other.end_time and other.start_time < self.end_time

    def __eq__(self, other: Event):
        """
        Determines if two instances of Event are equivalent. Equality is defined as exactly matching attributes.
        """
        if not isinstance(other, Event):
            raise TypeError(
                f"Cannot establish equality between Event and {type(other)}"
            )
        checked_attributes = ["title", "date", "time", "location", "id"]
        filter_attributes = lambda obj: {
            k: v for k, v in vars(obj).items() if k in checked_attributes
        }
        return filter_attributes(self) == filter_attributes(other)


class EventNode(Event):
    """
    A unique campus event node for storage within a linked list.
    """

    def __init__(
        self,
        title: str,
        date: str,
        time: str,
        location: str,
        next: EventNode | None = None,
    ):
        """
        Parameters
        ----------
        title: str
            The title of the event
        date: str
            The date the event will take place in the form YYYY-MM-DD
        time: str
            The time the event will take place in the form HH:MM
        datetime: tuple | None
            A tuple composed of the inputted date and time
        location: str
            The location of the event
        next: None | EventNode
            The next event in a linked list of events
            If None, indicates the end of the list
        """
        super().__init__(
            title=title,
            date=date,
            time=time,
            location=location,
        )
        self.next = next
