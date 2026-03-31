# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

## Repository Purpose

Python unit testing course (version 2.0, author Kamil Bartocha).
13 Jupyter notebook modules (00-12) introducing testing tools progressively,
each paired with a solutions `.py` file.
131 exercises across 42 sections total.

**Prerequisites:** `python_basics` and `python_intermediate` courses.

## Running and Testing

Run a Jupyter notebook:
```bash
jupyter notebook <module_dir>/<notebook>.ipynb
```

Run tests from a module's source file:
```bash
cd <module_dir>/
python -m pytest tests/ -v
# or for unittest
python -m unittest discover -v
```

Run a solution file directly:
```bash
python3 <module_dir>/<NN>_python_unittest_solutions.py
```

## Module Structure

Each module folder (`NN_python_unittest_<topic>/`) contains:
- `NN_python_unittest_<topic>.ipynb` — main teaching notebook
- `NN_python_unittest_solutions.py` — complete exercise solutions
- `src_<topic>.py` (optional) — code under test used in exercises

## Notebook Authoring Standards

Rules documented in `notebook-rules.md`. Summary:

**Structure per section (strictly in this order):**
```
Title cell (single # header, author, version 2.0)
Rozkład jazdy (agenda cell)
---
## N. 🔹 Section name
Theory cells (Polish prose, max 79 chars/line)
Example code cell (English names)
---
### 🐍 Ćwiczenia — topic
One markdown cell listing all exercises
One code cell per exercise
```

**Exercise code cell format:**
- Code Under Test (CUT) defined at top of cell or imported from `src_*.py`
- Student writes test methods; `...` as placeholder
- Always include at least one assertion or `print()` showing test result
- Mark harder exercises with `*(Trudniejsze)*`, add `# hint:` comments
- Test naming: `test_<what>_<condition>_<expected>`

**Language rules:**
- Theory: Polish, academic "we" voice (`wywołujemy`, `definiujemy`, `tworzymy`)
- Code: English names (`bank_account`, `user_service`, not `konto`, `serwis`)
- Terms: Polish first, English in brackets — `atrapa (mock)`, `pokrycie (coverage)`
- Hyphens `-` only, no em dashes `—`

## Module Topics Reference

| Module | Topic | Tools |
|--------|-------|-------|
| 00 | Wstep do testowania - piramida, AAA, TDD | - |
| 01 | `unittest` - TestCase, assert*, test discovery | `unittest` |
| 02 | `unittest` - setUp/tearDown, skip, subTest | `unittest` |
| 03 | `pytest` - funkcje testowe, assert, CLI | `pytest` |
| 04 | `pytest` - fixtures, scope, conftest.py, tmp_path | `pytest` |
| 05 | `pytest` - parametrize, markery, xfail | `pytest` |
| 06 | `unittest.mock` - Mock, MagicMock, patch | `unittest.mock` |
| 07 | `unittest.mock` - call, AsyncMock, patch.dict | `unittest.mock` |
| 08 | `pytest-mock` - mocker fixture, spy, stub | `pytest-mock` |
| 09 | Pokrycie kodu - line/branch, raporty | `coverage`, `pytest-cov` |
| 10 | Generowanie danych - Faker, providery, seed | `faker` |
| 11 | Property-based testing - @given, strategie | `hypothesis` |
| 12 | TDD i dobre praktyki - CI/CD, tox, wzorce | `tox`, `nox` |

Full exercise list is in `syllabus-python-unittests.md`.

## Dependencies

```bash
pip install pytest pytest-mock pytest-timeout coverage pytest-cov faker hypothesis tox nox
```

Or install from `requirements.txt` (to be created per module as needed).
