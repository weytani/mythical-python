"""
Dragon - A creature that introduces counters and computed properties.

This module teaches important concepts about derived state:
- State accumulation using counters (_meals_eaten)
- Computed/derived properties using @property decorator
- Encapsulation: hiding implementation details (_meals_eaten) while
  exposing meaningful state (hungry)
- The Pythonic approach to calculated attributes

Key Design Decision:
    The `hungry` attribute is a @property, not a stored boolean.
    This means it is computed dynamically based on `_meals_eaten`.
    This approach prevents state inconsistency - hungry always reflects
    the true state based on meal count, and cannot get out of sync.
"""


class Dragon:
    """
    A dragon with a name, color, rider, and hunger state.

    The dragon starts hungry and remains hungry until it has eaten
    three meals. The hunger state is computed dynamically based on
    the number of meals eaten.

    Attributes:
        name: The dragon's name (required).
        color: The dragon's color (required).
        rider: The dragon's rider (required).
        hungry: Whether the dragon is hungry (computed property).

    Example:
        >>> dragon = Dragon("Smaug", "gold", "Bilbo")
        >>> dragon.hungry
        True
        >>> dragon.eat()
        >>> dragon.hungry
        True
        >>> dragon.eat()
        >>> dragon.eat()
        >>> dragon.hungry
        False
    """

    def __init__(self, name: str, color: str, rider: str) -> None:
        """
        Initialize a new Dragon.

        Args:
            name: The dragon's name.
            color: The dragon's color.
            rider: The dragon's rider.
        """
        self.name = name
        self.color = color
        self.rider = rider
        self._meals_eaten = 0  # Internal counter, not exposed directly

    @property
    def hungry(self) -> bool:
        """
        Whether the dragon is hungry.

        This is a computed property - the value is derived from the
        internal meal counter rather than stored directly. This ensures
        the hungry state always accurately reflects the meal count.

        Returns:
            True if the dragon has eaten fewer than 3 meals, False otherwise.
        """
        return self._meals_eaten < 3

    def eat(self) -> None:
        """
        The dragon eats a meal, incrementing the meal counter.

        After 3 meals, the dragon will no longer be hungry.
        """
        self._meals_eaten += 1
