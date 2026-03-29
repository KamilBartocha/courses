# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About This Repository

A Polish-language Python fundamentals course. Content is delivered via Jupyter notebooks, with supporting Python scripts for live coding. Part of the larger `KamilBartocha/courses` repo.

## Running Code

```bash
# Open a notebook
jupyter notebook 01_python_instalacja_i_srodowiska/01_python_instalacja.ipynb

# Run a Python script directly
python3 02_python_skladnia_i_typy_proste/02_cheat_sheet.py
```

No package manager or requirements file — all examples use the Python standard library only.

## Module Structure

Eight modules (01–08), each containing three file types:
- `NN_cheat_sheet.py` — quick-reference code snippets
- `NN_exercise.py` — exercise starter code or solutions
- `NN_live_coding.py` — blank file used during live class sessions
- `NN_*.ipynb` — main Jupyter notebook with theory, examples, and exercises

Module topics: 01 Installation & IDE → 02 Syntax & Simple Types → 03 Collections & Control Flow → 04 Functions → 05 Files & Modules → 06 Exceptions → 07 Functional Programming → 08 OOP

Supporting reference: `syllabus-python-basics.md` (Polish-language concept summary per module).

## Notebook Conventions (from `notebook-rules.md`)

When editing or refactoring notebooks, follow these rules:

**Language & naming**
- Theory/prose cells: Polish, academic "we" voice (`wywołujemy`, `definiujemy`, not `wywołujesz`)
- Code: English variable/function names (`list1`, `cubes`, `text` — not `lista1`, `szesciany`, `tekst`)
- Technical terms: Polish first, English in brackets — e.g. `klasa (class)`, `dziedziczenie (inheritance)`
- Text line length: max 79 characters
- Use `-` (hyphen), not `—` (em dash)

**Cell structure per section**
```
## N. 🔹 Section name
Theory cells (Polish prose)
Example cells (runnable English code)
---
### 🐍 Ćwiczenia — topic
Exercise descriptions (one markdown cell)
One code cell per exercise
```

**Exercise templates**
- Use `...` as the placeholder for student solutions
- Always end with `print()` so output is visible
- Add `# hint:` comments for harder exercises
- Difficulty ramp: easy → medium → hard (mark hard with `*(Trudniejsze)*`)
- Minimum 3 exercises per section

**Notebook metadata**
- Title cell: single `#` header with version (`2.0`) and author name
- Add agenda (Rozkład jazdy) cell after the title — one line per section with emoji
- Version number: update to `2.0` after significant revisions
