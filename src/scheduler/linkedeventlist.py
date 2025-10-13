from scheduler.event import EventNode
from scheduler.defaults import INITIAL_ID
from scheduler.sort import sort_data, SortingAlgorithm
from scheduler.search import SearchAlgorithm, search_data


class LinkedEventList:
    """
    A singly linked list of events.
    """

    def __init__(self):
        """
        Attributes
        ----------
        head: EventNode | Node
            The first event in the linked list
        size: int
            The number of events in the event list
        """
        # Initialize event ID counter
        self._id = INITIAL_ID
        # Initialize array size
        self.size = 0
        # Initialize first event in list
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __getitem__(self, index: int) -> EventNode:
        if isinstance(index, int):
            # Validate index
            if index < 0:
                index += self.size
            if index < 0 or index >= self.size:
                raise IndexError(f"Index {index} is out of range")
            # Get node
            node = self.head
            for _ in range(index):
                node = node.next
            return node.copy()
        else:
            raise TypeError(f"Invalid index type {type(index)}")

    def __setitem__(self, index: int, value: EventNode):
        # TODO: Maybe some conflict detection here?
        if isinstance(index, int):
            # Validate index
            if index < 0:
                index += self.size
            if index < 0 or index >= self.size:
                raise IndexError(f"Index {index} is out of range")
            # Set node
            node = self.head
            for _ in range(index):
                node = node.next
            for k, v in vars(value).items():
                if k not in ["next"]:
                    setattr(node, k, v)
            if "_id" not in vars(value):
                delattr(node, "_id")
        else:
            raise TypeError(f"Invalid index type {type(index)}")

    def __len__(self):
        return self.size

    def insert(self, event: EventNode, index: int = -1):
        """
        Insert an event at a specific index.
        Defaults to appending an event at the end of the list.

        Parameters
        ----------
        event: EventNode
            The event to be inserted
        index: int
            The index at which the event will be inserted
        """
        # Assert type of event
        if not isinstance(event, EventNode):
            raise TypeError(f"Cannot insert event of type {type(event)}")
        # Check if event overlaps with an existing event
        node = self.head
        while node:
            if event.collides_with(node):
                raise ValueError("Conflict detected, cannot insert event")
            node = node.next

        # Insert event if no conflict detected
        # Set event ID
        event.id = self._id
        # Validate index
        if index < 0:
            index += self.size + 1
        if index < 0:
            index = 0
        if index > self.size:
            raise IndexError(f"Index {index} is out of range")

        # Iterate through linked list to insert index
        node = self.head
        if node is None or index == 0:
            event.next = self.head
            self.head = event
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            event.next = node.next
            node.next = event

        # Sequentially generate a new ID upon insertion
        self._id += 1
        # Increment size
        self.size += 1

    def delete(self, index: int = -1, event: EventNode | None = None):
        """
        Remove an item fom the event list.

        Parameters
        ----------
        index: int
            The index at which to remove an event
        event: EventNode | None
            An event to be removed from the list
            If None, defaults to index-based deletion
        """
        # Deal with empty list
        if self.head is None:
            raise IndexError("Trying to delete from empty list")
        # Delete at specific index
        if event is None:
            # Validate index
            if index < 0:
                index += self.size
            if index < 0 or index >= self.size:
                raise IndexError(f"Index {index} is out of range")

            # Remove node at specific index
            if index == 0:
                self.head = self.head.next
            else:
                node = self.head
                prev_node = None
                if node is not None:
                    for _ in range(index):
                        prev_node = node
                        node = node.next
                    prev_node.next = node.next

            # Decrease size of list
            self.size -= 1

        # Delete by matching event attributes
        else:
            node = self.head
            prev_node = None
            while node:
                if node == event:
                    if prev_node is None:
                        self.head = node.next
                        # Decrease size of list
                        self.size -= 1
                        print('block1',node.title)
                        break
                    else:
                        prev_node.next = node.next
                        # Decrease size of list
                        self.size -= 1
                        print(node.title)
                        break
                prev_node = node
                node = node.next

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
        # Sort data before performing binary search
        if algorithm == SearchAlgorithm.BINARY:
            self = sort_data(data=self, attribute="_id")
        found_event = search_data(data=self, target=id, algorithm=algorithm)
        if found_event is None:
            raise ValueError(f"Could not find ID {id} in event list")
        return found_event

    def list_all(self, sort: bool | SortingAlgorithm = True) -> list:
        """
        Displays all events in a list.

        Parameters
        ----------
        sort: bool | SortingAlgorithm
            Determines if returned list should be sorted by date and time
            If True, defaults to using the quick sort algorithm

        Returns
        -------
        List of all events
        """
        # Initialize an empty list
        eventlist = []

        # Determine sorting algorithm
        if sort is True:
            sort = SortingAlgorithm.QUICK
        if sort:
            node = sort_data(data=self, algorithm=sort).head
        else:
            node = self.head
        # Construct list
        while node:
            eventlist.append(node)
            node = node.next
        return eventlist
