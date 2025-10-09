# PART C: Searching & Conflict Detection
# Implements linear and binary search as well as an algorithm for checking if two or more events overlap in time
from enum import Enum, member
from scheduler.event import Event, EventNode
from scheduler.sort import sort_data

# TODO implement for linked lists

def linear_search(data: list, target: int) -> Event | EventNode | None:
    """
    Iteratively searches through a list of events for an event matching the target ID.

    Parameters
    ----------
    data: list
        List of Event or EventNode objects
    target: int
        Unique event ID to search for

    Returns
    -------
    The found Event or EventNode, else None if not found

    Authors
    -------
    Dnyanada Bhosale
    """
    n = len(data)

    # Iterate over the array in order to
    # find the key x
    for i in range(0, n):
        if data[i].id == target:
            return data[i]
    return None


def binary_search(data: list, target: int) -> Event | EventNode | None:
    """
    Searches through a list of events for an event matching the target ID using the classic binary search algorithm.

    Parameters
    ----------
    data: list
        List of Event or EventNode objects
    target: int
        Unique event ID to search for

    Returns
    -------
    The found Event or EventNode, else None if not found

    Authors
    -------
    Dnyanada Bhosale
    """
    # Ensure the data is sorted
    data = sort_data(data)

    # Initialize indices
    low = 0
    high = len(data) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if data[mid].id == target:
            return data[mid]

        # If x is greater, ignore left half
        elif data[mid].id < target:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return None


class SearchAlgorithm(Enum):
    """
    Enumeration of different search algorithms.

    Authors
    -------
    Stephanie Bie
    """

    LINEAR = member(linear_search)
    BINARY = member(binary_search)


def search_data(
    data: list[Event | EventNode],
    id: int,
    algorithm: SearchAlgorithm = SearchAlgorithm.BINARY,
) -> Event | EventNode | None:
    """
    Searches for an event using a specific algorithm.

    Parameters
    ----------
    data: list
        List of events
    id: int
        A unique event ID to search for
    algorithm: SearchAlgorithm
        Enumeration value for a search algorithm

    Returns
    -------
    Found event as either an Event object, an EventNode object, or a Nonetype if not found

    Authors
    -------
    Stephanie Bie
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SearchAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined search algorithm.")

    # Searches the data using the specified algorithm
    return algorithm.value(data=data, target=id)
