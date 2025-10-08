from scheduler.event import Event, EventNode
from scheduler.search import search_data, SearchAlgorithm
from scheduler.sort import sort_data, SortingAlgorithm

class LinkedEventList:
    """
    A singly linked list of events.
    """

    def __init__(self):
        self.head = None
        self.id = 1

    def insert(self, new_event: EventNode):
        
        current = self.head
        while current:
            if new_event.collides_with(current):
                print("An event already exist at this time! Please enter different time.")
                return None
            current = current.next

        new_event.id = self.id
        self.id += 1

        if self.head is None:
            self.head = new_event
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_event
        print(f"Successfully created new event: '{new_event.title} with ID: '{new_event.id}'")
        return new_event

    def delete(self, event_id: int) -> bool:
        current = self.head
        previous = None

        while current and current.id != event_id:
            previous = current
            current = current.next

        if current is None:
            return False
        
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return True

    def search_by_id(self, id: int, linear_search: bool):

        """I dont think binary search can be performed on Linked list since we can't randomly access index directly
        So we will probably have to convert to list and perform binary search.
        """

        if linear_search:
            return search_data.linear_search_linked_list(self.head, id)
        else:
            temp_list = self.list_all()
            return search_data.binary_search_linked_list(temp_list, id)

    def list_all(self) -> list:
        # TODO
        raise NotImplementedError

