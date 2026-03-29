# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Educational course repository for test automation with Python, organized as 5 progressive modules: intro, Python basics, API/Postman, pytest, and Selenium.

## Running Tests

```bash
# Run all tests in a directory
pytest 04_pytest_automation/test_calculator/

# Run a single test file
pytest 05_selenium_automation/solution/interia_login/login_refactoredv4/test_interia_login.py

# Run with verbose output
pytest -v test_file.py

# Run tests by marker
pytest -m login
pytest -m "not login"
```

The `login_refactoredv4/` module has its own `pytest.ini` defining the `login` marker — run pytest from that directory or specify the ini path when working there.

## Key Dependencies

- `pytest` — test framework
- `selenium` — browser automation (uses Safari webdriver on macOS)
- `requests` — HTTP API testing
- `python-dotenv` — loads credentials from `.env`

No `requirements.txt` exists at the repo root; dependencies are expected to be installed in the active environment.

## Architecture

The course follows a deliberate refactoring progression in `05_selenium_automation/solution/interia_login/`:

| File | Pattern introduced |
|---|---|
| `test_login.py` | Inline Selenium, hard-coded creds, `sleep()` |
| `test_login_refactoredv1.py` | Extract login to reusable function |
| `test_login_refactoredv2.py` | `setup`/`teardown`, `implicitly_wait()`, try/except |
| `test_login_refactoredv3.py` | pytest fixtures, `WebDriverWait`/`EC`, `.env` creds |
| `login_refactoredv4/` | Page Object Model, `conftest.py` with screenshot-on-failure |

**Page Object Model** (v4): locators defined as `(By.X, "value")` tuples on the page class; each UI interaction is a separate method; tests only call high-level page methods.

**conftest.py** in v4 hooks `pytest_runtest_makereport` to save a timestamped screenshot to `screenshots/` on test failure.

## Credentials

Tests against interia.pl require a `.env` file (gitignored) with:
```
INTERIA_EMAIL=...
INTERIA_PASSWORD=...
```

Some earlier refactoring files contain hard-coded credentials — this is intentional for pedagogical comparison, not a pattern to replicate.

## Module Layout

```
01_wstep_do_automatyzacji/   # Intro slides/PDF
02_python/                   # Python basics notebooks + exercises
03_api_postman_automation/   # Postman collections + API notebook
04_pytest_automation/        # pytest examples: calculator, fixtures, requests, full API project
05_selenium_automation/      # Selenium examples + progressive refactoring solutions
```
