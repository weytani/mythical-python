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
    pass
