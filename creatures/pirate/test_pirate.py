"""
Test suite for the Pirate class.

This exercise introduces state flags and accumulators:
- State flags triggered by thresholds (cursed after 3 heinous acts)
- Accumulator pattern (booty as a "wallet")
- Multiple independent state mechanisms (acts vs booty)

Learning Objectives:
- Understand state flags that get set based on thresholds
- Learn the accumulator/wallet pattern (booty += 100)
- Practice tracking multiple independent counters
- Distinguish between computed properties (Dragon) and triggered flags (Pirate)
"""

import pytest

from creatures.pirate.pirate import Pirate


class TestPirateCreation:
    """Tests for Pirate instantiation and default values."""

    def test_pirate_has_a_name(self):
        """A Pirate must have a name."""
        pirate = Pirate("Blackbeard")
        assert pirate.name == "Blackbeard"

    def test_pirate_has_default_job_scallywag(self):
        """A Pirate's job defaults to 'Scallywag'."""
        pirate = Pirate("Blackbeard")
        assert pirate.job == "Scallywag"

    def test_pirate_can_have_custom_job(self):
        """A Pirate can have a custom job."""
        pirate = Pirate("Blackbeard", job="Captain")
        assert pirate.job == "Captain"

    def test_pirate_starts_not_cursed(self):
        """A newly created Pirate is not cursed."""
        pirate = Pirate("Blackbeard")
        assert pirate.cursed is False

    def test_pirate_starts_with_no_booty(self):
        """A newly created Pirate has no booty."""
        pirate = Pirate("Blackbeard")
        assert pirate.booty == 0


class TestPirateHeinousActs:
    """Tests for cursed state triggered by heinous acts."""

    def test_pirate_is_not_cursed_after_one_act(self):
        """A Pirate is not cursed after one heinous act."""
        pirate = Pirate("Blackbeard")
        pirate.commit_heinous_act()
        assert pirate.cursed is False

    def test_pirate_is_not_cursed_after_two_acts(self):
        """A Pirate is not cursed after two heinous acts."""
        pirate = Pirate("Blackbeard")
        pirate.commit_heinous_act()
        pirate.commit_heinous_act()
        assert pirate.cursed is False

    def test_pirate_is_cursed_after_three_acts(self):
        """A Pirate becomes cursed after three heinous acts."""
        pirate = Pirate("Blackbeard")
        pirate.commit_heinous_act()
        pirate.commit_heinous_act()
        pirate.commit_heinous_act()
        assert pirate.cursed is True

    def test_pirate_curse_progression(self):
        """Complete curse progression: not cursed until 3 acts."""
        pirate = Pirate("Blackbeard")
        assert pirate.cursed is False

        pirate.commit_heinous_act()
        assert pirate.cursed is False

        pirate.commit_heinous_act()
        assert pirate.cursed is False

        pirate.commit_heinous_act()
        assert pirate.cursed is True  # Threshold reached

    def test_pirate_stays_cursed_after_more_acts(self):
        """A cursed Pirate remains cursed after more heinous acts."""
        pirate = Pirate("Blackbeard")
        for _ in range(5):
            pirate.commit_heinous_act()
        assert pirate.cursed is True


class TestPirateBooty:
    """Tests for booty accumulation - the wallet pattern."""

    def test_pirate_gains_booty_from_robbing_ship(self):
        """rob_ship() increases booty by 100."""
        pirate = Pirate("Blackbeard")
        pirate.rob_ship()
        assert pirate.booty == 100

    def test_pirate_accumulates_booty(self):
        """A Pirate accumulates booty from multiple robberies."""
        pirate = Pirate("Blackbeard")
        pirate.rob_ship()
        pirate.rob_ship()
        pirate.rob_ship()
        assert pirate.booty == 300

    def test_robbing_ship_does_not_affect_curse(self):
        """Robbing ships does not contribute to the curse."""
        pirate = Pirate("Blackbeard")
        for _ in range(10):
            pirate.rob_ship()
        assert pirate.booty == 1000
        assert pirate.cursed is False


class TestPirateIndependentStates:
    """Tests ensuring booty and curse are independent."""

    def test_heinous_acts_do_not_affect_booty(self):
        """Heinous acts do not change booty."""
        pirate = Pirate("Blackbeard")
        pirate.commit_heinous_act()
        pirate.commit_heinous_act()
        pirate.commit_heinous_act()
        assert pirate.booty == 0
        assert pirate.cursed is True

    def test_pirate_can_be_rich_and_cursed(self):
        """A Pirate can accumulate booty and become cursed independently."""
        pirate = Pirate("Blackbeard")
        pirate.rob_ship()
        pirate.commit_heinous_act()
        pirate.rob_ship()
        pirate.commit_heinous_act()
        pirate.rob_ship()
        pirate.commit_heinous_act()

        assert pirate.booty == 300
        assert pirate.cursed is True


class TestPirateMultipleInstances:
    """Tests ensuring each Pirate has independent state."""

    def test_acts_do_not_affect_other_pirates(self):
        """Each Pirate tracks their own heinous acts."""
        blackbeard = Pirate("Blackbeard")
        sparrow = Pirate("Jack Sparrow")

        blackbeard.commit_heinous_act()
        blackbeard.commit_heinous_act()
        blackbeard.commit_heinous_act()

        assert blackbeard.cursed is True
        assert sparrow.cursed is False

    def test_booty_does_not_affect_other_pirates(self):
        """Each Pirate has their own booty."""
        blackbeard = Pirate("Blackbeard")
        sparrow = Pirate("Jack Sparrow")

        blackbeard.rob_ship()
        blackbeard.rob_ship()

        assert blackbeard.booty == 200
        assert sparrow.booty == 0
