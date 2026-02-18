# ABOUTME: Ogre and Human creature implementations for the TDD curriculum.
# ABOUTME: Teaches chained modulo counters and cross-object state mutation.
"""
Ogre - Introduces chained counters across two cooperating classes.

This module teaches important concepts about multi-class interaction:
- Two cooperating classes (Ogre and Human) with cross-object state mutation
- Modulo arithmetic for periodic events (human notices every 3rd encounter)
- Chained counters (encounters trigger swings, swings trigger knockouts)
- Method delegation (encounter() conditionally calls swing_at())

Key Design Decisions:
    Both classes live in the same file, matching the Medusa+Person pattern
    established in the curriculum. The encounter() method delegates to
    swing_at() when the human notices the ogre, creating a chain:
    every 3rd encounter → swing, every 2nd swing → knockout.
"""


class Human:
    pass


class Ogre:
    pass
