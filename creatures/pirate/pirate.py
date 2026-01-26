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
    pass
