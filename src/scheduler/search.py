# PART C: Searching & Conflict Detection
# Implements linear and binary search as well as an algorithm for checking if two or more events overlap in time
from enum import Enum, member
from scheduler.event import Event, EventNode
from scheduler.sort import sort_data


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
    The found Event or EventNode
    """
    for datum in data:
        if datum.id == target:
            return datum
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
    The found Event or EventNode
    """
    # Ensure the data is sorted
    data = sort_data(data)

    # Classic binary search algorithm
    left_index, right_index = 0, len(data) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        datum = data[middle_index]
        if datum.id == target:
            return datum
        elif datum.id < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return None


class SearchAlgorithm(Enum):
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
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SearchAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined search algorithm.")

    # Searches the data using the specified algorithm
    return algorithm.value(data=data, target=id)


# TODO conflict implementation
