# For use with type hints,,,
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scheduler.eventlist import EventList
    from scheduler.linkedeventlist import LinkedEventList

from enum import Enum, member
from scheduler.event import EventNode
from scheduler.utils import parse_object


def insertion_sort(
    data: list | EventNode, attribute: str | None = None
) -> list | EventNode:
    """
    Sorts data using the insertion sorting algorithm.

    Parameters
    ----------
    data: list | EventNode
        The data to be sorted
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be used for sorting
        If None, matches each item

    Returns
    -------
    Sorted list or linked list node
    """
    # Insertion sort algorithm for lists
    if isinstance(data, list):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and parse_object(key, attribute) < parse_object(
                data[j], attribute
            ):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

    # Insertion sort algorithm for linked lists
    elif isinstance(data, EventNode):
        if not data or not data.next:
            return data
        temp_node = None
        current = data
        while current:
            next_node = current.next
            if not temp_node or parse_object(current, attribute) <= parse_object(
                temp_node, attribute
            ):
                current.next = temp_node
                temp_node = current
            else:
                temp_current = temp_node
                while temp_current.next and parse_object(
                    temp_current.next, attribute
                ) < parse_object(current, attribute):
                    temp_current = temp_current.next
                current.next = temp_current.next
                temp_current.next = current
            current = next_node
        return temp_node

    else:
        raise TypeError("Invalid datatype!!!")


def merge_sort(
    data: list | EventNode, attribute: str | None = None
) -> list | EventNode:
    """
    Sorts data using the merge sorting algorithm.

    Parameters
    ----------
    data: list | EventNode
        The data to be sorted
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be used for sorting
        If None, matches each item

    Returns
    -------
    Sorted list or linked list node
    """
    if isinstance(data, list):
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

    elif isinstance(data, EventNode):
        """Function for merging two halves"""

        def merge(left_node, right_node):
            """
            Need a dummy node but None will probably fail because our
            EventNode constructor needs valid input.
            Need to explore other options - Looks like we need to pass dummy values
            """
            temp = EventNode(None)  # Will probably fail on execution
            tail = temp
            while left_node and right_node:
                if parse_object(left_node, attribute) <= parse_object(
                    right_node, attribute
                ):
                    tail.next = left_node
                    left_node = left_node.next
                else:
                    tail.next = right_node
                    right_node = right_node.next
                tail = tail.next
            tail.next = left_node or right_node
            return temp.next

        if not data or not data.next:
            return data
        slow, fast = data, data.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_nodes = slow.next
        slow.next = None
        left_nodes = data
        left_half = merge_sort(left_nodes)
        right_half = merge_sort(right_nodes)
        return merge(left_half, right_half)

    else:
        raise TypeError("Invalid datatype!!!")


def quick_sort(
    data: list | EventNode, attribute: str | None = None
) -> list | EventNode:
    """
    Sorts data using the quick sorting algorithm. Chooses the first item in the list as a pivot.

    Parameters
    ----------
    data: list | EventNode
        The data to be sorted
    attribute: str | None
        The name of the attribute to parse in each item of the iterable to be used for sorting
        If None, matches each item

    Returns
    -------
    Sorted list or linked list node
    """
    if isinstance(data, list):
        # Base case
        if len(data) <= 1:
            return data

        # Choose a pivot
        pivot = data[0]

        # Split data into three sections (left, pivot, right)
        left_data = [
            d
            for d in data
            if parse_object(d, attribute) < parse_object(pivot, attribute)
        ]
        middle_data = [
            d
            for d in data
            if parse_object(d, attribute) == parse_object(pivot, attribute)
        ]
        right_data = [
            d
            for d in data
            if parse_object(d, attribute) > parse_object(pivot, attribute)
        ]

        return quick_sort(left_data) + middle_data + quick_sort(right_data)

    elif isinstance(data, EventNode):
        if not data or not data.next:
            return data
        """
        Taking first element as pivot.
        """
        pivot = data
        """
        Most probably below defined empty nodes mosts probably will 
        crash since we need valid inputs because of constructor. 
        We might have to pass dummy values.
        """
        less_head = EventNode(None)
        less_tail = less_head
        equal_head = EventNode(None)
        equal_tail = equal_head
        greater_head = EventNode(None)
        greater_tail = greater_head
        """
        Traverse through list and segregate nodes based on value of pivot
        """
        current = data
        while current:
            if parse_object(current, attribute) < parse_object(pivot, attribute):
                less_tail.next = current
                less_tail = less_tail.next
            elif parse_object(current, attribute) > parse_object(pivot, attribute):
                greater_tail.next = current
                greater_tail = greater_tail.next
            else:
                equal_tail.next = current
                equal_tail = equal_tail.next
        """
        Terminating the three new nodes by cutting of their tail 
        (setting tail = None)
        """
        less_tail.next, equal_tail.next, greater_tail.next = None, None, None
        """
        Recursively sort the nodes further.
        Equal_to is considered as already sorted
        """
        sorted_less = quick_sort(less_head.next)
        sorted_greater = quick_sort(greater_head.next)
        """
        Merging sorted nodes together
        """
        if not sorted_less:
            equal_tail.next = sorted_greater
            return equal_head.next
        else:
            tail_of_less = sorted_less
            while tail_of_less:
                tail_of_less = tail_of_less.next
            tail_of_less.next = equal_head.next
            equal_tail.next = sorted_greater
            return sorted_less

    else:
        raise TypeError("Invalid datatype!!!")


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
