# PART B: Sorting Events
# Implementation of three sorting algorithms
from enum import Enum
from src.scheduler.event import EventNode


def insertion_sort(data: list | EventNode) -> list | EventNode:
    """
    Copying list to another list so we don't alter original
    list which is already sorted by event id.
    """
    if type(data) is list:
        temp_list = list(data)
        for i in range(1, len(temp_list)):
            key_event = temp_list[i]
            j = i - 1

            while j >= 0 and key_event < temp_list[j]:
                temp_list[j + 1] = temp_list[j]
                j -= 1
            temp_list[j + 1] = key_event
        return temp_list

    elif type(data) is EventNode:
        if not data or not data.next:
            return data

        temp_node = None
        current = data
        while current:
            next_node = current.next
            if not temp_node or current <= temp_node:
                current.next = temp_node
                temp_node = current
            else:
                temp_current = temp_node
                while temp_current.next and temp_current.next < current:
                    temp_current = temp_current.next
                current.next = temp_current.next
                temp_current.next = current
            current = next_node
        return temp_node

    else:
        raise TypeError("Invalid datatype!!!")


def merge_sort(data: list | EventNode) -> list | EventNode:
    if type(data) is list:
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left_half = merge_sort(data[:mid])
        right_half = merge_sort(data[mid:])

        temp_list = []
        i, j = 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                temp_list.append(left_half[i])
                i += 1
            else:
                temp_list.append(right_half[j])
                j += 1
        """
        Need to discuss if we can use below extend() function 
        to append remaining items in list
        """
        temp_list.extend(left_half[i:])
        temp_list.extend(right_half[j:])
        return temp_list

    elif type(data) is EventNode:
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
                if left_node <= right_node:
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


def quick_sort(data: list | EventNode) -> list | EventNode:
    if type(data) is list:
        if len(data) <= 1:
            return data
        """ 
        Taking first element as pivot.
        """
        pivot = data[0]
        less_than = []
        equal_to = []
        greater_than = []
        for event in data:
            if event < pivot:
                less_than.append(event)
            elif event > pivot:
                greater_than.append(event)
            else:
                equal_to.append(event)
        return quick_sort(less_than) + equal_to + quick_sort(greater_than)

    elif type(data) is EventNode:
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
            if current < pivot:
                less_tail.next = current
                less_tail = less_tail.next
            elif current > pivot:
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
    INSERTION = insertion_sort
    MERGE = merge_sort
    QUICK = quick_sort


def sort_data(data, algorithm: SortingAlgorithm):
    return algorithm.value(data)
