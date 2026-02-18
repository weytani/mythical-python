# ABOUTME: Sphinx creature implementation for the TDD curriculum.
# ABOUTME: Teaches FIFO queues, find-and-remove patterns, and conditional return strings.
"""
Sphinx - Introduces FIFO queues and conditional return values.

This module teaches important data structure and control flow concepts:
- FIFO queue with a max capacity of 3 (oldest riddle dropped when full)
- Find-and-remove pattern (search list for matching dict, remove it)
- Conditional return strings based on game state
- String interpolation for dynamic response messages

Key Design Decisions:
    Riddles are stored as plain dicts with "riddle" and "answer" keys,
    matching the JavaScript original. The sliding window uses pop(0)
    when at capacity before appending a new riddle. Answer matching
    searches the full list (order-independent) rather than checking
    only the first element.
"""


class Sphinx:
    pass
