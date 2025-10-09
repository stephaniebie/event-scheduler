import datetime

class Event:
    """
    A unique campus event.
    """

    def __init__(
        self,
        id: int,
        title: str,
        date: str,
        time: str,
        location: str,
    ):        
        # Checks whether date and time are valid inputs and returns None if its invalid.
        try:        
            self.start_time = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            self.end_time = self.start_time + datetime.timedelta(hours = 1)
        except ValueError:
            raise ValueError(f"Invalid date '{date}' or time '{time}'")

        self.id = id
        self.title = title
        self.location = location
        self.date = date
        self.time = time

    # Function to check whether new event collides with other existing events.
    def collides_with(self, other): 
        return self.start_time < other.end_time and other.start_time < self.end_time

    def __eq__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time == other.start_time
    
    def __ne__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time != other.start_time
    
    def __gt__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time > other.start_time
    
    def __lt__(self, other):
        if not isinstance(other, Event):
            return NotImplemented
        return self.start_time < other.start_time
    

class EventNode(Event):
    """
    A unique campus event node for storage within a linked list.
    """

    def __init__(
        self,
        id: int,
        title: str,
        date: str,
        time: str,
        location: str,
        next: None | 'EventNode' = None,
    ):
        super().__init__(
            id=id,
            title=title,
            date=date,
            time=time,
            location=location,
        )
        self.next = next
