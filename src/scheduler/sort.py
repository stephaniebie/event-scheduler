# PART B: Sorting Events
# Implementation of three sorting algorithms
from src.scheduler.event import EventNode
from src.scheduler.event_array_list import EventList, LinkedEventList


def insertion_sort_list(events: list) -> list:
    """ Copying list to another list so we don't alter original list which is already sorted by event id. """

    temp_list = list(events)
    
    for i in range(1, len(temp_list)):
        key_event = temp_list[i]
        j = i - 1

        while j>=0 and key_event < temp_list[j]:
            temp_list[j + 1] = temp_list[j]
            j -= 1
        temp_list[j + 1] = key_event
    return temp_list

def merge_sort_list(events: list) -> list:
    if len(events) <= 1:
        return events

    mid = len(events)//2
    left_half = merge_sort_list(events[:mid])
    right_half = merge_sort_list(events[mid:])

    temp_list = []
    i,j = 0,0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            temp_list.append(left_half[i])
            i += 1
        else:
            temp_list.append(right_half[j])
            j += 1
    
    """
    Need to discuss if we can use below extend() function to append remaining items in list
    """

    temp_list.extend(left_half[i:])
    temp_list.extend(right_half[j:])
    return temp_list

def quick_sort_list(events: list) -> list:
    if len(events) <= 1:
        return events
    
    """ Taking middle element as pivot """
    pivot = events[len(events)//2] 

    less_than = []
    equal_to = []
    greater_than = []

    for event in events:
        if event < pivot:
            less_than.append(event)
        elif event > pivot:
            greater_than.append(event)
        else:
            equal_to.append(event)

    return quick_sort_list(less_than) + equal_to + quick_sort_list(greater_than)


def insertion_sort_linked_list(event_node):
    if not event_node or not event_node.next:
        return event_node

    temp_node = None
    current = event_node

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
            

def merge_sort_linked_list(event_node):

    """ Function for merging two halves """
    def merge(left_node, right_node):
        """ 
        Need a dummy node but None will probably fail because our EventNode constructor needs valid input. 
        Need to explore other options
        """
        temp = EventNode(None)  #Will probably fail on execution
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
    
    if not event_node or not event_node.next:
        return event_node
    
    slow, fast = event_node, event_node.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    right_nodes = slow.next
    slow.next = None
    left_nodes = event_node

    left_half = merge_sort_linked_list(left_nodes)
    right_half = merge_sort_linked_list(right_nodes)

    return merge(left_half, right_half)