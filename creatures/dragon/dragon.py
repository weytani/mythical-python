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
from dataclasses import dataclass


@dataclass
class Dragon:
    name: str
    color: str
    rider: str
    hungry: bool = True
    _meals_eaten: int = 0

    def __init__(self, name: str, color: str, rider: str):
        self.name = name
        self.color = color
        self.rider = rider
        self._meals_eaten = 0

    def eat(self):
        self._meals_eaten += 1
    
    @property
    def hungry(self) -> bool:
        return self._meals_eaten < 3
        