# For use with type hints,,,
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scheduler.eventlist import EventList
    from scheduler.linkedeventlist import LinkedEventList

from enum import Enum, member
from scheduler.sort import sort_data
from scheduler.utils import parse_object
from scheduler.event import Event, EventNode


def linear_search(data, target, attribute: str | None = None):
    """
    Iteratively searches through an iterable for an item matching the target.

    Parameters
    ----------
    data
        An iterable object
    target
        Any item to match with an item of data
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be matched with the target
        If None, matches each item

    Returns
    -------
    The found item or None if not found
    """
    # Iterate through the iterable
    for datum in data:
        # Match to target
        if parse_object(datum, attribute) == target:
            return datum
    return None


def binary_search(data, target, attribute: str | None = None):
    """
    Searches through an iterable for an item matching the target using the classic binary search algorithm.
    NOTE: This algorithm assumes that data is already sorted.

    Parameters
    ----------
    data
        An iterable object
    target
        Any item to match with an item of data
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be matched with the target
        If None, matches each item

    Returns
    -------
    The found item or None if not found
    """
    # Initialize min and max indices
    low = 0
    high = len(data) - 1
    while low <= high:
        # Get middle index
        mid = (low + high) // 2
        # Get item from iterable
        datum = data[mid]
        # If target is found, return the item
        if parse_object(datum, attribute) == target:
            return datum
        # Keep splitting the list
        elif parse_object(datum, attribute) < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


class SearchAlgorithm(Enum):
    LINEAR = member(linear_search)
    BINARY = member(binary_search)


def search_data(
    data: EventList | LinkedEventList,
    target,
    algorithm: SearchAlgorithm = SearchAlgorithm.BINARY,
    attribute: str | None = "_id",
) -> Event | EventNode | None:
    """
    Searches for an event using a specific algorithm.

    Parameters
    ----------
    data: EventList | LinkedEventList
        List of events
    target
        Any item to match with an item of data
    algorithm: SearchAlgorithm
        Enumeration value for a search algorithm
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be matched with the target
        If None, matches each item

    Returns
    -------
    Found event as either an Event object, an EventNode object, or None if not found
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SearchAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined search algorithm.")

    # Searches the data using the specified algorithm
    return algorithm.value(data=data, target=target, attribute=attribute)
