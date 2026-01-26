"""
Test suite for the Hobbit class.

This exercise focuses on lifecycle modeling and boundary conditions:
- Age-based state transitions (child -> adult -> old)
- Incrementing counters (age via celebrate_birthday)
- Conditional logic based on integer ranges
- Name-based conditional logic (has_ring)
- Boundary condition testing (critical TDD lesson)

Learning Objectives:
- Understand lifecycle modeling with discrete states from continuous variables
- Master boundary condition testing (age 32 vs 33, age 100 vs 101)
- Practice @property decorators for computed boolean states
- Learn name-based conditional returns
"""

import pytest

from creatures.hobbit.hobbit import Hobbit


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestHobbitCreation:
    """Tests for Hobbit instantiation and default values."""

    def test_hobbit_has_a_name(self):
        """A Hobbit must have a name."""
        hobbit = Hobbit("Frodo")
        assert hobbit.name == "Frodo"

    def test_hobbit_has_default_disposition_homebody(self):
        """A Hobbit's disposition defaults to 'homebody'."""
        hobbit = Hobbit("Sam")
        assert hobbit.disposition == "homebody"

    def test_hobbit_can_have_custom_disposition(self):
        """A Hobbit can have a custom disposition."""
        hobbit = Hobbit("Frodo", disposition="adventurous")
        assert hobbit.disposition == "adventurous"

    def test_hobbit_starts_at_age_zero(self):
        """A newly created Hobbit starts at age 0."""
        hobbit = Hobbit("Frodo")
        assert hobbit.age == 0


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestHobbitAging:
    """Tests for Hobbit aging via celebrate_birthday."""

    def test_hobbit_ages_on_birthday(self):
        """celebrate_birthday() increments the Hobbit's age."""
        hobbit = Hobbit("Frodo")
        hobbit.celebrate_birthday()
        assert hobbit.age == 1

    def test_hobbit_can_have_multiple_birthdays(self):
        """A Hobbit can celebrate multiple birthdays."""
        hobbit = Hobbit("Frodo")
        for _ in range(33):
            hobbit.celebrate_birthday()
        assert hobbit.age == 33


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestHobbitAdulthood:
    """Tests for is_adult property - boundary conditions are critical."""

    def test_hobbit_is_not_adult_at_age_zero(self):
        """A newborn Hobbit is not an adult."""
        hobbit = Hobbit("Frodo")
        assert hobbit.is_adult is False

    def test_hobbit_is_not_adult_at_age_32(self):
        """A Hobbit at exactly age 32 is NOT an adult (boundary test)."""
        hobbit = Hobbit("Frodo")
        for _ in range(32):
            hobbit.celebrate_birthday()
        assert hobbit.age == 32
        assert hobbit.is_adult is False

    def test_hobbit_is_adult_at_age_33(self):
        """A Hobbit at age 33 IS an adult (boundary test)."""
        hobbit = Hobbit("Frodo")
        for _ in range(33):
            hobbit.celebrate_birthday()
        assert hobbit.age == 33
        assert hobbit.is_adult is True

    def test_hobbit_remains_adult_after_33(self):
        """A Hobbit remains an adult after age 33."""
        hobbit = Hobbit("Frodo")
        for _ in range(50):
            hobbit.celebrate_birthday()
        assert hobbit.is_adult is True


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestHobbitOldAge:
    """Tests for is_old property - boundary conditions are critical."""

    def test_hobbit_is_not_old_at_age_zero(self):
        """A newborn Hobbit is not old."""
        hobbit = Hobbit("Frodo")
        assert hobbit.is_old is False

    def test_hobbit_is_not_old_at_age_100(self):
        """A Hobbit at exactly age 100 is NOT old (boundary test)."""
        hobbit = Hobbit("Frodo")
        for _ in range(100):
            hobbit.celebrate_birthday()
        assert hobbit.age == 100
        assert hobbit.is_old is False

    def test_hobbit_is_old_at_age_101(self):
        """A Hobbit at age 101 IS old (boundary test)."""
        hobbit = Hobbit("Frodo")
        for _ in range(101):
            hobbit.celebrate_birthday()
        assert hobbit.age == 101
        assert hobbit.is_old is True

    def test_old_hobbit_is_also_adult(self):
        """An old Hobbit is also an adult."""
        hobbit = Hobbit("Frodo")
        for _ in range(101):
            hobbit.celebrate_birthday()
        assert hobbit.is_old is True
        assert hobbit.is_adult is True


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestHobbitRing:
    """Tests for has_ring method - name-based conditional logic."""

    def test_frodo_has_the_ring(self):
        """Frodo has the ring."""
        hobbit = Hobbit("Frodo")
        assert hobbit.has_ring() is True

    def test_sam_does_not_have_the_ring(self):
        """Sam does not have the ring."""
        hobbit = Hobbit("Sam")
        assert hobbit.has_ring() is False

    def test_other_hobbits_do_not_have_the_ring(self):
        """Other hobbits do not have the ring."""
        merry = Hobbit("Merry")
        pippin = Hobbit("Pippin")
        assert merry.has_ring() is False
        assert pippin.has_ring() is False

    def test_ring_ownership_is_case_sensitive(self):
        """Ring ownership check is case-sensitive."""
        hobbit = Hobbit("frodo")  # lowercase
        assert hobbit.has_ring() is False


@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")
class TestHobbitLifecycle:
    """Integration tests for complete Hobbit lifecycle."""

    def test_hobbit_lifecycle_progression(self):
        """A Hobbit progresses through life stages correctly."""
        hobbit = Hobbit("Bilbo", disposition="adventurous")

        # Starts as child
        assert hobbit.is_adult is False
        assert hobbit.is_old is False

        # Age to adulthood
        for _ in range(33):
            hobbit.celebrate_birthday()
        assert hobbit.is_adult is True
        assert hobbit.is_old is False

        # Age to old
        for _ in range(68):  # 33 + 68 = 101
            hobbit.celebrate_birthday()
        assert hobbit.age == 101
        assert hobbit.is_adult is True
        assert hobbit.is_old is True
