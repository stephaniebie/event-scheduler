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
            if new_event.collides_with(current.data):
                print("An event already exist at this time! Please enter different time.")
                return None
            current = current.next

        new_event.id = self.id
        self.id += 1

        new_node = EventNode(new_event)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        print(f"Successfully created new event: '{new_event.title} with ID: '{new_event.id}'")
        return new_event

    def delete(self, event_id: int) -> bool:
        current = self.head
        previous = None

        if current is None:
            return False

        while current and current.data.id != event_id:
            previous = current
            current = current.next
        
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return True

    def search_by_id(self):
        # TODO
        raise NotImplementedError

    def list_all(self) -> list:
        # TODO
        raise NotImplementedError

