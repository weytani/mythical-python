"""
Unicorn - The first mythical creature in the TDD curriculum.

This module introduces fundamental Python OOP concepts:
- Class definition with __init__ constructor
- Instance attributes (self.name, self.color)
- Default parameter values for optional arguments
- Type hints for better code documentation and IDE support
- Methods that return boolean values
- String formatting with f-strings
"""


class Unicorn:
    """
    A magical unicorn with a name and color.

    Attributes:
        name: The unicorn's name (required).
        color: The unicorn's color (optional, defaults to "silver").

    Example:
        >>> unicorn = Unicorn("Sparkles")
        >>> unicorn.name
        'Sparkles'
        >>> unicorn.color
        'silver'
        >>> unicorn.is_silver()
        True
        >>> unicorn.say("Hello!")
        '**;* Hello! *;**'
    """

    def __init__(self, name: str, color: str = "silver") -> None:
        """
        Initialize a new Unicorn.

        Args:
            name: The unicorn's name.
            color: The unicorn's color. Defaults to "silver".
        """
        self.name = name
        self.color = color

    def is_silver(self) -> bool:
        """
        Check if the unicorn is silver colored.

        Returns:
            True if the unicorn's color is "silver", False otherwise.
        """
        return self.color == "silver"

    def say(self, phrase: str) -> str:
        """
        Make the unicorn say a phrase with magical sparkles.

        Args:
            phrase: The phrase for the unicorn to say.

        Returns:
            The phrase wrapped in sparkle decorations.
        """
        return f"**;* {phrase} *;**"
