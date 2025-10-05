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
        location: str
            The location of the event
        """
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.location = location


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
