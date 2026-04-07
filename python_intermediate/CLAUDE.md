# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Python intermediate course (version 2.0, author Kamil Bartocha). 20 Jupyter notebook modules (00–19) covering advanced Python topics, each paired with a solutions `.py` file. 236 exercises across 76 sections total. Course instructions are in Polish; all code must be in English.

## Running and Testing

Run a Jupyter notebook:
```bash
jupyter notebook <module_dir>/<notebook>.ipynb
```

Run the datareader library tests (module 05):
```bash
cd 05_python_interm_modules/05_library/datareader
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

Exception: module 05 also contains `05_library/datareader/` — a full installable Python package with `setup.py`, `__init__.py`, and pytest tests.

## Notebook Authoring Standards

These rules are documented in `notebook-rules.md` and must be followed when creating or editing notebooks:

**Structure per section (strictly in this order):**
```
Title cell (single # header, author, version)
Rozkład jazdy (agenda cell)
---
## N. 🔹 Section name
Theory cells (Polish prose, max 79 chars/line)
Example code cell (English variable names and strings)
---
### 🐍 Ćwiczenia — topic
One markdown cell listing all exercises
One code cell per exercise
```

**Exercise code cell format:**
- Starter code with input data and variable names already defined
- `...` as the placeholder for student solution
- Always end with a `print()` statement
- Add `# hint:` for harder problems
- Mark harder exercises with `*(Trudniejsze)*`
- If a section introduces N distinct concepts/methods, provide at least N exercises
  so every introduced concept is covered by at least one exercise

**Language rules:**
- Theory: Polish, academic "we" voice (`wywołujemy`, `definiujemy`, `tworzymy`)
- Code: English variable names and string literals (e.g. `list1`, `"alice"`, not `lista1`, `"ala"`)
- Technical terms: Polish first, English in brackets — `klasa (class)`, `dziedziczenie (inheritance)`
- Use `-` (hyphen), not `—` (em dash)

**Versioning:** update the version number in the title cell after significant revisions.

## Module Topics Reference

| Module | Topic |
|--------|-------|
| 00 | Basics review (prerequisites) |
| 01 | OOP: inheritance, encapsulation, dunder methods, class/static methods |
| 02 | Lambda, map, filter, list/dict/set comprehensions |
| 03 | `*args` and `**kwargs` |
| 04 | Virtual environments, requirements.txt, debugger |
| 05 | Custom modules, packages, `setup.py`, pytest |
| 06 | JSON serialization and file I/O |
| 07 | Exception handling, custom exceptions |
| 08 | Decorators, `@dataclass` |
| 09 | Context managers, `__enter__`/`__exit__`, `@contextmanager` |
| 10 | Metaclasses, `type()` |
| 11 | Abstract Base Classes, `@abstractmethod` |
| 12 | Generators, iterators, `itertools` |
| 13 | `functools`: `partial`, `lru_cache`, `reduce` |
| 14 | `collections`: Counter, defaultdict, deque, namedtuple, OrderedDict; `enum` |
| 15 | Type annotations, `typing` module (Python 3.9+) |
| 16 | Pydantic: `BaseModel`, `Field`, validators, `BaseSettings` |
| 17 | `pathlib`: `Path`, file I/O, `glob`/`rglob` |
| 18 | `logging`: levels, handlers, formatters, logger hierarchy |
| 19 | `dataclasses`: `field()`, `__post_init__`, `ClassVar`, `InitVar`, `frozen` |

Prerequisites for all modules are documented in `syllabus-python-basics.md`. Full exercise list per module is in `syllabus-python-intermediate.md`.
