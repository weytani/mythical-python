# ABOUTME: Direwolf and Stark creature implementations for the TDD curriculum.
# ABOUTME: Teaches bidirectional state mutation, guards, and @property for derived state.
"""
Direwolf - Capstone exercise for bidirectional state and location-matching guards.

This module teaches the most complex multi-class interaction in the curriculum:
- Bidirectional state mutation (protect sets stark.safe, leave unsets it)
- Location-matching guard clause (protect only works at same location)
- Capacity constraint (max 2 Starks per Direwolf)
- @property decorator for derived boolean state (hunts_white_walkers)
- Silent no-op guards (no exceptions raised on guard failure)

Key Design Decisions:
    Both classes live in the same file, matching the Medusa+Person pattern.
    The protect() method has two silent guards: location match and capacity
    check. Neither raises an exception — they simply do nothing. This is
    intentional for the learning exercise, matching the JavaScript original.
    The hunts_white_walkers attribute is a @property that derives its value
    from whether starks_to_protect is empty.
"""


class Stark:
    pass


class Direwolf:
    pass
