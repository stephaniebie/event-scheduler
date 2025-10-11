# PART A: Event Storage Structures
# An implementation of two independent ways of storing events
from scheduler.event import Event
from scheduler.search import search_data, SearchAlgorithm
from scheduler.sort import sort_data, SortingAlgorithm


class EventList:
    """
    An array-based list of events.
    """

    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.events = [None] * self.capacity
        self.id = 1  # This will sequentially generate unique ID
        self.size = 0 # variable to keep track of number of events in array
    """
    I defined a static array with default size = 10.

    I also defined a private function called _dynamic_resize() which will
    dynamically increase size of static array when array becomes full.
    """

    def _dynamic_resize(self, new_capacity: int):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.events[i]
        self.events = new_data
        self.capacity = new_capacity

    def insert(self, new_event: Event):
        for i in range(self.size):
            existing_event = self.events[i]
            if new_event.collides_with(
                existing_event
            ):  # Calls collide_with function to check if new event collides with existing events
                print(
                    "An event already exist at this time! Please enter different time."
                )
                return None
        """
        Added new condition which checks if array is full. If it is full, we
        will call our private resizing function and increase the size by twice
        every time our array hits maximum capacity.

        Multiplying size by 2 is more efficient that adding one slot at a time 
        because it will avoid copying every single element to new array. 
        If we increase size by 1 every single time, we will unnecessarily add 
        time complexity of O(n) - which is time taken to copy all elements to 
        new array every single time.
        """
        if self.size == self.capacity:
            self._dynamic_resize(self.capacity + 10) #Calling resize fn by passing new capacity value
        new_event.id = self.id
        self.events[self.size] = new_event
        self.id += 1
        self.size +=1
        print(
            f"Successfully created new event: '{new_event.title}' with ID: '{new_event.id}'"
        )
        return new_event

    # Below function deletes an event based on event ID and returns boolean
    def delete(self, event_id: int) -> bool:
        to_remove = -1
        """
        Since we are using static array, we need new logic to delete
        for event in self.events:
            if event.id == event_id:
                to_remove = event
                break

        if to_remove:
            self.events.remove(to_remove) #Not sure if we can use this fn
            return True

        return False
        """
        for i in range(self.size):
            if self.events[i] == event_id:
                to_remove = i
                break
        if to_remove == -1:
            return False
        for i in range(to_remove, self.size - 1):
            self.events[i] = self.events[i + 1]

        self.events[self.size - 1] = None
        self.size -=1
        return True    

    def search_by_id(self, id: int, algorithm: SearchAlgorithm):
        """
        Added new line to avoid None values being passed to the function
        """
        booked_events = self.events[:self.size]
        return search_data(booked_events, id, algorithm)

    def list_all(self, algorithm: SortingAlgorithm):
        """
        Added new line to avoid None values being passed to the function
        """
        booked_events = self.events[:self.size]
        sorted_list = sort_data(booked_events, algorithm)
        for event in sorted_list:
            print(event)
