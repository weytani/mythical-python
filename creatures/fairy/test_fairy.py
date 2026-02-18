# ABOUTME: Test suite for the Fairy class.
# ABOUTME: Validates fairy dust, clothing, disposition, changeling, and human ward behaviors.
"""
Test suite for the Fairy class.

This exercise explores mutable state, dictionary mutation, and behavioral triggers:
- Default and accumulated state (dust, clothes, human wards)
- Dictionary mutation by reference (replacing infant dispositions)
- Conditional behavior based on disposition (good natured vs vengeful)
- State transitions triggered by thresholds (calming after three changelings)

Learning Objectives:
- Understand mutable default values and dictionary mutation
- Learn how methods can modify external objects passed as arguments
- Master conditional behavior based on internal state
- Practice state accumulation with lists and counters
- Understand object identity vs equality (is vs ==)
"""

import pytest

from creatures.fairy.fairy import Fairy


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestFairyCreation:
    """Tests for Fairy instantiation and default attributes."""

    def test_fairy_has_a_name(self):
        """A Fairy must have a name."""
        fairy = Fairy("Holly")
        assert fairy.name == "Holly"

    def test_fairy_has_default_dust(self):
        """A Fairy starts with 10 dust."""
        fairy = Fairy("Mab")
        assert fairy.dust == 10


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestFairyDust:
    """Tests for Fairy dust accumulation mechanics."""

    def test_fairy_gets_dust_from_others_belief(self):
        """A Fairy gains 1 dust when someone else believes in her."""
        fairy = Fairy("Sookie")
        dust_before = fairy.dust
        fairy.receive_belief()
        assert fairy.dust == dust_before + 1

    def test_fairy_gets_more_dust_from_believing_in_herself(self):
        """A Fairy gains 10 dust when she believes in herself."""
        fairy = Fairy("Tinkerbell")
        dust_before = fairy.dust
        fairy.believe()
        assert fairy.dust == dust_before + 10


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestFairyClothes:
    """Tests for Fairy clothing and dress-making from flowers."""

    def test_fairy_starts_with_iris_dress(self):
        """A Fairy starts with a single Iris dress."""
        fairy = Fairy("Rose")
        assert fairy.clothes == {"dresses": ["Iris"]}

    def test_fairy_turns_flowers_into_dresses(self):
        """A Fairy can turn flowers into dresses."""
        fairy = Fairy("Honeysuckle")
        fairy.make_dresses(["Daffodil", "Tulip", "Poppy"])
        assert fairy.clothes["dresses"] == ["Iris", "Daffodil", "Tulip", "Poppy"]

    def test_fairy_accumulates_dresses_across_calls(self):
        """A Fairy accumulates dresses across multiple make_dresses calls."""
        fairy = Fairy("Cosmo Pepperfeet")
        fairy.make_dresses(["Ranunculus", "Daisy"])
        fairy.make_dresses(["Hydrangea", "Forget-me-not"])
        assert fairy.clothes["dresses"] == [
            "Iris",
            "Ranunculus",
            "Daisy",
            "Hydrangea",
            "Forget-me-not",
        ]


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestFairyDisposition:
    """Tests for Fairy disposition and provocation."""

    def test_fairy_starts_good_natured(self):
        """A Fairy starts with a good natured disposition."""
        fairy = Fairy("Cologne")
        assert fairy.disposition == "Good natured"

    def test_fairy_becomes_vengeful_when_provoked(self):
        """A Fairy becomes vengeful when provoked."""
        fairy = Fairy("Aine")
        fairy.provoke()
        assert fairy.disposition == "Vengeful"


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestFairyChangelings:
    """Tests for Fairy changeling behavior - replacing infant dispositions."""

    def test_fairy_replaces_infant_disposition_when_vengeful(self):
        """A vengeful Fairy replaces infant dispositions with 'Malicious'."""
        fairy = Fairy("Claudine")
        first_infant = {"name": "Sue", "eyes": "Blue", "disposition": "Sweet"}
        second_infant = {"name": "Henry", "eyes": "Brown", "disposition": "Charming"}

        fairy.provoke()
        fairy.replace_infant(first_infant)
        fairy.replace_infant(second_infant)

        assert first_infant == {
            "name": "Sue",
            "eyes": "Blue",
            "disposition": "Malicious",
        }
        assert second_infant == {
            "name": "Henry",
            "eyes": "Brown",
            "disposition": "Malicious",
        }

    def test_fairy_does_not_replace_infant_when_good_natured(self):
        """A good natured Fairy does not replace an infant's disposition."""
        fairy = Fairy("Marceline")
        first_infant = {"name": "Josiah", "eyes": "Green", "disposition": "Calm"}

        result = fairy.replace_infant(first_infant)

        assert result is first_infant


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestFairyHumanWards:
    """Tests for Fairy human ward collection and calming behavior."""

    def test_fairy_raises_stolen_infants(self):
        """A vengeful Fairy collects replaced infants as human wards."""
        fairy = Fairy("Winnie")
        first_infant = {"name": "Liam", "eyes": "Blue", "disposition": "Cheerful"}
        second_infant = {"name": "Nora", "eyes": "Hazel", "disposition": "Gentle"}

        fairy.provoke()
        fairy.replace_infant(first_infant)
        fairy.replace_infant(second_infant)

        assert fairy.human_wards == [first_infant, second_infant]

    def test_fairy_calms_down_after_three_stolen_infants(self):
        """A Fairy returns to good natured after stealing three infants."""
        fairy = Fairy("Basil")
        first_infant = {"name": "Ada", "eyes": "Brown", "disposition": "Quiet"}
        second_infant = {"name": "Felix", "eyes": "Green", "disposition": "Playful"}
        third_infant = {"name": "Clara", "eyes": "Blue", "disposition": "Spirited"}

        fairy.provoke()
        fairy.replace_infant(first_infant)
        fairy.replace_infant(second_infant)
        fairy.replace_infant(third_infant)

        assert fairy.disposition == "Good natured"
