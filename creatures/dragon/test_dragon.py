"""
Test suite for the Dragon class.

This exercise introduces counters and derived state (computed properties):
- State accumulation using an integer counter
- Conditional logic based on thresholds
- The @property decorator for computed/derived state
- Encapsulation of internal implementation details

Learning Objectives:
- Understand state accumulation (incrementing counters)
- Learn that state can be derived/computed rather than stored directly
- Master the @property decorator for Pythonic computed attributes
- Understand encapsulation: expose what matters (hungry), hide implementation (_meals_eaten)
"""

import pytest

from creatures.dragon.dragon import Dragon


class TestDragonCreation:
    """Tests for Dragon instantiation and attributes."""

    def test_dragon_has_a_name(self):
        """A Dragon must have a name."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        assert dragon.name == "Smaug"

    def test_dragon_has_a_color(self):
        """A Dragon must have a color."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        assert dragon.color == "gold"

    def test_dragon_has_a_rider(self):
        """A Dragon must have a rider."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        assert dragon.rider == "Bilbo"


class TestDragonHunger:
    """Tests for Dragon hunger state - the core lesson of this exercise."""

    def test_dragon_is_initially_hungry(self):
        """A newly created Dragon is always hungry."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        assert dragon.hungry is True

    def test_dragon_is_hungry_after_one_meal(self):
        """A Dragon is still hungry after eating once."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        dragon.eat()
        assert dragon.hungry is True

    def test_dragon_is_hungry_after_two_meals(self):
        """A Dragon is still hungry after eating twice."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        dragon.eat()
        dragon.eat()
        assert dragon.hungry is True

    def test_dragon_is_not_hungry_after_three_meals(self):
        """A Dragon is no longer hungry after eating three times."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        dragon.eat()
        dragon.eat()
        dragon.eat()
        assert dragon.hungry is False

    def test_dragon_hunger_progression(self):
        """Complete hunger progression test: hungry until 3 meals."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        assert dragon.hungry is True

        dragon.eat()
        assert dragon.hungry is True

        dragon.eat()
        assert dragon.hungry is True

        dragon.eat()
        assert dragon.hungry is False  # Threshold reached

    def test_dragon_stays_full_after_more_meals(self):
        """A Dragon remains not hungry even after eating more than 3 times."""
        dragon = Dragon("Smaug", "gold", "Bilbo")
        for _ in range(5):
            dragon.eat()
        assert dragon.hungry is False


class TestDragonMultipleInstances:
    """Tests ensuring each Dragon has independent state."""

    def test_eating_does_not_affect_other_dragons(self):
        """Each Dragon instance maintains its own meal count."""
        smaug = Dragon("Smaug", "gold", "Bilbo")
        drogon = Dragon("Drogon", "black", "Daenerys")

        smaug.eat()
        smaug.eat()
        smaug.eat()

        assert smaug.hungry is False
        assert drogon.hungry is True  # Drogon hasn't eaten
