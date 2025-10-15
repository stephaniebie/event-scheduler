from scheduler.event import Event
from scheduler.sort import sort_data, SortingAlgorithm
from scheduler.search import search_data, SearchAlgorithm
from scheduler.defaults import INITIAL_ID, INITIAL_CAPACITY


class EventList:
    """
    An array-based list of events.
    """

    def __init__(self, capacity: int = INITIAL_CAPACITY):
        """
        Attributes
        ----------
        capacity: int
            Base size of the initialized static array
        events: list
            List of events
        size: int
            The number of events in the event list
        """
        # Initialize event ID counter
        self._id = INITIAL_ID
        # Initialize maximum capacity
        self.capacity = capacity
        # Initialize array size
        self.size = 0
        # Create static array
        self.events = [None] * self.capacity

    def __iter__(self):
        for i in range(self.size):
            yield self.events[i]

    def __getitem__(self, index: int | slice) -> Event | list:
        if 0<= index < self.size:
            return self.events[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index: int | slice, value: Event | list):
        # TODO: Maybe some conflict detection here?
        if isinstance(index, (int, slice)):
            self.events[index] = value
        else:
            raise TypeError(f"Invalid index type {type(index)}")

    def __len__(self):
        return self.size

    def _resize(self, new_capacity: int):
        """
        Increases the capacity of the list.

        Parameters
        ----------
        new_capacity: int
            The event list's new capacity
        """
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.events[i]
        self.events = new_data
        self.capacity = new_capacity

    def insert(self, event: Event, index: int = -1):
        """
        Insert an event at a specific index.
        Defaults to appending an event at the end of the list.

        Parameters
        ----------
        event: Event
            The event to be inserted
        index: int
            The index at which the event will be inserted
        """
        # Assert type of event
        if not isinstance(event, Event):
            raise TypeError(f"Cannot insert event of type {type(event)}")
        # Check if event overlaps with an existing event
        has_conflict = False
        for existing_event in self.events:
            # Reached end of list
            if existing_event is None:
                break
            # Calls collide_with function to check if new event collides with existing events
            if event.collides_with(existing_event):
                has_conflict = True
                break
        if has_conflict:
            raise ValueError("Conflict detected, cannot insert event")

        # Insert event if no conflict detected
        # Define index at end of list
        if index == -1:
            index = self.size
        # Resize list if size reaches capacity
        if self.size == self.capacity:
            self._resize(self.capacity + INITIAL_CAPACITY)
        # Validate index
        if index > self.size:
            raise IndexError(f"Index {index} is out of range")
        # Set event ID
        event.id = self._id
        # Add event to list
        self.events = (
            list(self.events[:index])
            + [event]
            + list(self.events[index : self.capacity])
        )
        # Sequentially generate a new ID upon insertion
        self._id += 1
        # Increment size
        self.size += 1

    def delete(self, index: int = -1, event: Event | None = None):
        """
        Remove an item fom the event list.

        Parameters
        ----------
        index: int
            The index at which to remove an event
        event: Event | None
            An event to be removed from the list
            If None, defaults to index-based deletion
        """
        # Delete at specific index
        if event is None:
            # Validate index
            if index + 1 > self.size:
                raise IndexError(f"Index {index} is out of range")
            if index == -1:
                index = self.size
                if self.size > 0:
                    index -= 1
            # Creates a list of indices to remove
            remove_index = [index]

        # Delete by matching event attributes
        else:
            # Creates a list of indices to remove
            remove_index = [i for i in range(self.size) if self.events[i] == event]

        # Removes event(s) from list, while preserving array capacity
        if remove_index:
            self.events = [
                e for i, e in enumerate(self.events) if i not in remove_index
            ] + [None] * len(set(remove_index))
            self.size -= len(set(remove_index))

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
        # Sort data before performing binary search
        if algorithm == SearchAlgorithm.BINARY:
            self = sort_data(data=self, attribute="_id")
        # Searches for ID in the list of events
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
        # Remove None values
        eventlist = self.events[: self.size]

        # Determine sorting algorithm
        if sort is True:
            sort = SortingAlgorithm.QUICK
        if sort:
            eventlist = sort_data(data=self, algorithm=sort).events[: self.size]
        return eventlist
