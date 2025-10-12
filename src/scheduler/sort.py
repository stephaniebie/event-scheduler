# For use with type hints,,,
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scheduler.eventlist import EventList
    from scheduler.linkedeventlist import LinkedEventList

from enum import Enum, member
from scheduler.utils import parse_object


def insertion_sort(data, attribute: str | None = None):
    """
    Sorts data using the insertion sorting algorithm.

    Parameters
    ----------
    data
        The data to be sorted
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be used for sorting
        If None, matches each item

    Returns
    -------
    Sorted data
    """
    for i in range(1, len(data)):
        key = data[i].copy() if hasattr(data[i], "copy") else data[i]
        j = i - 1
        while j >= 0 and parse_object(key, attribute) < parse_object(
            data[j], attribute
        ):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def merge_sort(data, attribute: str | None = None):
    """
    Sorts data using the merge sorting algorithm.

    Parameters
    ----------
    data
        The data to be sorted
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be used for sorting
        If None, matches each item

    Returns
    -------
    Sorted data
    """
    if len(data) > 1:
        # Recursively divide the data into smaller parts
        middle_index = len(data) // 2
        left_data = [
            data[i].copy() if hasattr(data[i], "copy") else data[i]
            for i in range(middle_index)
        ]
        right_data = [
            data[i].copy() if hasattr(data[i], "copy") else data[i]
            for i in range(middle_index, len(data))
        ]

        merge_sort(data=left_data, attribute=attribute)
        merge_sort(data=right_data, attribute=attribute)

        i = j = k = 0

        # Merge the halves
        while i < len(left_data) and j < len(right_data):
            if parse_object(left_data[i], attribute) < parse_object(
                right_data[j], attribute
            ):
                data[k] = left_data[i]
                i += 1
            else:
                data[k] = right_data[j]
                j += 1
            k += 1

        # Add in the remaining elements that weren't merged in
        while i < len(left_data):
            data[k] = left_data[i]
            i += 1
            k += 1
        while j < len(right_data):
            data[k] = right_data[j]
            j += 1
            k += 1

        return data


def quick_sort(data, attribute: str | None = None):
    """
    Sorts data using the quick sorting algorithm. Chooses the first item in the list as a pivot.

    Parameters
    ----------
    data
        The data to be sorted
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be used for sorting
        If None, matches each item

    Returns
    -------
    Sorted data
    """

    def _partition(low, high):
        """
        Get partition index.
        """
        # Choose a pivot
        # NOTE: We are choosing a naive pivot strategy here to balance out the performance of sorting in a linked list
        pivot = data[low].copy() if hasattr(data[low], "copy") else data[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if parse_object(data[j], attribute) < parse_object(pivot, attribute):
                data[i], data[j] = data[j], data[i]
                i += 1
        data[low], data[i - 1] = data[i - 1], data[low]
        return i - 1

    def _sort(low, high):
        """
        Base sorting.
        """
        if low < high:
            partition_index = _partition(low, high)
            _sort(low, partition_index - 1)
            _sort(partition_index + 1, high)

    _sort(low=0, high=len(data) - 1)
    return data


class SortingAlgorithm(Enum):
    """
    Enumeration of different sorting algorithms
    """

    INSERTION = member(insertion_sort)
    MERGE = member(merge_sort)
    QUICK = member(quick_sort)


def sort_data(
    data: EventList | LinkedEventList,
    algorithm: SortingAlgorithm = SortingAlgorithm.QUICK,
    attribute: str | None = "start_time",
) -> EventList | LinkedEventList:
    """
    Sorts an event list by date and time using a specific algorithm.

    Parameters
    ----------
    data: EventList | LinkedEventList
        An event list object
    algorithm: SortingAlgorithm
        Enumeration value for a sorting algorithm
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be used for sorting

    Returns
    -------
    Sorted data as a list
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SortingAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined sorting algorithm.")

    # Sorts the data using the specified algorithm
    return algorithm.value(data=data, attribute=attribute)
