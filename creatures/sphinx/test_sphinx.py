# ABOUTME: Test suite for the Sphinx class.
# ABOUTME: Validates riddle collection, answer checking, hero-eating, and rage behavior.
"""
Test suite for the Sphinx class.

This exercise builds on collection management and introduces dictionary-based state:
- Dictionary data structures for riddles (key-value pairs)
- FIFO queue logic (max 3 riddles, oldest dropped when exceeded)
- Conditional return values based on correctness and game state
- State tracking across multiple interactions (heroes_eaten counter)

Learning Objectives:
- Understand dictionary usage for structured data (riddle/answer pairs)
- Learn FIFO queue patterns with a fixed-size collection
- Master conditional logic with multiple outcomes (correct, wrong, final answer)
- Practice method return values that communicate game state
"""

import pytest

from creatures.sphinx.sphinx import Sphinx


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestSphinxCreation:
    """Tests for Sphinx instantiation and default attributes."""

    def test_sphinx_has_no_name(self):
        """A Sphinx has no name by default."""
        sphinx = Sphinx()
        assert sphinx.name is None

    def test_sphinx_starts_with_no_riddles(self):
        """A newly created Sphinx has no riddles."""
        sphinx = Sphinx()
        assert sphinx.riddles == []


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestSphinxCollecting:
    """Tests for Sphinx riddle collection behavior."""

    def test_sphinx_collects_riddles(self):
        """A Sphinx can collect a riddle."""
        sphinx = Sphinx()
        riddle = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        sphinx.collect_riddle(riddle)
        assert sphinx.riddles == [riddle]

    def test_sphinx_collects_only_three_riddles(self):
        """A Sphinx holds at most 3 riddles, dropping the oldest when exceeded (FIFO)."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        riddle2 = {
            "riddle": "How far can a fox run into a grove?",
            "answer": "Halfway, after that it's running out.",
        }
        riddle3 = {
            "riddle": "What starts with an 'e' and ends with an 'e' and contains one letter?",
            "answer": "An envelope",
        }
        riddle4 = {
            "riddle": "What's been around for millions of years but is never more than a month old?",
            "answer": "The moon",
        }
        sphinx.collect_riddle(riddle1)
        sphinx.collect_riddle(riddle2)
        sphinx.collect_riddle(riddle3)
        sphinx.collect_riddle(riddle4)
        assert sphinx.riddles == [riddle2, riddle3, riddle4]


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestSphinxCorrectAnswers:
    """Tests for Sphinx behavior when heroes answer correctly."""

    def test_sphinx_accepts_correct_answer_and_removes_riddle(self):
        """A correct answer removes the answered riddle from the collection."""
        sphinx = Sphinx()
        riddle = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        sphinx.collect_riddle(riddle)
        sphinx.attempt_answer("short")
        assert sphinx.riddles == []

    def test_sphinx_accepts_answers_in_any_order(self):
        """A correct answer removes the matching riddle regardless of position."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        riddle2 = {
            "riddle": "How far can a fox run into a grove?",
            "answer": "Halfway, after that it's running out.",
        }
        riddle3 = {
            "riddle": "What starts with an 'e' and ends with an 'e' and contains one letter?",
            "answer": "An envelope",
        }
        sphinx.collect_riddle(riddle1)
        sphinx.collect_riddle(riddle2)
        sphinx.collect_riddle(riddle3)
        sphinx.attempt_answer("An envelope")
        assert sphinx.riddles == [riddle1, riddle2]

    def test_sphinx_mocks_heroes_on_correct_answer(self):
        """A correct answer returns a mocking taunt from the Sphinx."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        riddle2 = {
            "riddle": "How far can a fox run into a grove?",
            "answer": "Halfway, after that it's running out.",
        }
        sphinx.collect_riddle(riddle1)
        sphinx.collect_riddle(riddle2)
        result = sphinx.attempt_answer("short")
        assert result == "That wasn't that hard, I bet you don't get the next one"


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestSphinxWrongAnswers:
    """Tests for Sphinx behavior when heroes answer incorrectly."""

    def test_sphinx_starts_having_eaten_no_heroes(self):
        """A newly created Sphinx has eaten no heroes."""
        sphinx = Sphinx()
        assert sphinx.heroes_eaten == 0

    def test_sphinx_eats_hero_on_wrong_answer(self):
        """A wrong answer causes the Sphinx to eat the hero."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        riddle2 = {
            "riddle": "How far can a fox run into a grove?",
            "answer": "Halfway, after that it's running out.",
        }
        riddle3 = {
            "riddle": "What starts with an 'e' and ends with an 'e' and contains one letter?",
            "answer": "An envelope",
        }
        sphinx.collect_riddle(riddle1)
        sphinx.collect_riddle(riddle2)
        sphinx.collect_riddle(riddle3)
        sphinx.attempt_answer("e")
        assert sphinx.riddles == [riddle1, riddle2, riddle3]
        assert sphinx.heroes_eaten == 1

    def test_sphinx_does_not_eat_hero_on_correct_answer(self):
        """A correct answer does not increment the eaten counter."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        riddle2 = {
            "riddle": "How far can a fox run into a grove?",
            "answer": "Halfway, after that it's running out.",
        }
        riddle3 = {
            "riddle": "What starts with an 'e' and ends with an 'e' and contains one letter?",
            "answer": "An envelope",
        }
        sphinx.collect_riddle(riddle1)
        sphinx.collect_riddle(riddle2)
        sphinx.collect_riddle(riddle3)
        sphinx.attempt_answer("short")
        assert sphinx.riddles == [riddle2, riddle3]
        assert sphinx.heroes_eaten == 0


@pytest.mark.skip(reason="Complete Medusa first, then unskip this test")
class TestSphinxRage:
    """Tests for Sphinx rage behavior when all riddles are answered."""

    def test_sphinx_laughs_on_wrong_answer(self):
        """A wrong answer returns a laughing taunt from the Sphinx."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        sphinx.collect_riddle(riddle1)
        result = sphinx.attempt_answer("e")
        assert result == "Haha! Puny human, you look delicious"

    def test_sphinx_screams_when_all_riddles_answered(self):
        """The Sphinx screams in rage when all riddles are answered correctly."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        riddle2 = {
            "riddle": "How far can a fox run into a grove?",
            "answer": "Halfway, after that it's running out.",
        }
        sphinx.collect_riddle(riddle1)
        sphinx.collect_riddle(riddle2)
        sphinx.attempt_answer("short")
        result = sphinx.attempt_answer("Halfway, after that it's running out.")
        assert result == 'PSSSSSSS THIS HAS NEVER HAPPENED, HOW DID YOU KNOW THE ANSWER WAS "Halfway, after that it\'s running out."???'

    def test_sphinx_rage_references_last_answered_riddle(self):
        """The Sphinx's rage message references the last riddle that was answered."""
        sphinx = Sphinx()
        riddle1 = {
            "riddle": "What word becomes shorter when you add two letters to it?",
            "answer": "short",
        }
        riddle2 = {
            "riddle": "How far can a fox run into a grove?",
            "answer": "Halfway, after that it's running out.",
        }
        sphinx.collect_riddle(riddle1)
        sphinx.collect_riddle(riddle2)
        sphinx.attempt_answer("Halfway, after that it's running out.")
        result = sphinx.attempt_answer("short")
        assert result == 'PSSSSSSS THIS HAS NEVER HAPPENED, HOW DID YOU KNOW THE ANSWER WAS "short"???'
