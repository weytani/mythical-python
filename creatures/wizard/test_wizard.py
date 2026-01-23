"""
Test suite for the Wizard class.

This exercise emphasizes string manipulation and boolean arguments:
- Boolean default parameters in constructors
- String transformation methods (f-strings, .upper(), etc.)
- Resource management (magic power / rested state)

Learning Objectives:
- Understand boolean default arguments (bearded=True)
- Master string manipulation with f-strings
- Practice methods that transform input strings
- Learn resource depletion patterns (cast reduces power)
"""

import pytest

from creatures.wizard.wizard import Wizard


class TestWizardCreation:
    """Tests for Wizard instantiation and default values."""

    def test_wizard_has_a_name(self):
        """A Wizard must have a name."""
        wizard = Wizard("Gandalf")
        assert wizard.name == "Gandalf"

    def test_wizard_is_bearded_by_default(self):
        """A Wizard is bearded by default (boolean True)."""
        wizard = Wizard("Gandalf")
        assert wizard.bearded is True

    def test_wizard_can_be_beardless(self):
        """A Wizard can be created without a beard."""
        wizard = Wizard("Merlin", bearded=False)
        assert wizard.bearded is False

    def test_wizard_bearded_is_boolean_true(self):
        """The bearded attribute is specifically True, not just truthy."""
        wizard = Wizard("Gandalf")
        assert wizard.bearded is True
        assert type(wizard.bearded) is bool

    def test_wizard_starts_rested(self):
        """A newly created Wizard is rested (has full magic power)."""
        wizard = Wizard("Gandalf")
        assert wizard.rested is True


class TestWizardIncantation:
    """Tests for string manipulation via incantation method."""

    def test_incantation_prepends_sudo(self):
        """incantation() prepends 'sudo' to the phrase."""
        wizard = Wizard("Gandalf")
        assert wizard.incantation("rm -rf /") == "sudo rm -rf /"

    def test_incantation_works_with_any_phrase(self):
        """incantation() works with various phrases."""
        wizard = Wizard("Gandalf")
        assert wizard.incantation("make it so") == "sudo make it so"
        assert wizard.incantation("open sesame") == "sudo open sesame"

    def test_incantation_with_empty_string(self):
        """incantation() handles empty strings."""
        wizard = Wizard("Gandalf")
        assert wizard.incantation("") == "sudo "

    def test_incantation_preserves_case(self):
        """incantation() preserves the original case of the phrase."""
        wizard = Wizard("Gandalf")
        assert wizard.incantation("SHOUT") == "sudo SHOUT"
        assert wizard.incantation("whisper") == "sudo whisper"


class TestWizardCasting:
    """Tests for casting spells and fatigue."""

    def test_wizard_becomes_tired_after_casting(self):
        """cast() makes the wizard tired (no longer rested)."""
        wizard = Wizard("Gandalf")
        wizard.cast()
        assert wizard.rested is False

    def test_wizard_can_cast_multiple_times(self):
        """A Wizard can cast multiple times (stays tired)."""
        wizard = Wizard("Gandalf")
        wizard.cast()
        wizard.cast()
        wizard.cast()
        assert wizard.rested is False

    def test_cast_returns_spell_message(self):
        """cast() returns a message about casting a spell."""
        wizard = Wizard("Gandalf")
        result = wizard.cast()
        assert "cast" in result.lower() or "spell" in result.lower()


class TestWizardRest:
    """Tests for wizard rest/recovery."""

    def test_wizard_can_rest_to_recover(self):
        """rest() restores the wizard's rested state."""
        wizard = Wizard("Gandalf")
        wizard.cast()
        assert wizard.rested is False
        wizard.rest()
        assert wizard.rested is True

    def test_resting_when_already_rested(self):
        """rest() works even if wizard is already rested."""
        wizard = Wizard("Gandalf")
        assert wizard.rested is True
        wizard.rest()
        assert wizard.rested is True


class TestWizardMultipleInstances:
    """Tests ensuring each Wizard has independent state."""

    def test_casting_does_not_affect_other_wizards(self):
        """Each Wizard maintains their own rested state."""
        gandalf = Wizard("Gandalf")
        merlin = Wizard("Merlin")

        gandalf.cast()

        assert gandalf.rested is False
        assert merlin.rested is True

    def test_beard_is_independent(self):
        """Each Wizard has their own beard status."""
        gandalf = Wizard("Gandalf", bearded=True)
        voldemort = Wizard("Voldemort", bearded=False)

        assert gandalf.bearded is True
        assert voldemort.bearded is False
