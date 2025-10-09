# PART A: Event Storage Structures
# An implementation of two independent ways of storing events
from scheduler.event import Event
from scheduler.search import search_data, SearchAlgorithm
from scheduler.sort import sort_data, SortingAlgorithm


class EventList:
    """
    An array-based list of events.
    """

    def __init__(self):
        self.events = []
        self.id = 1  # This will sequentially generate unique ID

    def insert(self, new_event: Event):
        for existing_event in self.events:
            if new_event.collides_with(
                existing_event
            ):  # Calls collide_with function to check if new event collides with existing events
                print(
                    "An event already exist at this time! Please enter different time."
                )
                return None

        new_event.id = self.id
        self.events.append(new_event)
        self.id += 1
        print(
            f"Successfully created new event: '{new_event.title}' with ID: '{new_event.id}'"
        )
        return new_event

    # Below function deletes an event based on event ID and returns boolean
    def delete(self, event_id: int) -> bool:
        to_remove = None

        for event in self.events:
            if event.id == event_id:
                to_remove = event
                break

        if to_remove:
            self.events.remove(to_remove)
            return True

        return False

    def search_by_id(self, id: int, algorithm: SearchAlgorithm):
        return search_data(self.events, id, algorithm)

    def list_all(self, algorithm: SortingAlgorithm):
        sorted_list = sort_data(self.events, algorithm)
        for event in sorted_list:
            print(event)
