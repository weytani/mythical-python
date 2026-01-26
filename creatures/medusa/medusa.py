"""
Medusa - Introduces object interaction and collection management.

This module represents a major complexity jump, teaching:
- Two classes that interact (Medusa and Person)
- One-to-many relationships (Medusa has many statues)
- State mutation across objects (Medusa modifies Person.stoned)
- FIFO queue logic (max 3 statues, oldest released)
- Object references (statues list holds references to Person objects)

Key Design Decisions:
    The `statues` list holds references to Person objects, not copies.
    This teaches Python's reference semantics - modifying a Person
    affects the same object whether accessed directly or through
    the statues list.

    The FIFO queue pattern (pop(0) when over limit) teaches list
    manipulation and introduces queue data structure concepts.
"""


class Person:
    pass


class Medusa:
    pass
