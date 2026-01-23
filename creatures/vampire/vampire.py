"""
Vampire - A creature that introduces mutable state.

This module teaches fundamental concepts about object state:
- Internal state initialization (thirsty is set inside __init__, not passed in)
- State mutation through methods (drink changes thirsty)
- The distinction between constructor arguments and internal state
- Default parameter values (pet="bat")

Key Design Decision:
    The `thirsty` attribute is NOT a constructor parameter. This teaches
    that some state is internal to the object and should not be controllable
    by the caller. A vampire is ALWAYS born thirsty - this is an invariant
    of the class design.
"""


class Vampire:
    """
    A vampire with a name, pet, and thirst state.

    Attributes:
        name: The vampire's name (required).
        pet: The vampire's pet (optional, defaults to "bat").
        thirsty: Whether the vampire is thirsty (always starts True).

    Example:
        >>> vampire = Vampire("Vlad")
        >>> vampire.name
        'Vlad'
        >>> vampire.pet
        'bat'
        >>> vampire.thirsty
        True
        >>> vampire.drink()
        >>> vampire.thirsty
        False
    """

    def __init__(self, name: str, pet: str = "bat") -> None:
        """
        Initialize a new Vampire.

        Args:
            name: The vampire's name.
            pet: The vampire's pet. Defaults to "bat".

        Note:
            The thirsty attribute is initialized internally to True.
            It is intentionally NOT a parameter - vampires are always
            born thirsty.
        """
        self.name = name
        self.pet = pet
        self.thirsty = True  # Internal state, not a parameter

    def drink(self) -> None:
        """
        The vampire drinks, satisfying their thirst.

        This method mutates the vampire's state, changing thirsty to False.
        """
        self.thirsty = False
