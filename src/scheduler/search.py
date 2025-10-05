# PART C: Searching & Conflict Detection
# Implements linear and binary search as well as an algorithm for checking if two or more events overlap in time
from enum import Enum
from scheduler.eventlist import EventList, LinkedEventList


def linear_search(data, target):
    raise NotImplementedError


def binary_search(data, target):
    raise NotImplementedError


class SearchAlgorithm(Enum):
    LINEAR = linear_search
    BINARY = binary_search


def search_data(
    data: EventList | LinkedEventList,
    id: int,
    algorithm: SearchAlgorithm = SearchAlgorithm.BINARY,
) -> EventList | LinkedEventList:
    """
    Searches an event list using a specific algorithm.

    Parameters
    ----------
    data: EventList | LinkedEventList
        An event list object
    id: int
        A unique event ID to search for
    algorithm: SearchAlgorithm
        Enumeration value for a search algorithm
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SearchAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined search algorithm.")

    # Searches the data using the specified algorithm
    return algorithm.value(data=data, target=id)


# TODO conflict implementation
