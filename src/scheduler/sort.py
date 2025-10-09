# PART B: Sorting Events
# Implementation of three sorting algorithms
from enum import Enum, member
from scheduler.event import Event, EventNode


def insertion_sort(data: list) -> list:
    """
    Sorts data by time using the insertion sorting algorithm.

    Parameters
    ----------
    data: list
        List of Event or EventNode objects

    Returns
    -------
    Date-sorted list of Event or EventNode objects

    Authors
    -------
    Stephanie Bie
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        # Check if the key's start time is less than the next item's start time (iteratively)
        while j >= 0 and key.start_time < data[j].start_time:
            # Push over the sequential data
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def merge_sort(data: list) -> list:
    """
    Sorts data by time using the merge sorting algorithm.

    Parameters
    ----------
    data: list
        List of Event or EventNode objects

    Returns
    -------
    Date-sorted list of Event or EventNode objects

    Authors
    -------
    Stephanie Bie
    """
    if len(data) > 1:
        # Recursively divide the data into smaller parts
        middle_index = len(data) // 2
        left_data = data[:middle_index]
        right_data = data[middle_index:]
        merge_sort(left_data)
        merge_sort(right_data)

        # Initialize indices for traversing the halves
        i = j = k = 0

        # Merge the halves
        while i < len(left_data) and j < len(right_data):
            if left_data[i].start_time < right_data[j].start_time:
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


def quick_sort(data: list) -> list:
    """
    Sorts data by time using the quick sorting algorithm.

    Parameters
    ----------
    data: list
        List of Event or EventNode objects

    Returns
    -------
    Date-sorted list of Event or EventNode objects

    Authors
    -------
    Stephanie Bie
    """
    # Base case
    if len(data) <= 1:
        return data

    # For simplicity, the chosen pivot strategy is a midpoint approach
    pivot = data[len(data) // 2]

    # Split data into three sections (left, pivot, right)
    left_data = [d for d in data if d.start_time < pivot.start_time]
    middle_data = [d for d in data if d.start_time == pivot.start_time]
    right_data = [d for d in data if d.start_time > pivot.start_time]

    return quick_sort(left_data) + middle_data + quick_sort(right_data)


class SortingAlgorithm(Enum):
    """
    Enumeration of different sorting algorithms.

    Authors
    -------
    Stephanie Bie
    """

    INSERTION = member(insertion_sort)
    MERGE = member(merge_sort)
    QUICK = member(quick_sort)


def sort_data(
    data: list[Event | EventNode],
    algorithm: SortingAlgorithm = SortingAlgorithm.QUICK,
) -> list[Event | EventNode]:
    """
    Sorts an event list using a specific algorithm.

    Parameters
    ----------
    data: EventList | LinkedEventList
        An event list object
    algorithm: SortingAlgorithm
        Enumeration value for a sorting algorithm

    Returns
    -------
    Sorted data as a list

    Authors
    -------
    Stephanie Bie
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SortingAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined sorting algorithm.")

    # Sorts the data using the specified algorithm
    return algorithm.value(data)
