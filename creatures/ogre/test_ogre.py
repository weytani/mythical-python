# ABOUTME: Test suite for the Ogre and Human classes.
# ABOUTME: Validates encounter mechanics, swing logic, and knock-out/apologize behavior.
"""
Test suite for the Ogre and Human classes.

This exercise builds on object interaction with layered conditional logic:
- Two classes (Ogre and Human) that interact through encounters
- Modular counters driving derived behavior (every 3rd encounter, every 2nd swing)
- State mutation across objects (Ogre modifies Human's knocked_out state)
- Multi-step cause-and-effect chains (encounter → notice → swing → knock out)

Learning Objectives:
- Understand chained conditional logic (counter thresholds triggering actions)
- Learn modular arithmetic for periodic behavior (% operator)
- Master cross-object state mutation (one object changes another's attributes)
- Practice default parameter values in constructors
"""

import pytest

from creatures.ogre.ogre import Ogre, Human


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestHumanCreation:
    """Tests for Human instantiation and default attributes."""

    def test_human_has_a_name(self):
        """A Human must have a name."""
        human = Human("Jane")
        assert human.name == "Jane"

    def test_human_starts_with_zero_encounters(self):
        """A newly created Human has zero encounters."""
        human = Human("Jane")
        assert human.encounter_counter == 0

    def test_human_starts_not_knocked_out(self):
        """A newly created Human is not knocked out."""
        human = Human("Jane")
        assert human.knocked_out is False


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestOgreCreation:
    """Tests for Ogre instantiation and default attributes."""

    def test_ogre_has_a_name(self):
        """An Ogre must have a name."""
        ogre = Ogre("Brak")
        assert ogre.name == "Brak"

    def test_ogre_lives_in_swamp_by_default(self):
        """An Ogre lives in a Swamp by default."""
        ogre = Ogre("Brak")
        assert ogre.home == "Swamp"

    def test_ogre_can_live_elsewhere(self):
        """An Ogre can be given a different home."""
        ogre = Ogre("Brak", "The Ritz")
        assert ogre.home == "The Ritz"


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestOgreEncounter:
    """Tests for encounter mechanics between Ogre and Human."""

    def test_ogre_encounter_increments_human_counter(self):
        """An encounter increments the Human's encounter counter."""
        ogre = Ogre("Brak")
        human = Human("Jane")

        ogre.encounter(human)

        assert human.encounter_counter == 1

    def test_human_notices_ogre_every_third_encounter(self):
        """A Human notices the Ogre on every 3rd encounter."""
        ogre = Ogre("Brak")
        human = Human("Jane")

        ogre.encounter(human)
        ogre.encounter(human)
        assert human.notices_ogre() is False

        ogre.encounter(human)
        assert human.notices_ogre() is True

    def test_human_notices_on_sixth_encounter(self):
        """A Human notices the Ogre again on the 6th encounter."""
        ogre = Ogre("Brak")
        human = Human("Jane")

        assert human.notices_ogre() is False

        ogre.encounter(human)
        ogre.encounter(human)
        ogre.encounter(human)
        assert human.notices_ogre() is True

        ogre.encounter(human)
        ogre.encounter(human)
        assert human.notices_ogre() is False

        ogre.encounter(human)
        assert human.notices_ogre() is True


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestOgreSwinging:
    """Tests for the Ogre's club-swinging behavior."""

    def test_ogre_can_swing_club(self):
        """An Ogre can swing its club at a Human."""
        ogre = Ogre("Brak")
        human = Human("Jane")

        ogre.swing_at(human)

        assert ogre.swings == 1

    def test_ogre_starts_with_zero_swings(self):
        """A newly created Ogre has zero swings."""
        ogre = Ogre("Brak")
        assert ogre.swings == 0

    def test_ogre_swings_when_human_notices(self):
        """The Ogre swings its club when the Human notices it."""
        ogre = Ogre("Brak")
        human = Human("Jane")

        ogre.encounter(human)
        assert ogre.swings == 0

        ogre.encounter(human)
        ogre.encounter(human)
        assert ogre.swings == 1

    def test_ogre_hits_human_every_second_swing(self):
        """The Ogre knocks out the Human on every 2nd swing."""
        ogre = Ogre("Brak")
        human = Human("Jane")

        ogre.encounter(human)
        ogre.encounter(human)
        ogre.encounter(human)
        ogre.encounter(human)
        ogre.encounter(human)
        ogre.encounter(human)

        assert human.encounter_counter == 6
        assert ogre.swings == 2
        assert human.knocked_out is True


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestOgreApologize:
    """Tests for the Ogre's apologize behavior."""

    def test_human_wakes_up_when_ogre_apologizes(self):
        """A knocked-out Human wakes up when the Ogre apologizes."""
        ogre = Ogre("Brak")
        human = Human("Jane")

        ogre.apologize(human)

        assert human.knocked_out is False
