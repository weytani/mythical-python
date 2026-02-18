# Mythical Python — TDD Implementation Plan

## Context

This plan adds four new creature exercises (Fairy, Sphinx, Ogre+Human, Direwolf+Stark) to an existing Python TDD curriculum. The product is **test files and stubs** — learners write the implementations. We write a reference implementation for each creature to verify our tests are correct, then strip it back to stubs before shipping.

**Spec:** `spec.md`

**Key conventions observed from existing creatures:**
- Creatures after Unicorn use **class-level** `@pytest.mark.skip(reason="Complete Unicorn first, then unskip this test")` — all tests within an unskipped class run together
- Stub files have a module docstring + `class Foo: pass`
- `__init__.py` has a one-line docstring, import, and `__all__`
- Tests use `assert` (not `self.assertEqual`), each method has a docstring
- Multi-class exercises (Medusa+Person) put both classes in one file

---

## Phases

| Phase | Creature | Prompts | Deliverables |
|-------|----------|---------|-------------|
| 0 | Setup | 1 | Folder scaffolds for all 4 creatures |
| 1 | Fairy | 3 | Tests (13), stub, verified reference impl |
| 2 | Sphinx | 3 | Tests (13), stub, verified reference impl |
| 3 | Ogre + Human | 3 | Tests (12), stub, verified reference impl |
| 4 | Direwolf + Stark | 3 | Tests (15), stub, verified reference impl |
| 5 | Integration | 1 | README update, stubs reset, full suite green |
| **Total** | | **14** | **~53 tests across 4 creatures** |

---

## Phase 0: Project Setup

### Prompt 0 — Scaffold All Creature Folders

```text
You are working in the mythical-python TDD curriculum project at /Users/weytani/code/mythical-python.

This project teaches Python OOP through mythical creature exercises. There are 7 existing
creatures under creatures/. Each creature has its own folder with three files:
- __init__.py (one-line docstring, import, __all__)
- <creature>.py (module docstring, class stub with pass)
- test_<creature>.py (test suite)

Create the folder scaffolds for 4 new creatures. Do NOT write tests yet — just the
folders, __init__.py, and stub .py files.

1. creatures/fairy/
   - __init__.py: docstring "Fairy - Nested state and counter-triggered transitions."
     Import Fairy from creatures.fairy.fairy. __all__ = ["Fairy"]
   - fairy.py: Module docstring explaining it teaches nested mutable objects (dict with
     list values), counter-triggered state reset, and mutating argument objects in place.
     Key design decision: clothes must be initialized per-instance to avoid mutable
     default pitfall. Stub: class Fairy: pass

2. creatures/sphinx/
   - __init__.py: docstring "Sphinx - FIFO queues and conditional return values."
     Import Sphinx from creatures.sphinx.sphinx. __all__ = ["Sphinx"]
   - sphinx.py: Module docstring explaining it teaches FIFO queue (max 3, oldest dropped),
     find-and-remove by value, conditional return strings, and string interpolation.
     Key design decision: riddles are plain dicts, sliding window uses pop(0) before
     append. Stub: class Sphinx: pass

3. creatures/ogre/
   - __init__.py: docstring "Ogre - Chained counters across cooperating classes."
     Import Ogre, Human from creatures.ogre.ogre. __all__ = ["Ogre", "Human"]
   - ogre.py: Module docstring explaining it teaches two cooperating classes, modulo
     arithmetic, chained counters, and cross-object state mutation. Key design decision:
     both classes in one file matching the Medusa+Person pattern. encounter() delegates
     to swing_at() based on human.notices_ogre(). Stubs: class Human: pass and
     class Ogre: pass

4. creatures/direwolf/
   - __init__.py: docstring "Direwolf - Bidirectional state and location-matching guards."
     Import Direwolf, Stark from creatures.direwolf.direwolf. __all__ = ["Direwolf", "Stark"]
   - direwolf.py: Module docstring explaining it teaches multi-class interaction,
     bidirectional state mutation, location-matching guards, capacity constraints, and
     @property for derived state. Key design decision: both classes in one file, protect()
     uses two silent guards (location match + capacity), hunts_white_walkers is a
     @property. Stubs: class Stark: pass and class Direwolf: pass

After creating all files, verify the scaffolds:
- Run: pytest --collect-only creatures/fairy/ creatures/sphinx/ creatures/ogre/ creatures/direwolf/
- Confirm pytest discovers the folders (even though no tests exist yet)
- Run: python -c "from creatures.fairy import Fairy; from creatures.sphinx import Sphinx; from creatures.ogre import Ogre, Human; from creatures.direwolf import Direwolf, Stark; print('All imports OK')"

All files must start with a 2-line ABOUTME comment before the docstring.
```

---

## Phase 1: Fairy

### Prompt 1 — Fairy Tests: Creation & Dust

```text
You are working in /Users/weytani/code/mythical-python, a Python TDD curriculum.

Read these files first to understand the exact conventions:
- creatures/unicorn/test_unicorn.py (skip pattern for the first creature)
- creatures/dragon/test_dragon.py (skip pattern for later creatures)
- creatures/medusa/test_medusa.py (multi-class skip pattern)
- spec.md (section "8. Fairy" for full attribute/method specs)

Now create creatures/fairy/test_fairy.py with the first two test classes. Follow the
Dragon/Medusa pattern: ALL test classes get @pytest.mark.skip at the class level with
reason="Complete Medusa first, then unskip this test". No individual method-level skips.

Module docstring should explain:
- This exercise introduces nested mutable objects, counter-triggered state transitions,
  and mutating dict arguments
- Learning objectives: manage dicts-within-dicts, accumulate state, handle
  counter-triggered transitions, understand mutable default argument pitfall

Import: from creatures.fairy.fairy import Fairy

Test class 1 — TestFairyCreation (2 tests):
- test_fairy_has_a_name: Fairy("Holly"), assert name == "Holly"
- test_fairy_has_default_dust: Fairy("Mab"), assert dust == 10

Test class 2 — TestFairyDust (2 tests):
- test_fairy_gets_dust_from_others_belief: Create Fairy("Sookie"), capture dust before,
  call receive_belief(), verify dust increased by exactly 1
- test_fairy_gets_more_dust_from_believing_in_herself: Create Fairy("Tinkerbell"),
  capture dust before, call believe(), verify dust increased by exactly 10

After writing:
- Run: pytest creatures/fairy/test_fairy.py --collect-only
- Verify pytest discovers 2 test classes and 4 test methods, all marked as skipped

Start the file with a 2-line ABOUTME comment.
```

### Prompt 2 — Fairy Tests: Clothes, Disposition, Changelings & Wards

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/fairy/test_fairy.py to see what exists. Read spec.md section "8. Fairy"
for full method specs and exact behaviors.

Add four more test classes to test_fairy.py. All get @pytest.mark.skip at the class level
with reason="Complete Medusa first, then unskip this test".

Test class 3 — TestFairyClothes (3 tests):
- test_fairy_starts_with_iris_dress: Fairy("Rose"), assert clothes == {"dresses": ["Iris"]}
- test_fairy_turns_flowers_into_dresses: Fairy("Honeysuckle"), call
  make_dresses(["Daffodil", "Tulip", "Poppy"]), assert clothes["dresses"] ==
  ["Iris", "Daffodil", "Tulip", "Poppy"]
- test_fairy_accumulates_dresses_across_calls: Fairy("Cosmo Pepperfeet"), call
  make_dresses(["Ranunculus", "Daisy"]) then make_dresses(["Hydrangea", "Forget-me-not"]),
  assert clothes["dresses"] == ["Iris", "Ranunculus", "Daisy", "Hydrangea", "Forget-me-not"]

Test class 4 — TestFairyDisposition (2 tests):
- test_fairy_starts_good_natured: Fairy("Cologne"), assert disposition == "Good natured"
- test_fairy_becomes_vengeful_when_provoked: Fairy("Aine"), call provoke(),
  assert disposition == "Vengeful"

Test class 5 — TestFairyChangelings (2 tests):
- test_fairy_replaces_infant_disposition_when_vengeful: Fairy("Claudine"), two infant
  dicts with name/eyes/disposition keys. Call provoke(), then replace_infant() on each.
  Assert each infant's disposition is now "Malicious" (eyes and name unchanged).
- test_fairy_does_not_replace_infant_when_good_natured: Fairy("Marceline"), one infant
  dict. Call replace_infant() WITHOUT provoking first. Assert infant is returned unchanged
  (same object reference).

Test class 6 — TestFairyHumanWards (2 tests):
- test_fairy_raises_stolen_infants: Fairy("Winnie"), provoke, replace two infants.
  Assert human_wards == [first_infant, second_infant].
- test_fairy_calms_down_after_three_stolen_infants: Fairy("Basil"), provoke, replace
  three infants. Assert disposition == "Good natured" after the third.

After writing:
- Run: pytest creatures/fairy/test_fairy.py --collect-only
- Verify 6 test classes, 11 test methods total, all skipped
```

### Prompt 3 — Fairy Reference Implementation & Verification

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/fairy/test_fairy.py to see all 6 test classes and 11 tests.
Read creatures/fairy/fairy.py to see the current stub.
Read spec.md section "8. Fairy" for the complete attribute and method specifications.

Write a complete reference implementation of the Fairy class in creatures/fairy/fairy.py.
Keep the existing module docstring. Replace `class Fairy: pass` with the full
implementation.

Requirements:
- __init__(self, name: str) with all default attributes per spec
- clothes MUST be initialized as a new dict per instance (avoid mutable default pitfall)
- human_wards MUST be initialized as a new list per instance
- receive_belief(): adds 1 to dust
- believe(): adds 10 to dust
- make_dresses(flowers: list[str]): extends clothes["dresses"]
- provoke(): sets disposition to "Vengeful"
- replace_infant(infant: dict): if vengeful, mutate infant["disposition"] to "Malicious",
  append to human_wards, check if len(human_wards) % 3 == 0 and reset disposition.
  If not vengeful, return infant unchanged. Always return the infant.

Verification — run these commands and confirm:
1. Remove all @pytest.mark.skip decorators from test_fairy.py temporarily
2. Run: pytest creatures/fairy/test_fairy.py -v
3. ALL 11 tests must pass
4. Restore all @pytest.mark.skip decorators to test_fairy.py
5. Run: pytest creatures/fairy/test_fairy.py -v
6. All 11 tests must show as skipped

IMPORTANT: After verification, RESET fairy.py back to the stub (class Fairy: pass)
with the module docstring preserved. The reference implementation is only for validation.

Start fairy.py with a 2-line ABOUTME comment.
```

---

## Phase 2: Sphinx

### Prompt 4 — Sphinx Tests: Creation & Collecting

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/dragon/test_dragon.py and creatures/medusa/test_medusa.py for test
conventions. Read spec.md section "9. Sphinx" for full specs.

Create creatures/sphinx/test_sphinx.py with the first two test classes. Follow the same
pattern: class-level @pytest.mark.skip(reason="Complete Medusa first, then unskip this test").

Module docstring: introduces FIFO queues, find-and-remove patterns, conditional return
values, and string interpolation. Learning objectives: implement sliding window queue,
search-and-remove logic, conditional returns with interpolation.

Import: from creatures.sphinx.sphinx import Sphinx

Test class 1 — TestSphinxCreation (2 tests):
- test_sphinx_has_no_name: Sphinx(), assert name is None
- test_sphinx_starts_with_no_riddles: Sphinx(), assert riddles == []

Test class 2 — TestSphinxCollecting (2 tests):
- test_sphinx_collects_riddles: Create Sphinx, create riddle dict
  {"riddle": "What word becomes shorter when you add two letters to it?", "answer": "short"}.
  Call collect_riddle(riddle). Assert riddles == [riddle].
- test_sphinx_collects_only_three_riddles: Create Sphinx, create 4 riddle dicts.
  Collect all 4. Assert riddles contains only the last 3 (FIFO — first dropped).
  Use these exact riddles from the JS source:
    riddle1: "What word becomes shorter..." / "short"
    riddle2: "How far can a fox run into a grove?" / "Halfway, after that it's running out."
    riddle3: "What starts with an 'e' and ends with an 'e' and contains one letter?" / "An envelope"
    riddle4: "What's been around for millions of years but is never more than a month old?" / "The moon"

After writing:
- Run: pytest creatures/sphinx/test_sphinx.py --collect-only
- Verify 2 test classes, 4 test methods, all skipped

Start the file with a 2-line ABOUTME comment.
```

### Prompt 5 — Sphinx Tests: Answers, Eating & Rage

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/sphinx/test_sphinx.py to see what exists. Read spec.md section "9. Sphinx"
for exact return strings and behaviors.

Add three more test classes. All get class-level @pytest.mark.skip with same reason.

Test class 3 — TestSphinxCorrectAnswers (3 tests):
- test_sphinx_accepts_correct_answer_and_removes_riddle: Collect 1 riddle, attempt its
  answer. Assert riddles == [].
- test_sphinx_accepts_answers_in_any_order: Collect 3 riddles, attempt the THIRD one's
  answer ("An envelope"). Assert riddles == [riddle1, riddle2] (third removed).
- test_sphinx_mocks_heroes_on_correct_answer: Collect 2 riddles, attempt first answer.
  Assert return value is exactly: "That wasn't that hard, I bet you don't get the next one"

Test class 4 — TestSphinxWrongAnswers (3 tests):
- test_sphinx_starts_having_eaten_no_heroes: Sphinx(), assert heroes_eaten == 0
- test_sphinx_eats_hero_on_wrong_answer: Collect 3 riddles, attempt wrong answer "e".
  Assert riddles unchanged (still all 3), heroes_eaten == 1.
- test_sphinx_does_not_eat_hero_on_correct_answer: Collect 3 riddles, attempt "short".
  Assert riddles == [riddle2, riddle3], heroes_eaten == 0.

Test class 5 — TestSphinxRage (3 tests):
- test_sphinx_laughs_on_wrong_answer: Collect 1 riddle, attempt wrong answer "e".
  Assert return == "Haha! Puny human, you look delicious"
- test_sphinx_screams_when_all_riddles_answered: Collect 2 riddles, answer both
  correctly in order. Assert final return ==
  'PSSSSSSS THIS HAS NEVER HAPPENED, HOW DID YOU KNOW THE ANSWER WAS "Halfway, after that it\'s running out."???'
- test_sphinx_rage_references_last_answered_riddle: Collect 2 riddles, answer them in
  REVERSE order (riddle2 first, then riddle1). Assert final return ==
  'PSSSSSSS THIS HAS NEVER HAPPENED, HOW DID YOU KNOW THE ANSWER WAS "short"???'

After writing:
- Run: pytest creatures/sphinx/test_sphinx.py --collect-only
- Verify 5 test classes, 13 test methods total, all skipped
```

### Prompt 6 — Sphinx Reference Implementation & Verification

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/sphinx/test_sphinx.py for all 5 test classes.
Read creatures/sphinx/sphinx.py for the stub.
Read spec.md section "9. Sphinx" for complete specs.

Write a complete reference implementation of the Sphinx class in creatures/sphinx/sphinx.py.

Requirements:
- __init__(self) with name=None, riddles=[], heroes_eaten=0
- riddles MUST be initialized as a new list per instance
- collect_riddle(riddle: dict): if len >= 3, pop(0) first, then append
- attempt_answer(answer: str) -> str:
  - Search riddles for dict where ["answer"] == answer
  - If found: remove it. If riddles now empty, return rage string with the answered
    riddle's answer interpolated. Otherwise return mock string.
  - If not found: increment heroes_eaten, return laugh string.
- Exact return strings per spec.md

Verification:
1. Remove all @pytest.mark.skip from test_sphinx.py temporarily
2. Run: pytest creatures/sphinx/test_sphinx.py -v
3. ALL 13 tests must pass
4. Restore all @pytest.mark.skip decorators
5. Run: pytest creatures/sphinx/test_sphinx.py -v — all skipped
6. RESET sphinx.py back to stub (class Sphinx: pass) with docstring preserved

Start sphinx.py with a 2-line ABOUTME comment.
```

---

## Phase 3: Ogre + Human

### Prompt 7 — Ogre Tests: Human & Ogre Creation

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/medusa/test_medusa.py for multi-class test conventions (how Person and
Medusa tests are organized). Read spec.md section "10. Ogre + Human" for full specs.

Create creatures/ogre/test_ogre.py with the first two test classes. Class-level
@pytest.mark.skip(reason="Complete Medusa first, then unskip this test").

Module docstring: introduces two cooperating classes with chained modulo counters.
Learning objectives: understand modulo arithmetic for periodic events, track independent
counters across objects, implement method delegation (encounter calls swing_at).

Import: from creatures.ogre.ogre import Ogre, Human

Test class 1 — TestHumanCreation (3 tests):
- test_human_has_a_name: Human("Jane"), assert name == "Jane"
- test_human_starts_with_zero_encounters: Human("Jane"), assert encounter_counter == 0
- test_human_starts_not_knocked_out: Human("Jane"), assert knocked_out is False

Test class 2 — TestOgreCreation (3 tests):
- test_ogre_has_a_name: Ogre("Brak"), assert name == "Brak"
- test_ogre_lives_in_swamp_by_default: Ogre("Brak"), assert home == "Swamp"
- test_ogre_can_live_elsewhere: Ogre("Brak", "The Ritz"), assert home == "The Ritz"

After writing:
- Run: pytest creatures/ogre/test_ogre.py --collect-only
- Verify 2 test classes, 6 test methods, all skipped

Start the file with a 2-line ABOUTME comment.
```

### Prompt 8 — Ogre Tests: Encounters, Swinging & Apology

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/ogre/test_ogre.py to see what exists. Read spec.md section "10. Ogre + Human"
for exact chained counter logic.

Add three more test classes with class-level skips.

Test class 3 — TestOgreEncounter (3 tests):
- test_ogre_encounter_increments_human_counter: Ogre("Brak"), Human("Jane").
  Call encounter(human). Assert human.encounter_counter == 1.
- test_human_notices_ogre_every_third_encounter: Ogre("Brak"), Human("Jane").
  encounter twice — assert notices_ogre() is False.
  encounter a third time — assert notices_ogre() is True.
- test_human_notices_on_sixth_encounter: Ogre("Brak"), Human("Jane").
  Assert notices_ogre() is False initially.
  3 encounters — notices is True.
  2 more encounters (5 total) — notices is False.
  1 more encounter (6 total) — notices is True.

Test class 4 — TestOgreSwinging (4 tests):
- test_ogre_can_swing_club: Ogre("Brak"), Human("Jane"). Call swing_at(human).
  Assert swings == 1.
- test_ogre_starts_with_zero_swings: Ogre("Brak"). Assert swings == 0.
- test_ogre_swings_when_human_notices: Ogre("Brak"), Human("Jane").
  1 encounter — assert swings == 0.
  2 more encounters (3 total) — human notices, assert swings == 1.
- test_ogre_hits_human_every_second_swing: Ogre("Brak"), Human("Jane").
  6 encounters total. Assert encounter_counter == 6, swings == 2,
  knocked_out is True.

Test class 5 — TestOgreApologize (1 test):
- test_human_wakes_up_when_ogre_apologizes: Ogre("Brak"), Human("Jane").
  Call apologize(human). Assert knocked_out is False.

After writing:
- Run: pytest creatures/ogre/test_ogre.py --collect-only
- Verify 5 test classes, 14 test methods total, all skipped
```

### Prompt 9 — Ogre Reference Implementation & Verification

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/ogre/test_ogre.py for all 5 test classes.
Read creatures/ogre/ogre.py for the stub.
Read spec.md section "10. Ogre + Human" for complete specs.

Write complete reference implementations for BOTH Human and Ogre classes in
creatures/ogre/ogre.py.

Human requirements:
- __init__(self, name: str): name, encounter_counter=0, knocked_out=False
- notices_ogre(self) -> bool: True when encounter_counter % 3 == 0 and counter > 0

Ogre requirements:
- __init__(self, name: str, home: str = "Swamp"): name, home, swings=0
- encounter(self, human): increment human.encounter_counter, then if
  human.notices_ogre() is True, call self.swing_at(human)
- swing_at(self, human): increment self.swings, then if swings % 2 == 0,
  set human.knocked_out = True
- apologize(self, human): set human.knocked_out = False

Verification:
1. Remove all @pytest.mark.skip from test_ogre.py temporarily
2. Run: pytest creatures/ogre/test_ogre.py -v
3. ALL 14 tests must pass
4. Restore all @pytest.mark.skip decorators
5. RESET ogre.py back to stubs (class Human: pass, class Ogre: pass) with docstring

Start ogre.py with a 2-line ABOUTME comment.
```

---

## Phase 4: Direwolf + Stark

### Prompt 10 — Direwolf Tests: Stark & Direwolf Creation

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/medusa/test_medusa.py for multi-class test layout.
Read spec.md section "11. Direwolf + Stark" for full specs.

Create creatures/direwolf/test_direwolf.py with the first three test classes. Class-level
@pytest.mark.skip(reason="Complete Medusa first, then unskip this test").

Module docstring: capstone exercise introducing bidirectional state mutation,
location-matching guards, capacity constraints, and @property for derived state.
Learning objectives: manage guard clauses that silently no-op, implement bidirectional
state changes across objects, use @property for derived boolean state.

Import: from creatures.direwolf.direwolf import Direwolf, Stark

Test class 1 — TestStarkCreation (3 tests):
- test_stark_has_a_name: Stark("Bran"), assert name == "Bran"
- test_stark_defaults_to_winterfell: Stark("Bran"), assert location == "Winterfell"
- test_stark_starts_unsafe: Stark("John", "Winterfell"), assert safe is False

Test class 2 — TestStarkHouseWords (2 tests):
- test_stark_says_winter_is_coming_when_unsafe: Stark("John", "Winterfell"),
  assert house_words() == "Winter is Coming"
- test_stark_says_north_remembers_when_safe: Stark("Arya", "Dorn"). Create
  Direwolf("Nymeria", "Dorn"). Protect stark. Assert house_words() == "The North Remembers".
  (This test crosses into Direwolf but is testing Stark's method.)

Test class 3 — TestDirewolfCreation (4 tests):
- test_direwolf_has_a_name: Direwolf("Nymeria"), assert name == "Nymeria"
- test_direwolf_defaults_to_beyond_the_wall: Direwolf("Lady"),
  assert home == "Beyond the Wall"
- test_direwolf_defaults_to_massive: Direwolf("Ghost"), assert size == "Massive"
- test_direwolf_can_have_custom_home_and_size: Direwolf("Shaggydog", "Karhold", "Smol Pupper"),
  assert name/home/size match

After writing:
- Run: pytest creatures/direwolf/test_direwolf.py --collect-only
- Verify 3 test classes, 9 test methods, all skipped

Start the file with a 2-line ABOUTME comment.
```

### Prompt 11 — Direwolf Tests: Protect, Hunting & Leave

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/direwolf/test_direwolf.py to see what exists. Read spec.md section
"11. Direwolf + Stark" for exact guard logic and behaviors.

Add three more test classes with class-level skips.

Test class 4 — TestDirewolfProtect (4 tests):
- test_direwolf_starts_with_no_starks: Direwolf("Nymeria"), Stark("Arya").
  Assert starks_to_protect == [].
- test_direwolf_protects_stark_at_same_location: Direwolf("Nymeria", "Riverlands"),
  Stark("Arya", "Riverlands"). Protect. Assert len(starks_to_protect) == 1,
  starks_to_protect[0].name == "Arya".
- test_direwolf_only_protects_if_locations_match: Direwolf("Ghost") (default: Beyond the Wall),
  Stark("John", "King's Landing"). Protect. Assert starks_to_protect == [].
- test_direwolf_protects_max_two_starks: Two direwolves at Winterfell. 5 Starks at
  Winterfell. Protect: direwolf1 gets 2, direwolf2 gets 2 (5th rejected).
  Assert direwolf1 has ["Sansa", "John"], direwolf2 has ["Rob", "Bran"].

Test class 5 — TestDirewolfHunting (2 tests):
- test_direwolf_hunts_when_not_protecting: Direwolf("Nymeria", "Winterfell"),
  Stark("Sansa"). Assert hunts_white_walkers is True before protect.
- test_direwolf_stops_hunting_when_protecting: Same setup. Protect stark.
  Assert hunts_white_walkers is False.

Test class 6 — TestDirewolfLeave (2 tests):
- test_direwolf_can_leave_stark: Direwolf("Summer", "Winterfell"),
  Direwolf("Lady", "Winterfell"), Stark("Sansa"), Stark("Arya").
  direwolf1 protects Arya (safe=True). direwolf2 protects Sansa.
  direwolf1 leaves Arya. Assert direwolf1.starks_to_protect == [],
  direwolf2 still has Sansa, Arya.safe is False.
- test_stark_becomes_unsafe_when_direwolf_leaves: Direwolf("Nymeria", "Dorn"),
  Stark("Arya", "Dorn"). Protect, assert safe True. Leave, assert safe False.

After writing:
- Run: pytest creatures/direwolf/test_direwolf.py --collect-only
- Verify 6 test classes, 17 test methods total, all skipped
```

### Prompt 12 — Direwolf Reference Implementation & Verification

```text
You are working in /Users/weytani/code/mythical-python.

Read creatures/direwolf/test_direwolf.py for all 6 test classes.
Read creatures/direwolf/direwolf.py for the stub.
Read spec.md section "11. Direwolf + Stark" for complete specs.

Write complete reference implementations for BOTH Stark and Direwolf in
creatures/direwolf/direwolf.py.

Stark requirements:
- __init__(self, name: str, location: str = "Winterfell"): name, location, safe=False
- house_words(self) -> str: "The North Remembers" if safe, "Winter is Coming" if not

Direwolf requirements:
- __init__(self, name: str, home: str = "Beyond the Wall", size: str = "Massive"):
  name, home, size, starks_to_protect=[] (new list per instance)
- protect(self, stark): Guard 1: self.home == stark.location. Guard 2:
  len(starks_to_protect) < 2. If both pass: append stark, set stark.safe = True.
  Otherwise silently do nothing.
- leave(self, stark): Remove stark from starks_to_protect, set stark.safe = False.
- @property hunts_white_walkers: return len(self.starks_to_protect) == 0

Verification:
1. Remove all @pytest.mark.skip from test_direwolf.py temporarily
2. Run: pytest creatures/direwolf/test_direwolf.py -v
3. ALL 17 tests must pass
4. Restore all @pytest.mark.skip decorators
5. RESET direwolf.py back to stubs (class Stark: pass, class Direwolf: pass) with docstring

Start direwolf.py with a 2-line ABOUTME comment.
```

---

## Phase 5: Integration

### Prompt 13 — README, Final Verification & Cleanup

```text
You are working in /Users/weytani/code/mythical-python.

Three tasks remain:

TASK 1: Update README.md
Read README.md. Add the four new creatures to the "## The Creatures" section, after
the existing "### 7. Medusa" entry. Use the exact descriptions from spec.md section
"README Updates". Number them 8-11.

TASK 2: Verify all stubs are clean
Confirm each creature's implementation file contains ONLY the module docstring and
stub class(es) with pass:
- creatures/fairy/fairy.py: class Fairy: pass
- creatures/sphinx/sphinx.py: class Sphinx: pass
- creatures/ogre/ogre.py: class Human: pass, class Ogre: pass
- creatures/direwolf/direwolf.py: class Stark: pass, class Direwolf: pass

TASK 3: Full suite verification
Run: pytest --collect-only
Verify:
- All existing creature tests still collected
- All 4 new creature test files collected
- New creature tests show as skipped (class-level skips)
- No import errors, no collection errors

Run: pytest creatures/fairy/ creatures/sphinx/ creatures/ogre/ creatures/direwolf/ -v
Verify all new tests are reported as SKIPPED.

Run: pytest (full suite) to confirm nothing is broken.

Report the final count: total tests discovered, total skipped, total passing.
```

---

## Verification Checklist

After all prompts are complete:

- [ ] 4 new creature folders exist under creatures/
- [ ] Each folder has __init__.py, <creature>.py (stub), test_<creature>.py
- [ ] All test files have proper module docstrings with learning objectives
- [ ] All test classes have class-level @pytest.mark.skip
- [ ] All implementation files are stubs (class with pass)
- [ ] All imports work: `python -c "from creatures.fairy import Fairy"` etc.
- [ ] pytest --collect-only shows all new tests as skipped
- [ ] Full pytest run passes (existing tests + new skipped tests)
- [ ] README.md updated with creatures 8-11
- [ ] All files start with 2-line ABOUTME comment
