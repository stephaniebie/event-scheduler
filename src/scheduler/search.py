# PART C: Searching & Conflict Detection
# Implements linear and binary search as well as an algorithm for checking if two or more events overlap in time

def linear_search_list(event_list: list, target_id: int):
    for event in event_list:
        if event.id == target_id:
            return event
    return None


def binary_search_list(event_list: list, target_id: int):
    low = 0
    high = len(event_list) - 1

    while low <= high:
        mid = (low + high)//2
        if event_list[mid].id == target_id:
            return event_list[mid]
        elif event_list[mid].id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


def linear_search_linked_list(event_node, target_id: int):
    current = event_node
    while current:
        if current.id == target_id:
            return current
        current = current.next
    return None

def binary_search_linked_list(event_node, target_id: int):
    
    """
    We can't directly perform binary search on linked list. We will have to convert to list
    """

    event_list = []
    current = event_node

    while current:
        event_list.append(current)
        current = current.next
    
    low = 0
    high = len(event_list) - 1

    while low <= high:
        mid = (low + high)//2
        if event_list[mid].id == target_id:
            return event_list[mid]
        elif event_list[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None