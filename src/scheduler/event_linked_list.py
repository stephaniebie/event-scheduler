from scheduler.event import Event, EventNode
from scheduler.search import search_data, SearchAlgorithm
from scheduler.sort import sort_data, SortingAlgorithm

class LinkedEventList:
    """
    A singly linked list of events.
    """

    def __init__(
        self,
        head: None | EventNode = None,
    ):
        self.head = head
        self.size = 0

    def insert(self, item: EventNode, index: int = -1):
        # TODO
        raise NotImplementedError

    def delete(self):
        # TODO
        raise NotImplementedError

    def search_by_id(self):
        # TODO
        raise NotImplementedError

    def list_all(self) -> list:
        # TODO
        raise NotImplementedError

