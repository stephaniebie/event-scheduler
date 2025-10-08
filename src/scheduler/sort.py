# PART B: Sorting Events
# Implementation of three sorting algorithms
from enum import Enum
from src.scheduler.event_array_list import EventList, LinkedEventList


def insertion_sort_list(data):
    raise NotImplementedError


def merge_sort_list(data):
    raise NotImplementedError


def quick_sort(data):
    raise NotImplementedError


class SortingAlgorithm(Enum):
    """
    Enumeration of different sorting algorithms
    """

    INSERTION = insertion_sort_list
    MERGE = merge_sort_list
    QUICK = quick_sort


def sort_data(
    data: EventList | LinkedEventList,
    algorithm: SortingAlgorithm = SortingAlgorithm.QUICK,
) -> EventList | LinkedEventList:
    """
    Sorts an event list using a specific algorithm.

    Parameters
    ----------
    data: EventList | LinkedEventList
        An event list object
    algorithm: SortingAlgorithm
        Enumeration value for a sorting algorithm
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SortingAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined sorting algorithm.")

    # Sorts the data using the specified algorithm
    return algorithm.value(data)
