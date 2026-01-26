# Mythical Python

A Test-Driven Development (TDD) curriculum for learning Python Object-Oriented Programming through mythical creatures.

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd mythical-python
```

### 2. Set Up Your Environment

Create and activate a virtual environment:

https://stevekinney.com/writing/setup-python

### 3. Install Dependencies

```bash
pip install -e ".[dev]"
```

### 4. Verify Your Setup

Run the test suite to make sure everything is working:

```bash
pytest creatures/unicorn/test_unicorn.py
```

You should see **1 test passing** and several tests skipped. This means you're ready to begin!

## How This Works

This curriculum uses **Test-Driven Development** (TDD). The tests are already written for you - your job is to make them pass by implementing the creature classes.

### The TDD Cycle

1. **Run the tests** - See which test is failing
2. **Read the test** - Understand what the test expects
3. **Write code** - Implement just enough to make the test pass
4. **Refactor** - Clean up your code if needed
5. **Repeat** - Unskip the next test and continue

### Working Through the Exercises

Each creature has a test file (`test_*.py`) and an implementation file (`*.py`).

1. Start with the **Unicorn** - it's the first creature and introduces basic concepts
2. Run the tests: `pytest creatures/unicorn/test_unicorn.py`
3. The first test runs automatically; subsequent tests are skipped
4. Make the first test pass by editing `creatures/unicorn/unicorn.py`
5. When a test passes, **unskip the next test** by removing its `@pytest.mark.skip` decorator
6. Continue until all Unicorn tests pass
7. Move on to the next creature

### Running Tests

Run tests for a specific creature:

```bash
pytest creatures/unicorn/test_unicorn.py
pytest creatures/dragon/test_dragon.py
```

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

## The Creatures

Work through these creatures **in order**. Each one builds on concepts from the previous exercises.

### 1. Unicorn

**Concepts:** Classes, `__init__`, instance attributes, default parameters, type hints, boolean methods, f-strings

The Unicorn introduces the fundamentals of Python classes. You'll learn how to create objects with required and optional attributes, and write simple methods.

### 2. Dragon

**Concepts:** State accumulation, counters, `@property` decorator, computed/derived state, encapsulation

The Dragon teaches you about tracking state over time. You'll learn how to use the `@property` decorator to compute values dynamically rather than storing them.

### 3. Vampire

**Concepts:** Mutable state, internal state initialization, state mutation through methods

The Vampire demonstrates how objects can change over time. You'll learn the difference between constructor arguments and internal state.

### 4. Hobbit

**Concepts:** Lifecycle modeling, boundary conditions, age-based state transitions, `@property` for lifecycle states

The Hobbit teaches lifecycle modeling with age-based transitions. Pay close attention to boundary conditions - this is a critical TDD skill!

### 5. Pirate

**Concepts:** State flags, accumulators, threshold-triggered state, multiple independent state mechanisms

The Pirate introduces the difference between computed state (like Dragon's hunger) and triggered state (once cursed, always cursed).

### 6. Wizard

**Concepts:** Boolean default parameters, string transformation, resource management

The Wizard emphasizes string manipulation and boolean arguments in constructors.

### 7. Medusa

**Concepts:** Object interaction, one-to-many relationships, state mutation across objects, FIFO queues, object references

Medusa represents a major complexity jump. You'll work with two classes that interact, managing collections of objects and understanding Python's reference semantics.

## Tips for Success

- **Read the test file first** - The docstrings explain what each test expects
- **Read the module docstring** - Each creature file has hints about the concepts involved
- **Make one test pass at a time** - Don't try to implement everything at once
- **Pay attention to boundary conditions** - Test edge cases carefully
- **Use `pytest -v`** - Verbose output helps you understand what's happening

## Running with Coverage

To see how much of your code is covered by tests:

```bash
pytest --cov=creatures
```

## Getting Help

If you're stuck:

1. Re-read the failing test carefully
2. Check the test's docstring for hints
3. Look at the module docstring in the creature file
4. Review concepts from previous creatures

Happy coding!
