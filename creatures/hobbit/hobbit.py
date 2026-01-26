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
    pass
