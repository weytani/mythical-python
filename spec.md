# Mythical Python — New Creatures Specification

## Overview

Add four new creature exercises to the existing TDD curriculum, ported from the JavaScript [mythical-critters](https://github.com/turingschool-examples/mythical-critters) repo. Each exercise is adapted to idiomatic Python conventions while preserving the original pedagogical intent and test-driven workflow.

## Scope

| # | Creature | Classes | Source JS Files |
|---|----------|---------|-----------------|
| 8 | Fairy | `Fairy` | `fairy-test.js` |
| 9 | Sphinx | `Sphinx` | `sphinx-test.js` |
| 10 | Ogre | `Ogre`, `Human` | `ogre-test.js` |
| 11 | Direwolf | `Direwolf`, `Stark` | `direwolf-test.js` |

These slot in **after the existing 7 creatures** (Unicorn through Medusa) and are ordered by increasing complexity.

---

## Architecture & Conventions

### File Layout

Each creature gets its own folder under `creatures/`, following the established pattern:

```
creatures/
  fairy/
    __init__.py
    fairy.py
    test_fairy.py
  sphinx/
    __init__.py
    sphinx.py
    test_sphinx.py
  ogre/
    __init__.py
    ogre.py          # contains both Ogre and Human classes
    test_ogre.py
  direwolf/
    __init__.py
    direwolf.py      # contains both Direwolf and Stark classes
    test_direwolf.py
```

### Multi-Class Exercises

For exercises with companion classes (Ogre+Human, Direwolf+Stark), both classes live in the **same file**. This matches the established Medusa+Person pattern in the existing curriculum.

### Python Adaptation Rules

- **snake_case** for all method and attribute names (e.g., `starksToProtect` → `starks_to_protect`)
- **`@property`** for derived/computed state (e.g., `hunts_white_walkers`)
- **`None`** instead of `null` (e.g., `sphinx.name` defaults to `None`)
- **Type hints** on `__init__` parameters where the existing creatures use them
- **Dicts** for plain data objects (riddles, infants) — no need for dataclasses since the JS originals use plain objects

### File Boilerplate

Each file follows the existing conventions:

**`__init__.py`:**
```python
"""<Creature> - <one-line description>."""

from creatures.<creature>.<creature> import <ClassName>

__all__ = ["<ClassName>"]
```

**`<creature>.py`:**
```python
"""
<Creature> - <short description of what it introduces>.

This module teaches:
- <concept 1>
- <concept 2>
- ...

Key Design Decisions:
    <paragraph explaining architectural choices>
"""


class <ClassName>:
    pass
```

**`test_<creature>.py`:**
```python
"""
Test suite for the <Creature> class.

This exercise introduces:
- <concept 1>
- <concept 2>
- ...

Learning Objectives:
- <objective 1>
- <objective 2>
- ...
"""

import pytest

from creatures.<creature>.<creature> import <ClassName>
```

### TDD Workflow

- The **first test class** is NOT skipped (learners start there)
- All subsequent test classes have `@pytest.mark.skip(reason="Unskip this test to continue")`
- Within the first test class, the **first test method** is NOT skipped; subsequent methods ARE skipped
- Each test method has a docstring explaining what it expects

---

## Creature Specifications

### 8. Fairy

**Concepts:** Nested mutable objects (dict with list values), counter-triggered state reset, mutating argument objects in place

**Constructor:** `Fairy(name: str)`

**Attributes:**

| Attribute | Type | Default | Notes |
|-----------|------|---------|-------|
| `name` | `str` | required | |
| `dust` | `int` | `10` | |
| `clothes` | `dict` | `{"dresses": ["Iris"]}` | Mutable default — must use instance copy |
| `disposition` | `str` | `"Good natured"` | |
| `human_wards` | `list` | `[]` | Accumulated stolen infants |

**Methods:**

| Method | Behavior |
|--------|----------|
| `receive_belief()` | Adds 1 to `dust` |
| `believe()` | Adds 10 to `dust` |
| `make_dresses(flowers: list[str])` | Extends `clothes["dresses"]` with the given flower names |
| `provoke()` | Sets `disposition` to `"Vengeful"` |
| `replace_infant(infant: dict)` | If vengeful: mutates `infant["disposition"]` to `"Malicious"`, appends infant to `human_wards`. If 3 infants stolen, resets `disposition` to `"Good natured"`. If not vengeful: returns infant unchanged. |

**Data handling notes:**
- `clothes` must be initialized as a new dict per instance to avoid the mutable default argument pitfall
- `replace_infant` mutates the passed-in dict in place (teaches Python reference semantics for dicts)
- The 3-infant counter is derived from `len(human_wards) % 3 == 0` after appending, or tracked explicitly

**Test classes (6):**

1. `TestFairyCreation` — name, default dust
2. `TestFairyDust` — `receive_belief()`, `believe()`
3. `TestFairyClothes` — default clothes, `make_dresses()`, chained calls accumulate
4. `TestFairyDisposition` — starts good natured, `provoke()` → vengeful
5. `TestFairyChangelings` — `replace_infant()` mutates when vengeful, no-op when good natured
6. `TestFairyHumanWards` — stolen infants accumulate, disposition resets after 3 thefts

---

### 9. Sphinx

**Concepts:** FIFO queue (max 3, oldest dropped), find-and-remove by value, conditional return strings, string interpolation

**Constructor:** `Sphinx()` — takes no arguments

**Attributes:**

| Attribute | Type | Default | Notes |
|-----------|------|---------|-------|
| `name` | `None` | `None` | Explicitly `None`, not an empty string |
| `riddles` | `list[dict]` | `[]` | Each riddle is `{"riddle": str, "answer": str}` |
| `heroes_eaten` | `int` | `0` | |

**Methods:**

| Method | Behavior |
|--------|----------|
| `collect_riddle(riddle: dict)` | Appends riddle to `riddles`. If already at 3 riddles, drops the oldest (index 0) first, then appends. |
| `attempt_answer(answer: str) -> str` | Searches `riddles` for a dict whose `"answer"` value matches. **Correct:** removes that riddle. If riddles is now empty → return rage string. Otherwise → return `"That wasn't that hard, I bet you don't get the next one"`. **Wrong:** increments `heroes_eaten`, riddles unchanged → return `"Haha! Puny human, you look delicious"`. |

**Return strings (exact):**

| Condition | Return Value |
|-----------|-------------|
| Correct answer, riddles remain | `"That wasn't that hard, I bet you don't get the next one"` |
| Wrong answer | `"Haha! Puny human, you look delicious"` |
| Correct answer, no riddles remain | `'PSSSSSSS THIS HAS NEVER HAPPENED, HOW DID YOU KNOW THE ANSWER WAS "{answer}"???'` where `{answer}` is the answered riddle's answer value |

**Data handling notes:**
- Riddles are plain dicts, not named tuples or dataclasses
- FIFO drop: `riddles.pop(0)` when `len(riddles) >= 3` before appending
- Answer matching is order-independent — search the full list, not just the first element
- The rage string must interpolate the specific answer that was just given, using the riddle's `"answer"` field

**Test classes (5):**

1. `TestSphinxCreation` — name is `None`, riddles is `[]`
2. `TestSphinxCollecting` — `collect_riddle()`, max 3 with FIFO drop
3. `TestSphinxCorrectAnswers` — removes matching riddle, order-independent, returns mock string
4. `TestSphinxWrongAnswers` — `heroes_eaten` increments, riddles unchanged, returns laugh string
5. `TestSphinxRage` — all riddles answered correctly triggers rage string with interpolated answer

---

### 10. Ogre + Human

**Concepts:** Two cooperating classes, modulo arithmetic, chained counters, cross-object state mutation, method delegation

**Constructor — Ogre:** `Ogre(name: str, home: str = "Swamp")`

**Constructor — Human:** `Human(name: str)`

**Ogre Attributes:**

| Attribute | Type | Default | Notes |
|-----------|------|---------|-------|
| `name` | `str` | required | |
| `home` | `str` | `"Swamp"` | |
| `swings` | `int` | `0` | |

**Human Attributes:**

| Attribute | Type | Default | Notes |
|-----------|------|---------|-------|
| `name` | `str` | required | |
| `encounter_counter` | `int` | `0` | |
| `knocked_out` | `bool` | `False` | |

**Ogre Methods:**

| Method | Behavior |
|--------|----------|
| `encounter(human)` | Increments `human.encounter_counter`. If `human.notices_ogre()` is `True` after incrementing, auto-calls `swing_at(human)`. |
| `swing_at(human)` | Increments `ogre.swings`. If `swings % 2 == 0` (every 2nd swing), sets `human.knocked_out = True`. |
| `apologize(human)` | Sets `human.knocked_out = False`. |

**Human Methods:**

| Method | Behavior |
|--------|----------|
| `notices_ogre() -> bool` | Returns `True` when `encounter_counter % 3 == 0` and `encounter_counter > 0`. Otherwise `False`. |

**Chained counter logic:**
- Every 3rd encounter → human notices → ogre swings
- Every 2nd swing → ogre hits → human knocked out
- At 6 encounters: 2 swings total, 2nd swing is a hit → knocked out

**Test classes (5):**

1. `TestHumanCreation` — name, `encounter_counter` starts 0, `knocked_out` is `False`
2. `TestOgreCreation` — name, home defaults to `"Swamp"`, swings starts 0
3. `TestOgreEncounter` — `encounter()` increments counter, `notices_ogre()` true on multiples of 3
4. `TestOgreSwinging` — `swing_at()` increments swings, encounter auto-swings on notice, hit on every 2nd swing
5. `TestOgreApologize` — `apologize()` resets `knocked_out`

---

### 11. Direwolf + Stark

**Concepts:** Multi-class interaction, bidirectional state mutation, location-matching guard, array capacity cap, derived boolean property

**Constructor — Direwolf:** `Direwolf(name: str, home: str = "Beyond the Wall", size: str = "Massive")`

**Constructor — Stark:** `Stark(name: str, location: str = "Winterfell")`

**Direwolf Attributes:**

| Attribute | Type | Default | Notes |
|-----------|------|---------|-------|
| `name` | `str` | required | |
| `home` | `str` | `"Beyond the Wall"` | |
| `size` | `str` | `"Massive"` | |
| `starks_to_protect` | `list` | `[]` | Max 2 Starks |

**Stark Attributes:**

| Attribute | Type | Default | Notes |
|-----------|------|---------|-------|
| `name` | `str` | required | |
| `location` | `str` | `"Winterfell"` | |
| `safe` | `bool` | `False` | |

**Direwolf Methods:**

| Method | Behavior |
|--------|----------|
| `protect(stark)` | Adds stark to `starks_to_protect` and sets `stark.safe = True`. **Guards:** Only works if `direwolf.home == stark.location`. Silently ignores if locations don't match. Also ignores if already at capacity (2 starks). |
| `leave(stark)` | Removes stark from `starks_to_protect` and sets `stark.safe = False`. |

**Direwolf Properties:**

| Property | Behavior |
|----------|----------|
| `hunts_white_walkers` | `@property`. Returns `True` when `starks_to_protect` is empty, `False` otherwise. |

**Stark Methods:**

| Method | Behavior |
|--------|----------|
| `house_words() -> str` | Returns `"The North Remembers"` when `safe` is `True`. Returns `"Winter is Coming"` when `safe` is `False`. |

**Guard logic:**
- `protect()` checks `self.home == stark.location` before adding
- `protect()` checks `len(self.starks_to_protect) < 2` before adding
- Both guards silently no-op (no exceptions raised) — this matches the JS behavior and is intentional for the learning exercise

**Test classes (6):**

1. `TestStarkCreation` — name, location defaults to `"Winterfell"`, safe starts `False`
2. `TestStarkHouseWords` — returns different strings based on `safe` state
3. `TestDirewolfCreation` — name, home defaults, size defaults, `starks_to_protect` starts empty
4. `TestDirewolfProtect` — adds stark, sets safe, location guard, max 2 cap
5. `TestDirewolfHunting` — `hunts_white_walkers` property: `True` when empty, `False` when protecting
6. `TestDirewolfLeave` — removes stark, sets `safe` back to `False`

---

## Error Handling Strategy

These are **teaching exercises**, not production code. Error handling is intentionally minimal:

- **No exceptions raised** for invalid input. Guards silently no-op (e.g., protecting a Stark in the wrong location, adding a 3rd Stark, answering a riddle when none exist).
- **No input validation** on types. Tests always pass correct types — the focus is OOP concepts, not defensive programming.
- **Mutable default arguments** are the one "gotcha" learners must handle correctly. The stub docstrings should hint at this for `Fairy.clothes` and all list-type attributes.

---

## Testing Plan

### Framework

- **pytest** with `@pytest.mark.skip` decorators (existing project standard)
- Tests run via: `pytest creatures/<creature>/test_<creature>.py`

### Test Progression Per Creature

| Step | Action |
|------|--------|
| 1 | First test in first class runs immediately (no skip) |
| 2 | All other tests decorated with `@pytest.mark.skip(reason="Unskip this test to continue")` |
| 3 | Learner removes one `@pytest.mark.skip` at a time |
| 4 | Red → implement → green → refactor → unskip next |

### Test Count Summary

| Creature | Test Classes | Approx Test Methods |
|----------|-------------|-------------------|
| Fairy | 6 | 13 |
| Sphinx | 5 | 13 |
| Ogre | 5 | 12 |
| Direwolf | 6 | 15 |
| **Total** | **22** | **~53** |

### Validation

After implementation, all tests should pass when all skips are removed:

```bash
# Run individual creature
pytest creatures/fairy/test_fairy.py
pytest creatures/sphinx/test_sphinx.py
pytest creatures/ogre/test_ogre.py
pytest creatures/direwolf/test_direwolf.py

# Run full suite
pytest
```

### Test Style Guidelines (matching existing tests)

- Each test method has a docstring explaining expected behavior
- Tests use `assert` statements (no unittest-style `self.assertEqual`)
- Tests are grouped by concept into `Test*` classes
- Test methods named `test_<behavior_under_test>`
- Prefer explicit values over loops in tests (readability for learners)

---

## Implementation Order

Build in this order to match curriculum progression:

1. **Fairy** — single class, gentlest introduction of the four
2. **Sphinx** — single class, data-structure focused
3. **Ogre + Human** — two classes, chained counters
4. **Direwolf + Stark** — two classes, most complex multi-class interaction

For each creature, implement in this order:
1. Create the folder structure (`__init__.py`, stub `.py`, test file)
2. Write the complete test file with all skips in place
3. Write the stub implementation file (classes with `pass`)
4. Verify: first test passes, all others skip

---

## README Updates

Add the four new creatures to the `## The Creatures` section of `README.md`:

```markdown
### 8. Fairy

**Concepts:** Nested mutable objects, counter-triggered state transitions, mutating dict arguments

The Fairy teaches nested data manipulation and state machines. You'll learn to manage
dicts-within-dicts, accumulate state across method calls, and handle counter-triggered
transitions.

### 9. Sphinx

**Concepts:** FIFO queues, find-and-remove patterns, conditional return values, string interpolation

The Sphinx is data-structure focused. You'll implement a sliding window queue (max 3),
search-and-remove logic, and conditional return strings with interpolated values.

### 10. Ogre

**Concepts:** Two cooperating classes, modulo arithmetic, chained counters, cross-object mutation

The Ogre introduces chained counter logic across two classes. Every 3rd encounter triggers
a swing, every 2nd swing triggers a knockout. Tracking independent counters is the key challenge.

### 11. Direwolf

**Concepts:** Bidirectional state mutation, location-matching guards, capacity constraints, derived properties

The Direwolf is the capstone exercise. Two classes with guard clauses, capacity limits,
and bidirectional state changes build on everything learned in previous exercises.
```
