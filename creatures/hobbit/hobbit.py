"""
Hobbit - A creature that introduces lifecycle modeling.

This module teaches important concepts about lifecycle and boundaries:
- Age-based state transitions using integer comparisons
- Boundary conditions (age > 32, not age >= 32)
- Computed properties for lifecycle states
- Name-based conditional logic (Frodo has the ring)

Key Design Decision:
    The `is_adult` and `is_old` attributes are @property decorators,
    computing state based on the current age. This ensures lifecycle
    states are always accurate and never out of sync with age.

Boundary Values:
    - Adult: age > 32 (33 and above)
    - Old: age > 100 (101 and above)
"""


class Hobbit:
    """
    A hobbit with a name, disposition, and age-based lifecycle.

    Hobbits age through birthdays and progress through life stages:
    - Child: age <= 32
    - Adult: age > 32
    - Old: age > 100

    Attributes:
        name: The hobbit's name (required).
        disposition: The hobbit's disposition (optional, defaults to "homebody").
        age: The hobbit's age (starts at 0).
        is_adult: Whether the hobbit is an adult (computed property).
        is_old: Whether the hobbit is old (computed property).

    Example:
        >>> hobbit = Hobbit("Frodo", disposition="adventurous")
        >>> hobbit.age
        0
        >>> hobbit.is_adult
        False
        >>> for _ in range(33):
        ...     hobbit.celebrate_birthday()
        >>> hobbit.is_adult
        True
        >>> hobbit.has_ring()
        True
    """

    def __init__(self, name: str, disposition: str = "homebody") -> None:
        """
        Initialize a new Hobbit.

        Args:
            name: The hobbit's name.
            disposition: The hobbit's disposition. Defaults to "homebody".
        """
        self.name = name
        self.disposition = disposition
        self.age = 0  # Internal state, always starts at 0

    def celebrate_birthday(self) -> None:
        """
        The hobbit celebrates a birthday, incrementing their age by 1.
        """
        self.age += 1

    @property
    def is_adult(self) -> bool:
        """
        Whether the hobbit is an adult.

        A hobbit becomes an adult when their age exceeds 32.

        Returns:
            True if age > 32, False otherwise.
        """
        return self.age > 32

    @property
    def is_old(self) -> bool:
        """
        Whether the hobbit is old.

        A hobbit becomes old when their age exceeds 100.

        Returns:
            True if age > 100, False otherwise.
        """
        return self.age > 100

    def has_ring(self) -> bool:
        """
        Check if this hobbit has the One Ring.

        Only Frodo has the ring (case-sensitive).

        Returns:
            True if the hobbit's name is "Frodo", False otherwise.
        """
        return self.name == "Frodo"
