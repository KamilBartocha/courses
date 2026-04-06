# Project Rules

Rules for creating `project_NN_nazwa/` projects in the python_basics course.

## File structure

```
project_NN_nazwa/
    nazwa_task.py       <- student file (functions stubbed with pass)
    nazwa_solution.py   <- complete reference solution
    data_file           <- input data if needed (e.g. app.log)
```

## Task file conventions

### Header comment
```python
# nazwa_task.py - Project NN: Krotki opis
#
# Kontekst biznesowy (2-4 linijki, po polsku).
# Co dostaje student i co ma zrobic.
#
# Uruchomienie: python3 nazwa_task.py
```

### Input data
- Defined at module level, before any functions.
- Use Polish names for entities (clients, products), English for variable names (`orders`, `fields`, `transaction`).

### Task sections — one function per section
```python
# ─── Zadanie N ─ Krotki opis zadania ─────────────────────────────────────────
def function_name(args):
    """English-language docstring.

    One paragraph explaining what the function does.

    Args:
        arg1: Description.
        arg2: Description.

    Returns:
        Description of the return value.

    Example:
        function_name(input) -> expected_output

    Hint: short hint for harder tasks.
    """
    pass
```

### Entry point
```python
# Uruchomienie
result = main_function(data)
```
or
```python
# ─── Uruchomienie ─────────────────────────────────────────────────────────────
result = main_function(data)
```

## Docstring rules

- Language: English.
- Structure order: description, blank line, Args, blank line, Returns, blank line, Example (if useful), blank line, Hint (if needed).
- Example block shows a concrete call and its expected return value.
- Hint only on tasks where the approach is non-obvious (e.g. key= argument, `.get()`, `.zfill()`).
- `print_report` / `print_summary` functions use "Expected output format:" instead of "Returns:" and show the exact output with real values.

## Section separator style

```python
# ─── Zadanie N ─ Opis ────────────────────────────────────────────────────────
```
- Use `─` (U+2500) for the horizontal lines.
- Total line length: 79 characters.
- For the entry point block: `# ─── Uruchomienie ───...`

## Number and scope of tasks

- Each project has at least 5 tasks (Zadanie 1-5).
- Last task is always the report/summary function that orchestrates tasks.
- Difficulty ramps: data loading / simple transform → aggregation → sorting/ranking → formatted output.

## Language rules

- Header comment and section labels: Polish.
- Function names, variable names, string literals in code: English.
- Docstrings: English.
- Polish names/words only in input data (client names, product names, report labels in expected output).
