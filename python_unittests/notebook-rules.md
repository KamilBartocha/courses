# Notebook Authoring Rules — Python Unit Tests

## Instructions — apply to any Python unit tests notebook

### 1. Language rules
- Theory/prose cells: Polish, academic "we" voice (`wywołujemy`, `definiujemy`, `tworzymy`)
- Code: English variable names and string literals (`user_data`, `"alice"` — not `dane_uzytkownika`, `"ala"`)
- Technical terms: Polish first, English in brackets — `test jednostkowy (unit test)`, `atrapa (mock)`
- Max 79 characters per text line; use `-` (hyphen), not `—` (em dash)

### 2. Cell structure per section (strictly this order)
```
## N. 🔹 Section name
Theory cells (Polish prose)
Example code cell (English names)
---
### 🐍 Ćwiczenia — topic
One markdown cell listing all exercises
One code cell per exercise
```

### 3. Exercise cell format
- Input data and variable names pre-defined; `...` as the placeholder for student solution
- Always ends with a `print()` or assertion so output is visible
- `# hint:` comments on harder exercises; mark them with `*(Trudniejsze)*`
- Minimum 3 exercises per section, difficulty ramping easy → medium → hard
- For test exercises: provide the class/function under test in the cell,
  student writes the test methods

### 4. Notebook metadata
- Title cell: single `#` header with module number, course name, topic, version (`2.0`), and author
- Second cell: `Rozkład jazdy` agenda — one emoji-prefixed line per section
- Update version number after significant revisions

### 5. Code under test (CUT) conventions
- Functions/classes being tested are defined at the top of the notebook cell
  or imported from a companion `src_<topic>.py` file in the same directory
- Keep CUT simple and focused — exercises test the testing skill, not domain logic
- Example CUT names: `BankAccount`, `Calculator`, `UserService`, `EmailValidator`

### 6. Test naming convention
- Test methods: `test_<what>_<condition>_<expected>` (e.g. `test_withdraw_insufficient_funds_raises`)
- Test classes: `Test<ClassUnderTest>` (e.g. `TestBankAccount`)

### 7. Sections should cover: Why → How → When
- Explain *why* a feature exists before showing *how* to use it
- End each section with a *when to use* summary or comparison table
