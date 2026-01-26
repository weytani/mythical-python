"""
Vampire - A creature that introduces mutable state.

This module teaches fundamental concepts about object state:
- Internal state initialization (thirsty is set inside __init__, not passed in)
- State mutation through methods (drink changes thirsty)
- The distinction between constructor arguments and internal state
- Default parameter values (pet="bat")

Key Design Decision:
    The `thirsty` attribute is NOT a constructor parameter. This teaches
    that some state is internal to the object and should not be controllable
    by the caller. A vampire is ALWAYS born thirsty - this is an invariant
    of the class design.
"""


class Vampire:
    pass
