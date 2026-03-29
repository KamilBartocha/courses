# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Polish-language Python education repository by Kamil Bartocha. Three progressive courses, each in its own subdirectory with its own `CLAUDE.md`:

| Directory | Course | Scope |
|---|---|---|
| `python_basics/` | Python fundamentals | 8 modules (01–08), standard library only |
| `python_intermediate/` | Advanced Python | 17 modules (100–116), 186 exercises |
| `test_automation_basics/` | Test automation | 5 modules, pytest + Selenium |

Each subdirectory `CLAUDE.md` contains the authoritative module map, run commands, and topic reference for that course.

## Shared Notebook Conventions

All 45+ Jupyter notebooks across the three courses follow the same authoring standard (documented per-course in `notebook-rules.md`):

**Language rules**
- Theory/prose cells: Polish, academic "we" voice (`wywołujemy`, `definiujemy`, `tworzymy`)
- Code: English variable names and string literals (`list1`, `"alice"` — not `lista1`, `"ala"`)
- Technical terms: Polish first, English in brackets — `klasa (class)`, `dziedziczenie (inheritance)`
- Max 79 characters per text line; use `-` (hyphen), not `—` (em dash)

**Cell structure per section (strictly this order)**
```
## N. 🔹 Section name
Theory cells (Polish prose)
Example code cell (English names)
---
### 🐍 Ćwiczenia — topic
One markdown cell listing all exercises
One code cell per exercise
```

**Exercise cell format**
- Input data and variable names pre-defined; `...` as the placeholder for student solution
- Always ends with `print()` so output is visible
- `# hint:` comments on harder exercises; mark them with `*(Trudniejsze)*`
- Minimum 3 exercises per section, difficulty ramping easy → medium → hard

**Notebook metadata**
- Title cell: single `#` header with module number, course name, topic, version (`2.0`), and author
- Second cell: `Rozkład jazdy` agenda — one emoji-prefixed line per section
- Update version number after significant revisions
