"""
Test suite for the Vampire class.

This exercise introduces mutable state and logical state transitions:
- Internal state initialization (not passed as argument)
- State mutation through methods
- Default parameter values (reinforcing Unicorn lessons)

Learning Objectives:
- Understand that objects are state machines, not static data containers
- Learn to initialize internal state within __init__ (not as parameter)
- Practice state mutation through method calls
- Understand the difference between external arguments and internal state
"""

import pytest

from creatures.vampire.vampire import Vampire


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestVampireCreation:
    """Tests for Vampire instantiation and default values."""

    def test_vampire_has_a_name(self):
        """A Vampire must have a name passed to the constructor."""
        vampire = Vampire("Vlad")
        assert vampire.name == "Vlad"

    def test_vampire_has_default_pet_bat(self):
        """A Vampire's pet defaults to 'bat' if not specified."""
        vampire = Vampire("Vlad")
        assert vampire.pet == "bat"

    def test_vampire_can_have_custom_pet(self):
        """A Vampire can have a custom pet using keyword argument."""
        vampire = Vampire("Dracula", pet="wolf")
        assert vampire.pet == "wolf"


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestVampireThirst:
    """Tests for Vampire thirst state - the core lesson of this exercise."""

    def test_vampire_is_initially_thirsty(self):
        """A newly created Vampire is always thirsty (internal state)."""
        vampire = Vampire("Vlad")
        assert vampire.thirsty is True

    def test_vampire_is_not_thirsty_after_drinking(self):
        """drink() changes thirsty state to False."""
        vampire = Vampire("Vlad")
        vampire.drink()
        assert vampire.thirsty is False

    def test_vampire_thirst_lifecycle(self):
        """Complete lifecycle test: thirsty -> drink -> not thirsty."""
        vampire = Vampire("Vlad")
        # Verify initial state
        assert vampire.thirsty is True

        # Trigger state change
        vampire.drink()

        # Verify new state
        assert vampire.thirsty is False


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestVampireMultipleInstances:
    """Tests ensuring each Vampire has independent state."""

    def test_drinking_does_not_affect_other_vampires(self):
        """Each Vampire instance maintains its own thirst state."""
        vlad = Vampire("Vlad")
        dracula = Vampire("Dracula")

        vlad.drink()

        assert vlad.thirsty is False
        assert dracula.thirsty is True  # Dracula is still thirsty
