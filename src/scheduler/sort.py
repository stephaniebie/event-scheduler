# PART B: Sorting Events
# Implementation of three sorting algorithms
from enum import Enum, member
from scheduler.event import Event, EventNode


def insertion_sort(data: list) -> list:
    data_length = len(data)
    for i in range(1, data_length):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j].datetime > key.datetime:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def merge_sort(data: list) -> list:
    if len(data) > 1:
        # Recursively divide the data into smaller parts
        middle_index = len(data) // 2
        left_data = data[:middle_index]
        right_data = data[middle_index:]

        merge_sort(left_data)
        merge_sort(right_data)

        i = j = k = 0

        # Merge the halves
        while i < len(left_data) and j < len(right_data):
            if left_data[i].datetime < right_data[j].datetime:
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
    if len(data) <= 1:
        return data

    # Choose a pivot
    pivot = data[len(data) // 2]

    # Split data into three sections (left, pivot, right)
    left_data = [d for d in data if d.datetime < pivot.datetime]
    middle_data = [d for d in data if d.datetime == pivot.datetime]
    right_data = [d for d in data if d.datetime > pivot.datetime]

    return quick_sort(left_data) + middle_data + quick_sort(right_data)


class SortingAlgorithm(Enum):
    """
    Enumeration of different sorting algorithms
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
    """
    # Further enforces the algorithm enumeration
    if algorithm not in list(SortingAlgorithm):
        raise ValueError(f"{algorithm} is an invalid or undefined sorting algorithm.")

    # Sorts the data using the specified algorithm
    return algorithm.value(data)
