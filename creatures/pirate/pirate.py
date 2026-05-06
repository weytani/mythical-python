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
from dataclasses import dataclass


@dataclass
class Pirate:
    name: str
    job: str = "Scallywag"
    cursed: bool = False
    booty: int = 0
    heinous_acts: int = 0

    def commit_heinous_act(self):
        """Commit a heinous act."""
        self.heinous_acts += 1
        if self.heinous_acts >= 3:
            self.cursed = True


