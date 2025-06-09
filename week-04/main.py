class ReservableItem:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} ({self.capacity})"


class Event(ReservableItem):
    def __init__(self, name, capacity, date):
        super().__init__(name, capacity)
        self.date = date
        self.tickets = []

    def __len__(self):
        return len(self.tickets)

    def add_ticket(self, ticket):
        if len(self.tickets) < self.capacity:
            self.tickets.append(ticket)
            return True
        return False


class Ticket:
    def __init__(self, owner, event):
        self.owner = owner
        self.event = event

    def __eq__(self, other):
        return self.owner == other.owner and self.event == other.event


class ReservationSystem:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def find_event(self, name):
        return next((e for e in self.events if e.name == name), None)

def main():
    event = Event("Concert", 100, "2023-10-01")
    ticket1 = Ticket("Alice", event)
    ticket2 = Ticket("Bob", event)

    event.add_ticket(ticket1)
    event.add_ticket(ticket2)

    print(event)  # Output: Concert (100)
    print(len(event))  # Output: 2

    system = ReservationSystem()
    system.add_event(event)

    found_event = system.find_event("Concert")
    if found_event:
        print(f"Found event: {found_event}")


if __name__ == "__main__":
    main()
