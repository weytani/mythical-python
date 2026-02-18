# ABOUTME: Fairy creature implementation for the TDD curriculum.
# ABOUTME: Teaches nested mutable objects, counter-triggered state reset, and mutating arguments.
"""
Fairy - Introduces nested mutable objects and counter-triggered state transitions.

This module teaches important concepts about nested data and state machines:
- Nested mutable objects (dict containing a list of dresses)
- Counter-triggered state reset (disposition resets after 3 stolen infants)
- Mutating argument objects in place (replace_infant modifies the passed dict)
- The mutable default argument pitfall (clothes must be per-instance)

Key Design Decisions:
    The `clothes` attribute is a dict containing a list. This must be
    initialized as a new dict per instance in __init__ to avoid the
    classic Python mutable default argument bug. If you use a class-level
    default or a mutable default in the function signature, all instances
    will share the same dict.

    The `replace_infant` method mutates the passed-in dict in place,
    teaching Python's reference semantics for mutable objects.
"""


class Fairy:
    pass
