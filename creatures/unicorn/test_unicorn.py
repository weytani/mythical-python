"""
Test suite for the Unicorn class.

This is the entry point to the TDD curriculum. The Unicorn exercise introduces:
- Class constructors with __init__
- Default parameter values (keyword arguments)
- Type hints
- Basic string manipulation

Learning Objectives:
- Understand how to create a class with required and optional parameters
- Learn Python's default argument syntax: def __init__(self, name: str, color: str = "silver")
- Practice writing methods that return boolean values
- Practice string formatting with f-strings
"""

import pytest

from creatures.unicorn.unicorn import Unicorn


class TestUnicornCreation:
    """Tests for Unicorn instantiation and default values."""

    def test_unicorn_has_a_name(self):
        """A Unicorn must have a name passed to the constructor."""
        unicorn = Unicorn("Robert")
        assert unicorn.name == "Robert"

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_has_default_color_silver(self):
        """A Unicorn's color defaults to 'silver' if not specified."""
        unicorn = Unicorn("Robert")
        assert unicorn.color == "silver"

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_is_silver_returns_true_for_default_color(self):
        """is_silver() returns True when color is the default 'silver'."""
        unicorn = Unicorn("Robert")
        assert unicorn.is_silver() is True


class TestUnicornCustomColor:
    """Tests for Unicorn with custom color."""

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_can_have_custom_color(self):
        """A Unicorn can be created with a custom color using keyword argument."""
        unicorn = Unicorn("Barbara", color="purple")
        assert unicorn.color == "purple"

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_is_silver_returns_false_for_custom_color(self):
        """is_silver() returns False when color is not 'silver'."""
        unicorn = Unicorn("Barbara", color="purple")
        assert unicorn.is_silver() is False

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_can_have_white_color(self):
        """A Unicorn can be white (common alternative default in other implementations)."""
        unicorn = Unicorn("Snowflake", color="white")
        assert unicorn.color == "white"
        assert unicorn.is_silver() is False


class TestUnicornSpeech:
    """Tests for Unicorn speech with sparkles."""

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_says_phrase_with_sparkles(self):
        """say() wraps the phrase in sparkle decorations."""
        unicorn = Unicorn("Johnny")
        assert unicorn.say("Wonderful!") == "**;* Wonderful! *;**"

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_says_different_phrases(self):
        """say() works with any phrase."""
        unicorn = Unicorn("Sparkles")
        assert unicorn.say("Hello") == "**;* Hello *;**"
        assert unicorn.say("I love TDD") == "**;* I love TDD *;**"

    @pytest.mark.skip(reason="Unskip this test to continue")
    def test_unicorn_says_empty_string(self):
        """say() handles empty strings gracefully."""
        unicorn = Unicorn("Silent")
        assert unicorn.say("") == "**;*  *;**"
