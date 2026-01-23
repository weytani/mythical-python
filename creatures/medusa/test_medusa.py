"""
Test suite for the Medusa and Person classes.

This exercise represents a major jump in complexity - object interaction:
- Two distinct classes that interact (Medusa and Person)
- One-to-many relationships (Medusa has many statues)
- State mutation across objects (Medusa modifies Person)
- FIFO queue logic (max 3 statues, oldest released when exceeded)

Learning Objectives:
- Understand object references and how one object can modify another
- Learn collection management (lists of objects)
- Master FIFO queue pattern with append/pop(0)
- Practice coupling between classes
"""

import pytest

from creatures.medusa.medusa import Medusa, Person


class TestPersonCreation:
    """Tests for Person instantiation."""

    def test_person_has_a_name(self):
        """A Person must have a name."""
        person = Person("Perseus")
        assert person.name == "Perseus"

    def test_person_is_not_stoned_by_default(self):
        """A Person is not stoned (turned to stone) by default."""
        person = Person("Perseus")
        assert person.stoned is False


class TestMedusaCreation:
    """Tests for Medusa instantiation."""

    def test_medusa_has_a_name(self):
        """A Medusa must have a name."""
        medusa = Medusa("Cassiopeia")
        assert medusa.name == "Cassiopeia"

    def test_medusa_starts_with_no_statues(self):
        """A newly created Medusa has no statues."""
        medusa = Medusa("Cassiopeia")
        assert medusa.statues == []
        assert len(medusa.statues) == 0


class TestMedusaStare:
    """Tests for Medusa's stare ability - the core lesson."""

    def test_medusa_can_turn_person_to_stone(self):
        """stare() turns a Person to stone."""
        medusa = Medusa("Cassiopeia")
        victim = Person("Perseus")

        assert victim.stoned is False
        medusa.stare(victim)
        assert victim.stoned is True

    def test_stoned_person_is_added_to_statues(self):
        """stare() adds the victim to Medusa's statues collection."""
        medusa = Medusa("Cassiopeia")
        victim = Person("Perseus")

        medusa.stare(victim)

        assert victim in medusa.statues
        assert len(medusa.statues) == 1

    def test_medusa_can_have_multiple_statues(self):
        """Medusa can turn multiple people to stone."""
        medusa = Medusa("Cassiopeia")
        v1 = Person("Victim 1")
        v2 = Person("Victim 2")

        medusa.stare(v1)
        medusa.stare(v2)

        assert v1 in medusa.statues
        assert v2 in medusa.statues
        assert len(medusa.statues) == 2

    def test_medusa_can_have_three_statues(self):
        """Medusa can have up to 3 statues."""
        medusa = Medusa("Cassiopeia")
        v1 = Person("1")
        v2 = Person("2")
        v3 = Person("3")

        medusa.stare(v1)
        medusa.stare(v2)
        medusa.stare(v3)

        assert len(medusa.statues) == 3
        assert all(v.stoned for v in [v1, v2, v3])


class TestMedusaStatueLimit:
    """Tests for FIFO queue logic - max 3 statues."""

    def test_fourth_victim_releases_first(self):
        """When a 4th person is stoned, the 1st is released (FIFO)."""
        medusa = Medusa("Cassiopeia")
        v1 = Person("1")
        v2 = Person("2")
        v3 = Person("3")
        v4 = Person("4")

        medusa.stare(v1)
        medusa.stare(v2)
        medusa.stare(v3)
        medusa.stare(v4)

        # v4 should be stoned and in statues
        assert v4.stoned is True
        assert v4 in medusa.statues

        # v1 should be released (no longer stoned, not in statues)
        assert v1.stoned is False
        assert v1 not in medusa.statues

        # Still only 3 statues
        assert len(medusa.statues) == 3

    def test_statue_limit_maintains_fifo_order(self):
        """The oldest statue is always released first."""
        medusa = Medusa("Cassiopeia")
        victims = [Person(str(i)) for i in range(5)]

        # Stare at all 5 victims
        for v in victims:
            medusa.stare(v)

        # Only last 3 should be statues
        assert len(medusa.statues) == 3
        assert victims[0] not in medusa.statues
        assert victims[1] not in medusa.statues
        assert victims[2] in medusa.statues
        assert victims[3] in medusa.statues
        assert victims[4] in medusa.statues

        # First two should be un-stoned
        assert victims[0].stoned is False
        assert victims[1].stoned is False

    def test_released_person_can_be_stoned_again(self):
        """A released person can be turned to stone again."""
        medusa = Medusa("Cassiopeia")
        v1 = Person("1")
        v2 = Person("2")
        v3 = Person("3")
        v4 = Person("4")

        medusa.stare(v1)
        medusa.stare(v2)
        medusa.stare(v3)
        medusa.stare(v4)  # v1 is released

        assert v1.stoned is False

        # Stare at v1 again
        medusa.stare(v1)  # v2 is released

        assert v1.stoned is True
        assert v1 in medusa.statues
        assert v2.stoned is False


class TestMedusaMultipleInstances:
    """Tests ensuring each Medusa has independent state."""

    def test_each_medusa_has_own_statues(self):
        """Each Medusa maintains their own statues collection."""
        medusa1 = Medusa("Stheno")
        medusa2 = Medusa("Euryale")
        victim = Person("Unlucky")

        medusa1.stare(victim)

        assert victim in medusa1.statues
        assert victim not in medusa2.statues
        assert len(medusa1.statues) == 1
        assert len(medusa2.statues) == 0

    def test_different_medusas_can_share_victims(self):
        """Multiple Medusas can have the same person as a statue."""
        medusa1 = Medusa("Stheno")
        medusa2 = Medusa("Euryale")
        victim = Person("Very Unlucky")

        medusa1.stare(victim)
        medusa2.stare(victim)

        # Both have the victim as a statue
        assert victim in medusa1.statues
        assert victim in medusa2.statues
        # Victim is definitely stoned
        assert victim.stoned is True


class TestObjectReferences:
    """Tests demonstrating object reference behavior."""

    def test_statue_is_same_object_as_original(self):
        """The statue in the list is the same object (reference) as the original."""
        medusa = Medusa("Cassiopeia")
        victim = Person("Perseus")

        medusa.stare(victim)

        # The statue in the list IS the same object
        assert medusa.statues[0] is victim

    def test_modifying_person_reflects_in_statue_list(self):
        """Changes to a Person object are visible through the statues list."""
        medusa = Medusa("Cassiopeia")
        victim = Person("Perseus")

        medusa.stare(victim)

        # Both references point to the same object
        assert victim.stoned is True
        assert medusa.statues[0].stoned is True

        # If we could un-stone via the victim reference, it would show in statues
        # (This demonstrates reference semantics)
