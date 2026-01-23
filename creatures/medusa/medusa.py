"""
Medusa - Introduces object interaction and collection management.

This module represents a major complexity jump, teaching:
- Two classes that interact (Medusa and Person)
- One-to-many relationships (Medusa has many statues)
- State mutation across objects (Medusa modifies Person.stoned)
- FIFO queue logic (max 3 statues, oldest released)
- Object references (statues list holds references to Person objects)

Key Design Decisions:
    The `statues` list holds references to Person objects, not copies.
    This teaches Python's reference semantics - modifying a Person
    affects the same object whether accessed directly or through
    the statues list.

    The FIFO queue pattern (pop(0) when over limit) teaches list
    manipulation and introduces queue data structure concepts.
"""

from __future__ import annotations


class Person:
    """
    A person who can be turned to stone by Medusa.

    Attributes:
        name: The person's name (required).
        stoned: Whether the person has been turned to stone (default False).

    Example:
        >>> person = Person("Perseus")
        >>> person.stoned
        False
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a new Person.

        Args:
            name: The person's name.
        """
        self.name = name
        self.stoned = False


class Medusa:
    """
    A medusa who can turn people to stone with her stare.

    Medusa can have at most 3 statues at a time. When she turns a 4th
    person to stone, the oldest statue is released (FIFO queue).

    Attributes:
        name: The medusa's name (required).
        statues: List of Person objects currently turned to stone.

    Example:
        >>> medusa = Medusa("Cassiopeia")
        >>> victim = Person("Perseus")
        >>> medusa.stare(victim)
        >>> victim.stoned
        True
        >>> victim in medusa.statues
        True
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a new Medusa.

        Args:
            name: The medusa's name.
        """
        self.name = name
        self.statues: list[Person] = []

    def stare(self, victim: Person) -> None:
        """
        Turn a person to stone with Medusa's deadly stare.

        The victim is turned to stone and added to the statues collection.
        If this exceeds the maximum of 3 statues, the oldest statue is
        released (turned back to flesh) and removed from the collection.

        This demonstrates:
        - Object interaction (Medusa modifies Person's state)
        - Collection management (list append)
        - FIFO queue pattern (pop(0) when over limit)

        Args:
            victim: The Person to turn to stone.
        """
        victim.stoned = True
        self.statues.append(victim)

        # FIFO queue: if more than 3 statues, release the oldest
        if len(self.statues) > 3:
            released = self.statues.pop(0)
            released.stoned = False
