# PART C: Searching & Conflict Detection
# Implements linear and binary search as well as an algorithm for checking if two or more events overlap in time

from enum import Enum
from src.scheduler.event import EventNode


def linear_search(data: list | EventNode, target_id: int):
    if type(data) is list:
        for event in data:
            if event.id == target_id:
                return event
        return None

    elif type(data) is EventNode or data is None:
        current = data
        while current:
            if current.id == target_id:
                return current
            current = current.next
        return None

    else:
        raise TypeError("Invalid datatype!!!")


def binary_search(data: list | EventNode, target_id: int):
    if type(data) is list:
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid].id == target_id:
                return data[mid]
            elif data[mid].id < target_id:
                low = mid + 1
            else:
                high = mid - 1
        return None

    elif type(data) is EventNode or data is None:
        length = 0
        current = data
        """
        Traversing through linked list to get length
        """
        while current:
            length += 1
            current = current.next
        """
        If linked list is empty, returns None
        """
        if length == 0:
            return None
        """
        Performing Binary Search
        """
        low, high = 0, length - 1
        while low <= high:
            mid = (low + high) // 2
            mid_node = data
            """
            Since we can't directly access index in linked list,
            we are traversing from head till middle node
            """
            for _ in range(mid):
                mid_node = mid_node.next
            if mid_node.id == target_id:
                return mid_node
            elif mid_node.id < target_id:
                low = mid + 1
            else:
                high = mid - 1

    else:
        raise TypeError("Invalid datatype!!!")


class SearchAlgorithm(Enum):
    LINEAR = linear_search
    BINARY = binary_search


def search_data(data, target_id: int, algorithm: SearchAlgorithm):
    if algorithm == SearchAlgorithm.LINEAR:
        return linear_search(data, target_id)

    elif algorithm == SearchAlgorithm.BINARY:
        return binary_search(data, target_id)

    """ 
    We can use following method

    return algorithm.value(data, target_id)

    This will automatically call the search function depending
    on the value stored in algorithm.

    """
