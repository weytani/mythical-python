# ABOUTME: Test suite for the Direwolf and Stark classes.
# ABOUTME: Validates pack protection mechanics, location-based guarding, and inter-object state.
"""
Test suite for the Direwolf and Stark classes.

This exercise teaches multi-object interaction with bidirectional relationships:
- Two classes (Direwolf and Stark) that modify each other's state
- Location-based conditional logic (protection only works at same location)
- Capacity constraints (max 2 Starks per Direwolf)
- Bidirectional state changes (protect/leave affects both objects)

Learning Objectives:
- Understand bidirectional object relationships (Direwolf knows its Starks, Stark knows it's safe)
- Learn conditional mutation (location matching before state change)
- Master capacity-limited collections with guard clauses
- Practice cleanup logic (leaving reverses state changes)
"""

import pytest

from creatures.direwolf.direwolf import Direwolf, Stark


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestStarkCreation:
    """Tests for Stark instantiation and default attributes."""

    def test_stark_has_a_name(self):
        """A Stark must have a name."""
        stark = Stark("Bran")
        assert stark.name == "Bran"

    def test_stark_defaults_to_winterfell(self):
        """A Stark's location defaults to Winterfell."""
        stark = Stark("Bran")
        assert stark.location == "Winterfell"

    def test_stark_starts_unsafe(self):
        """A Stark is not safe by default."""
        stark = Stark("John", "Winterfell")
        assert stark.safe is False


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestStarkHouseWords:
    """Tests for Stark house words - reflects safety state."""

    def test_stark_says_winter_is_coming_when_unsafe(self):
        """An unsafe Stark says 'Winter is Coming'."""
        stark = Stark("John", "Winterfell")
        assert stark.house_words() == "Winter is Coming"

    def test_stark_says_north_remembers_when_safe(self):
        """A safe Stark says 'The North Remembers'."""
        stark = Stark("Arya", "Dorn")
        direwolf = Direwolf("Nymeria", "Dorn")
        direwolf.protect(stark)
        assert stark.house_words() == "The North Remembers"


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestDirewolfCreation:
    """Tests for Direwolf instantiation and default attributes."""

    def test_direwolf_has_a_name(self):
        """A Direwolf must have a name."""
        direwolf = Direwolf("Nymeria")
        assert direwolf.name == "Nymeria"

    def test_direwolf_defaults_to_beyond_the_wall(self):
        """A Direwolf's home defaults to 'Beyond the Wall'."""
        direwolf = Direwolf("Lady")
        assert direwolf.home == "Beyond the Wall"

    def test_direwolf_defaults_to_massive(self):
        """A Direwolf's size defaults to 'Massive'."""
        direwolf = Direwolf("Ghost")
        assert direwolf.size == "Massive"

    def test_direwolf_can_have_custom_home_and_size(self):
        """A Direwolf can be created with a custom home and size."""
        direwolf = Direwolf("Shaggydog", "Karhold", "Smol Pupper")
        assert direwolf.name == "Shaggydog"
        assert direwolf.home == "Karhold"
        assert direwolf.size == "Smol Pupper"


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestDirewolfProtect:
    """Tests for Direwolf protection mechanics - the core lesson."""

    def test_direwolf_starts_with_no_starks(self):
        """A Direwolf starts with no Starks to protect."""
        direwolf = Direwolf("Nymeria")
        stark = Stark("Arya")
        assert direwolf.starks_to_protect == []

    def test_direwolf_protects_stark_at_same_location(self):
        """A Direwolf can protect a Stark at the same location."""
        direwolf = Direwolf("Nymeria", "Riverlands")
        stark = Stark("Arya", "Riverlands")
        direwolf.protect(stark)
        assert len(direwolf.starks_to_protect) == 1
        assert direwolf.starks_to_protect[0].name == "Arya"

    def test_direwolf_only_protects_if_locations_match(self):
        """A Direwolf cannot protect a Stark at a different location."""
        direwolf = Direwolf("Ghost")
        stark = Stark("John", "King's Landing")
        direwolf.protect(stark)
        assert direwolf.starks_to_protect == []

    def test_direwolf_protects_max_two_starks(self):
        """A Direwolf can protect at most two Starks."""
        direwolf1 = Direwolf("Summer", "Winterfell")
        direwolf2 = Direwolf("Grey Wind", "Winterfell")

        sansa = Stark("Sansa", "Winterfell")
        john = Stark("John", "Winterfell")
        rob = Stark("Rob", "Winterfell")
        bran = Stark("Bran", "Winterfell")
        arya = Stark("Arya", "Winterfell")

        direwolf1.protect(sansa)
        direwolf1.protect(john)

        direwolf2.protect(rob)
        direwolf2.protect(bran)
        direwolf2.protect(arya)

        assert len(direwolf1.starks_to_protect) == 2
        assert direwolf1.starks_to_protect[0].name == "Sansa"
        assert direwolf1.starks_to_protect[1].name == "John"

        assert len(direwolf2.starks_to_protect) == 2
        assert direwolf2.starks_to_protect[0].name == "Rob"
        assert direwolf2.starks_to_protect[1].name == "Bran"


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestDirewolfHunting:
    """Tests for Direwolf hunting behavior - derived from protection state."""

    def test_direwolf_hunts_when_not_protecting(self):
        """A Direwolf hunts white walkers when not protecting any Starks."""
        direwolf = Direwolf("Nymeria", "Winterfell")
        stark = Stark("Sansa")
        assert direwolf.hunts_white_walkers is True

    def test_direwolf_stops_hunting_when_protecting(self):
        """A Direwolf stops hunting white walkers when protecting a Stark."""
        direwolf = Direwolf("Nymeria", "Winterfell")
        stark = Stark("Sansa")
        direwolf.protect(stark)
        assert direwolf.hunts_white_walkers is False


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestDirewolfLeave:
    """Tests for Direwolf leaving a Stark - cleanup and state reversal."""

    def test_direwolf_can_leave_stark(self):
        """A Direwolf can leave a Stark it was protecting."""
        direwolf1 = Direwolf("Summer", "Winterfell")
        direwolf2 = Direwolf("Lady", "Winterfell")
        sansa = Stark("Sansa")
        arya = Stark("Arya")

        direwolf1.protect(arya)
        assert arya.safe is True

        direwolf2.protect(sansa)
        direwolf1.leave(arya)

        assert direwolf1.starks_to_protect == []
        assert direwolf2.starks_to_protect[0].name == "Sansa"
        assert arya.safe is False

    def test_stark_becomes_unsafe_when_direwolf_leaves(self):
        """A Stark becomes unsafe when their Direwolf leaves."""
        direwolf = Direwolf("Nymeria", "Dorn")
        stark = Stark("Arya", "Dorn")

        direwolf.protect(stark)
        assert stark.safe is True

        direwolf.leave(stark)
        assert stark.safe is False
