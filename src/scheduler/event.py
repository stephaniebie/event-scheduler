import datetime


class Event:
    """
    A unique campus event.

    Authors
    -------
    Augustine Joy
    """

    def __init__(
        self,
        id: int,
        title: str,
        date: str,
        time: str,
        location: str,
    ):
        """
        Attributes
        ----------
        id: int
            A unique event ID
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

        self.id = id
        self.title = title
        self.location = location
        self.date = date
        self.time = time

        # Checks whether date and time are valid inputs and returns None if its invalid.
        try:
            self.start_time = datetime.datetime.strptime(
                f"{date} {time}", "%Y-%m-%d %H:%M"
            )
            self.end_time = self.start_time + datetime.timedelta(hours=1)
        except ValueError:
            raise ValueError(f"Invalid date '{date}' or time '{time}'")

    # Function to check whether new event collides with other existing events.
    def collides_with(self, other):
        return self.start_time < other.end_time and other.start_time < self.end_time

    def __eq__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time == other.start_time

    def __ne__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time != other.start_time

    def __gt__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time > other.start_time

    def __lt__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time < other.start_time


class EventNode(Event):
    """
    A unique campus event node for storage within a linked list.

    Attributes
    ----------
    id: int
        A unique event ID
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
    next: None | Event
        The next event in a linked list of events
        If None, indicates the end of the list

    Authors
    -------
    Stephanie Bie
    """

    def __init__(
        self,
        id: int,
        title: str,
        date: str,
        time: str,
        location: str,
        next: None | "EventNode" = None,
    ):
        super().__init__(
            id=id,
            title=title,
            date=date,
            time=time,
            location=location,
        )
        self.next = next
