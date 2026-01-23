"""
Wizard - A creature that emphasizes string manipulation and boolean arguments.

This module teaches important concepts about strings and booleans:
- Boolean default parameters (bearded=True)
- String transformation using f-strings
- Resource management (rested state depleted by casting)

Key Design Decisions:
    The `bearded` parameter demonstrates boolean defaults in constructors.
    Unlike string defaults (like "silver" for Unicorn), boolean defaults
    require students to understand True/False as first-class values.

    The `incantation()` method introduces functional string transformation,
    preparing students for more complex string manipulation patterns.
"""


class Wizard:
    """
    A wizard with a name, beard status, and magical abilities.

    Wizards can cast spells (which tires them) and create incantations
    by transforming phrases with magical prefixes.

    Attributes:
        name: The wizard's name (required).
        bearded: Whether the wizard has a beard (optional, defaults to True).
        rested: Whether the wizard is rested (starts True, False after casting).

    Example:
        >>> wizard = Wizard("Gandalf")
        >>> wizard.bearded
        True
        >>> wizard.incantation("fly")
        'sudo fly'
        >>> wizard.rested
        True
        >>> wizard.cast()
        'Gandalf casts a spell!'
        >>> wizard.rested
        False
    """

    def __init__(self, name: str, bearded: bool = True) -> None:
        """
        Initialize a new Wizard.

        Args:
            name: The wizard's name.
            bearded: Whether the wizard has a beard. Defaults to True.
        """
        self.name = name
        self.bearded = bearded
        self.rested = True  # Internal state, wizards start rested

    def incantation(self, phrase: str) -> str:
        """
        Transform a phrase into a magical incantation.

        Prepends "sudo" to give the phrase magical authority.
        This demonstrates string manipulation with f-strings.

        Args:
            phrase: The phrase to transform.

        Returns:
            The phrase with "sudo " prepended.
        """
        return f"sudo {phrase}"

    def cast(self) -> str:
        """
        The wizard casts a spell, becoming tired.

        Casting depletes the wizard's energy, setting rested to False.

        Returns:
            A message describing the spell being cast.
        """
        self.rested = False
        return f"{self.name} casts a spell!"

    def rest(self) -> None:
        """
        The wizard rests, recovering their energy.

        Sets rested back to True, allowing the wizard to cast again
        at full power.
        """
        self.rested = True
