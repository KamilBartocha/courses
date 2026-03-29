# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Python intermediate course (version 2.0, author Kamil Bartocha). 17 Jupyter notebook modules (100–116) covering advanced Python topics, each paired with a solutions `.py` file. 186 exercises across 67 sections total. Course instructions are in Polish; all code must be in English.

## Running and Testing

Run a Jupyter notebook:
```bash
jupyter notebook <module_dir>/<notebook>.ipynb
```

Run the datareader library tests (module 105):
```bash
cd 105_python_interm_modules/105_library/datareader
python -m pytest tests/
# or run a single test file
python -m unittest tests/test_json_reader.py
```

Run a solution file directly:
```bash
python3 <module_dir>/<NNN>_python_interm_solutions.py
```

## Module Structure

Each module folder (`NNN_python_interm_<topic>/`) contains:
- `NNN_python_interm_<topic>.ipynb` — main teaching notebook
- `NNN_python_interm_solutions.py` — complete exercise solutions

Exception: module 105 also contains `105_library/datareader/` — a full installable Python package with `setup.py`, `__init__.py`, and pytest tests.

## Notebook Authoring Standards

These rules are documented in `NOTEBOOK_REFACTORING_PLAYBOOK.md` and must be followed when creating or editing notebooks:

**Structure per section (strictly in this order):**
```
Title cell (single # header, author, version)
Rozkład jazdy (agenda cell)
---
## N. 🔹 Section name
Theory cells (Polish prose, max 79 chars/line)
Example code cell (English variable names and strings)
---
### ✏️ Ćwiczenia — topic
One markdown cell listing all exercises
One code cell per exercise
```

**Exercise code cell format:**
- Starter code with input data and variable names already defined
- `...` as the placeholder for student solution
- Always end with a `print()` statement
- Add `# hint:` for harder problems
- Mark harder exercises with `*(Trudniejsze)*`

**Language rules:**
- Theory: Polish, academic "we" voice (`wywołujemy`, `definiujemy`, `tworzymy`)
- Code: English variable names and string literals (e.g. `list1`, `"alice"`, not `lista1`, `"ala"`)
- Technical terms: Polish first, English in brackets — `klasa (class)`, `dziedziczenie (inheritance)`
- Use `-` (hyphen), not `—` (em dash)

**Versioning:** update the version number in the title cell after significant revisions.

## Module Topics Reference

| Module | Topic |
|--------|-------|
| 100 | Basics review (prerequisites) |
| 101 | OOP: inheritance, encapsulation, dunder methods, class/static methods |
| 102 | Lambda, map, filter, list/dict/set comprehensions |
| 103 | `*args` and `**kwargs` |
| 104 | Virtual environments, requirements.txt, debugger |
| 105 | Custom modules, packages, `setup.py`, pytest |
| 106 | JSON serialization and file I/O |
| 107 | Exception handling, custom exceptions |
| 108 | Decorators, `@dataclass` |
| 109 | Context managers, `__enter__`/`__exit__`, `@contextmanager` |
| 110 | Metaclasses, `type()` |
| 111 | Abstract Base Classes, `@abstractmethod` |
| 112 | Generators, iterators, `itertools` |
| 113 | `functools`: `partial`, `lru_cache`, `reduce` |
| 114 | `collections`: Counter, defaultdict, deque, namedtuple; `enum` |
| 115 | Type annotations, `typing` module |
| 116 | Pydantic: `BaseModel`, `Field`, validators |

Prerequisites for all modules are documented in `BASIC_CONCEPTS.md`. Full exercise list per module is in `SYLLABUS.md`.
