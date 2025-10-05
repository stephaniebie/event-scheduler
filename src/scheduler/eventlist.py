# PART A: Event Storage Structures
# An implementation of two independent ways of storing events
from scheduler.event import Event, EventNode


class EventList:
    """
    An array-based list of events.
    """

    def __init__(
        self,
        events: list[Event] = [],
    ):
        self.events = events

    def insert(self):
        # TODO
        raise NotImplementedError

    def delete(self):
        # TODO
        raise NotImplementedError

    def search_by_id(self):
        # TODO
        raise NotImplementedError

    def list_all(self):
        # TODO
        raise NotImplementedError


class LinkedEventList:
    """
    A singly linked list of events.
    """

    def __init__(
        self,
        head: None | EventNode = None,
    ):
        self.head = head

    def insert(self):
        # TODO
        raise NotImplementedError

    def delete(self):
        # TODO
        raise NotImplementedError

    def search_by_id(self):
        # TODO
        raise NotImplementedError

    def list_all(self):
        # TODO
        raise NotImplementedError
