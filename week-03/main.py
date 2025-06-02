#!/usr/bin/env python3
"""Simple CLI reservation system illustrating object‑oriented concepts.

Features implemented
--------------------
* Base class ``ReservableItem`` and subclass ``Event`` (inheritance).
* Class, static and magic methods (``__str__``, ``__repr__``, ``__eq__``, ``__len__``).
* A ``ReservationSystem`` container supporting iteration and length (polymorphism).
* Command‑line interface built with ``argparse`` (no external deps).

Run ``python reservation_cli.py --help`` for usage.
"""
from __future__ import annotations

import argparse
import sys
import uuid
from datetime import datetime
from typing import Dict, List, Tuple

# ──────────────────────────────────────────────────────────────────────────────
# Core domain model
# ──────────────────────────────────────────────────────────────────────────────

class ReservableItem:
    """A generic item that can be reserved (base class)."""

    def __init__(self, name: str, capacity: int):
        self.id: str = self._generate_id()
        self.name: str = name
        self.capacity: int = self._validate_capacity(capacity)
        self._reserved: int = 0  # tickets already booked

    # ── Static / class helpers ────────────────────────────────────────────
    @staticmethod
    def _validate_capacity(capacity: int) -> int:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        return capacity

    @classmethod
    def _generate_id(cls) -> str:
        """Return a short UUID for easier typing in the CLI."""
        return uuid.uuid4().hex[:8]

    # ── Business logic ────────────────────────────────────────────────────
    def reserve(self, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self._reserved + quantity > self.capacity:
            raise ValueError("Not enough capacity available")
        self._reserved += quantity

    @property
    def available(self) -> int:
        return self.capacity - self._reserved

    # ── Magic methods ─────────────────────────────────────────────────────
    def __len__(self) -> int:  # so len(event) returns its capacity
        return self.capacity

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ReservableItem) and self.id == other.id

    def __str__(self) -> str:
        return f"{self.name} [id={self.id}] {self._reserved}/{self.capacity} reserved"

    def __repr__(self) -> str:  # unambiguous developer‑oriented form
        cls = self.__class__.__name__
        return f"{cls}(id='{self.id}', name='{self.name}', capacity={self.capacity})"


class Event(ReservableItem):
    """A dated event that can be booked (inherits from ReservableItem)."""

    def __init__(self, name: str, date: datetime, capacity: int):
        super().__init__(name, capacity)
        self.date: datetime = date

    # ── Alternative constructor ───────────────────────────────────────────
    @classmethod
    def from_string(cls, spec: str) -> "Event":
        """Build *Event* from ``"name;YYYY‑MM‑DD;capacity"`` string."""
        try:
            name, date_s, cap_s = spec.split(";")
            date = datetime.strptime(date_s.strip(), "%Y-%m-%d")
            capacity = int(cap_s)
        except ValueError as exc:
            raise ValueError(
                "Expected format 'Name;YYYY‑MM‑DD;capacity'"
            ) from exc
        return cls(name.strip(), date, capacity)

    # ── Magic overrides ───────────────────────────────────────────────────
    def __str__(self) -> str:
        date_fmt = self.date.strftime("%Y‑%m‑%d")
        return f"{self.name} @ {date_fmt} (ID: {self.id}) — {self.available}/{self.capacity} seats left"

    def __repr__(self) -> str:
        base = super().__repr__()
        return base[:-1] + f", date='{self.date.isoformat()}')"  # inject date


class Ticket:
    """Represents a ticket bound to a specific *Event*."""

    __slots__ = ("event", "quantity")

    def __init__(self, event: Event, quantity: int = 1):
        self.event: Event = event
        self.quantity: int = quantity

    # no business logic here; reserving handled by Event.reserve
    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Ticket)
            and self.event == other.event
            and self.quantity == other.quantity
        )

    def __str__(self) -> str:
        return f"Ticket for '{self.event.name}' x{self.quantity}"

    def __repr__(self) -> str:
        return f"Ticket(event={repr(self.event)}, quantity={self.quantity})"


# ──────────────────────────────────────────────────────────────────────────────
# Aggregate / service layer
# ──────────────────────────────────────────────────────────────────────────────

class ReservationSystem:
    """Container for events and their reservations."""

    def __init__(self):
        self._events: Dict[str, Event] = {}
        self._reservations: List[Tuple[str, Ticket]] = []  # (event_id, ticket)

    # Collection‑like behaviour
    def __len__(self) -> int:
        return len(self._events)

    def __iter__(self):
        return iter(self._events.values())

    # ── Commands ────────────────────────────────────────────────────────
    def add_event(self, event: Event) -> None:
        if event.id in self._events:
            raise ValueError(f"Event with id {event.id} already exists")
        self._events[event.id] = event

    def list_events(self) -> List[Event]:
        return list(self._events.values())

    def reserve(self, event_id: str, qty: int) -> Ticket:
        event = self._events.get(event_id)
        if not event:
            raise KeyError(f"Event ID '{event_id}' not found")
        event.reserve(qty)
        ticket = Ticket(event, qty)
        self._reservations.append((event_id, ticket))
        return ticket

    def list_reservations(self) -> List[Ticket]:
        return [t for _eid, t in self._reservations]


# ──────────────────────────────────────────────────────────────────────────────
# CLI entry point
# ──────────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Minimal event reservation CLI")
    sub = p.add_subparsers(dest="command", required=True)

    # add_event
    pe = sub.add_parser("add_event", help="Create a new event")
    pe.add_argument("name", help="Event name")
    pe.add_argument("date", help="Event date (YYYY‑MM‑DD)")
    pe.add_argument("capacity", type=int, help="Total number of seats")

    # list_events
    sub.add_parser("list_events", help="Show all events")

    # reserve
    pr = sub.add_parser("reserve", help="Reserve tickets for an event")
    pr.add_argument("event_id", help="ID of the event")
    pr.add_argument("quantity", type=int, help="Number of seats to book")

    # list_reservations
    sub.add_parser("list_reservations", help="Show all reservations")

    return p


def main(argv: List[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    # For demo purposes we keep everything in memory; in real life you'd persist.
    system = ReservationSystem()

    # Dispatch commands
    if args.command == "add_event":
        try:
            date = datetime.strptime(args.date, "%Y-%m-%d")
            event = Event(args.name, date, args.capacity)
            system.add_event(event)
            print(f"✅ Added event: {event}")
        except Exception as exc:
            print(f"❌ Error: {exc}")

    elif args.command == "list_events":
        events = system.list_events()
        if not events:
            print("(no events yet)")
        else:
            for ev in events:
                print(ev)

    elif args.command == "reserve":
        try:
            ticket = system.reserve(args.event_id, args.quantity)
            print(f"✅ Reservation successful! {ticket}")
        except Exception as exc:
            print(f"❌ Error: {exc}")

    elif args.command == "list_reservations":
        res = system.list_reservations()
        if not res:
            print("(no reservations yet)")
        else:
            for t in res:
                print(t)


if __name__ == "__main__":  # pragma: no cover
    main()
