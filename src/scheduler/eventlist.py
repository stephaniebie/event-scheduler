# PART A: Event Storage Structures
# An implementation of two independent ways of storing events
from scheduler.event import Event, EventNode
from scheduler.search import search_data, SearchAlgorithm
from scheduler.sort import sort_data, SortingAlgorithm


class EventList:
    """
    An array-based list of events.
    """

    def __init__(
        self,
        capacity: int = 10,
    ):
        """
        Attributes
        ----------
        capacity: int
            Base size of the initialized static array
        size: int
            Number of events in the list
        events: list
            The list of all events
        """
        # Initialize maximum capacity
        self.capacity = capacity
        # Initialize array size
        self.size = 0
        # Create a static array
        self.events = [None] * self.capacity

    def insert(self, item: Event, index: int = -1):
        """
        Insert an event at a specific index. Defaults to appending an event at the end of the list.

        Parameters
        ----------
        item: Event
            The event to be inserted
        index: int
            The index at which the event will be inserted
        """
        if index == -1:
            index = self.size
        if self.size > self.capacity:
            self.capacity = self.size
        if index > self.size:
            raise IndexError(f"Index {index} is out of range")
        else:
            self.events = (
                list(self.events[:index])
                + [None]
                + list(self.events[index : self.capacity])
            )
            self.size += 1
        self.events[index] = item

    def delete(self, index: int = -1):
        """
        Remove an item fom the event list at a certain index. Defaults to removing last item in list.

        Parameters
        ----------
        index: int
            The index at which to remove an event
        """
        if index + 1 > self.size:
            raise IndexError(f"Index {index} is out of range")
        if index == -1:
            index = self.size
            if self.size > 0:
                index -= 1
        self.events = [e for i, e in enumerate(self.events) if i != index]
        self.events += [None]
        self.size -= 1

    def search_by_id(
        self, id: int, algorithm: SearchAlgorithm = SearchAlgorithm.BINARY
    ) -> Event:
        """
        Searches for an event using an ID.

        Parameters
        ----------
        id: int
            The target ID to search for
        algorithm: SearchAlgorithm
            The SearchAlgorithm enumeration that determines which search algorithm to use

        Returns
        -------
        The Event object that was found
        """
        found_event = search_data(data=self.list_all(), id=id, algorithm=algorithm)
        if found_event is None:
            raise ValueError(f"Could not find ID {id} in event list")
        return found_event

    def list_all(self) -> list:
        """
        Displays all events in a list.

        Returns
        -------
        List of all events
        """
        return [e for e in self.events if e is not None]

    def sort(self, algorithm: SortingAlgorithm = SortingAlgorithm.QUICK):
        """
        Sorts events by date and time.
        """
        self.events = sort_data(data=self.list_all(), algorithm=algorithm)


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
        """
        Insert an event at a specific index. Defaults to appending an event at the end of the list.

        Parameters
        ----------
        item: EventNode
            The event to be inserted
        index: int
            The index at which the event will be inserted
        """
        # Validate index
        if index == -1:
            index = self.size
        elif index + 1 > self.size:
            raise IndexError(f"Index {index} is out of range")
        # Iterate through linked list to insert index
        node = self.head
        if node is None:
            self.head = item
            item.next = None
        else:
            while index > 1:
                index -= 1
                node = node.next
            item.next = node.next
            node.next = item
        # Increase size of list
        self.size += 1

    def delete(self):
        # TODO
        raise NotImplementedError

    def search_by_id(
        self, id: int, algorithm: SearchAlgorithm = SearchAlgorithm.BINARY
    ) -> EventNode:
        """
        Searches for an event using an ID.

        Parameters
        ----------
        id: int
            The target ID to search for
        algorithm: SearchAlgorithm
            The SearchAlgorithm enumeration that determines which search algorithm to use

        Returns
        -------
        The EventNode object that was found
        """
        found_event = search_data(data=self.list_all(), id=id, algorithm=algorithm)
        if found_event is None:
            raise ValueError(f"Could not find ID {id} in event list")
        return found_event

    def list_all(self) -> list:
        """
        Displays all events in a list.

        Returns
        -------
        List of all events
        """
        events = []
        node = self.head
        while node:
            events.append(node)
            node = node.next
        return events

    def sort(self, algorithm: SortingAlgorithm = SortingAlgorithm.QUICK):
        """
        Sorts events by date and time.
        """
        events = sort_data(data=self.list_all(), algorithm=algorithm)
        if len(events) >= 1:
            self.head = events[0]
            if len(events) > 1:
                node = self.head
                for event in events[1:]:
                    node.next = event
                    node = event
                node.next = None
