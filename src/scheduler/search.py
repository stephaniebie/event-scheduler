# PART C: Searching & Conflict Detection
# Implements linear and binary search as well as an algorithm for checking if two or more events overlap in time
from enum import Enum
from scheduler.eventlist import EventList, LinkedEventList


def linear_search(data, target):
    raise NotImplementedError
    n = len(data)
    
    # Iterate over the array in order to
    # find the key x
    for i in range(0, n):
        if (arr[i] == target):
            return i
    return -1


def binary_search(data, target):
    raise NotImplementedError
    low = 0
    high = len(data) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == target:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


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
