"""
Pirate - A creature that introduces state flags and accumulators.

This module teaches important concepts about triggered state and accumulation:
- State flags: cursed is set True when a threshold is reached (not computed)
- Accumulator pattern: booty acts as a "wallet" that grows over time
- Multiple independent state mechanisms in one class

Key Design Decisions:
    Unlike Dragon's `hungry` (a computed @property), the Pirate's `cursed`
    is a stored boolean that gets SET when the threshold is reached. This
    teaches students the difference between:
    - Computed state: always derived from current data (Dragon.hungry)
    - Triggered state: set once and remains (Pirate.cursed)

    The `booty` attribute demonstrates the accumulator/wallet pattern,
    where value is added incrementally and persists.
"""


class Pirate:
    """
    A pirate with a name, job, curse status, and booty.

    Pirates can commit heinous acts (leading to a curse after 3)
    and rob ships (accumulating booty).

    Attributes:
        name: The pirate's name (required).
        job: The pirate's job (optional, defaults to "Scallywag").
        cursed: Whether the pirate is cursed (False until 3 heinous acts).
        booty: The pirate's accumulated treasure (starts at 0).

    Example:
        >>> pirate = Pirate("Blackbeard", job="Captain")
        >>> pirate.cursed
        False
        >>> pirate.commit_heinous_act()
        >>> pirate.commit_heinous_act()
        >>> pirate.commit_heinous_act()
        >>> pirate.cursed
        True
        >>> pirate.rob_ship()
        >>> pirate.booty
        100
    """

    def __init__(self, name: str, job: str = "Scallywag") -> None:
        """
        Initialize a new Pirate.

        Args:
            name: The pirate's name.
            job: The pirate's job. Defaults to "Scallywag".
        """
        self.name = name
        self.job = job
        self.cursed = False
        self.booty = 0
        self._heinous_acts = 0  # Internal counter for curse threshold

    def commit_heinous_act(self) -> None:
        """
        The pirate commits a heinous act.

        After 3 heinous acts, the pirate becomes cursed.
        The curse is permanent once triggered.
        """
        self._heinous_acts += 1
        if self._heinous_acts >= 3:
            self.cursed = True

    def rob_ship(self) -> None:
        """
        The pirate robs a ship, gaining 100 booty.

        This demonstrates the accumulator/wallet pattern where
        value is added incrementally.
        """
        self.booty += 100
