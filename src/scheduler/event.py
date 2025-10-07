class Event:
    """
    A unique campus event.
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
        self.datetime = None

        # NOTE: Uses strict string splicing which assumes no errors with date and time inputs
        #       If time permits, update this to catch possible invalid types or string formats
        if len(date) == 10 and len(time) == 5:
            # Date time of the form (year, month, day, hour, minute)
            self.datetime = tuple(
                int(d) for d in [date[:4], date[5:7], date[8:], time[:2], time[3:]]
            )

    # TODO add dunder eq, ne, and gt to be used for checking conflicts / overlaps


class EventNode(Event):
    """
    A unique campus event node for storage within a linked list.
    """

    def __init__(
        self,
        id: int,
        title: str,
        date: str,
        time: str,
        location: str,
        next: None | Event = None,
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
        next: None | Event
            The next event in a linked list of events
            If None, indicates the end of the list
        """
        super().__init__(
            id=id,
            title=title,
            date=date,
            time=time,
            location=location,
        )
        self.next = next
