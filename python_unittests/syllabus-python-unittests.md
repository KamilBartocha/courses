# Python Unit Tests — Syllabus

Kurs obejmuje 13 modułów (notebooks 00-12).
Łącznie **131 ćwiczeń** w **42 sekcjach** tematycznych.

**Wymagania wstępne:** kurs `python_basics` i `python_intermediate`
(OOP, wyjątki, dekoratory, kontekst managery, `dataclasses`).

**Narzędzia omawiane w kursie** (w kolejności wprowadzania):
`unittest` → `pytest` → `unittest.mock` / `pytest-mock`
→ `coverage` / `pytest-cov` → `faker` → `hypothesis`

---

## Moduł 00 — Wstęp do testowania

**Plik:** `00_unittest_intro/00_unittest_intro.ipynb`

Czym jest test jednostkowy i dlaczego warto pisać testy.
Rodzaje testów (jednostkowe, integracyjne, e2e) i ich miejsce
w piramidzie testów. Wzorzec AAA (Arrange-Act-Assert).
Wprowadzenie do TDD (Red-Green-Refactor).

### Sekcje
1. 🔹 Piramida testów i rodzaje testów
2. 🔹 Wzorzec AAA (Arrange-Act-Assert)
3. 🔹 TDD - cykl Red-Green-Refactor

### Ćwiczenia (9)
1. Przeczytaj kod i zidentyfikuj bloki Arrange/Act/Assert
2. Napisz pierwszy test manualny dla funkcji `is_palindrome()`
3. *(Trudniejsze)* Wypisz liste przypadków testowych dla `divide(a, b)`
4. Zidentyfikuj co testuje test jednostkowy, a co integracyjny w przykładach
5. Dla klasy `BankAccount` wypisz minimum 5 przypadków testowych
6. *(Trudniejsze)* Napisz pseudokod TDD dla funkcji `validate_email()`
7. Odróznij SUT (System Under Test) od DOC (Depended-On Component) w przykładzie
8. Sklasyfikuj testy z listy jako unit/integration/e2e
9. *(Trudniejsze)* Zaprojektuj strategie testów dla modułu `ShoppingCart`

---

## Moduł 01 — `unittest` - podstawy

**Plik:** `01_unittest_basics/01_unittest_basics.ipynb`

Wbudowany moduł `unittest`. Klasa `TestCase`, metody `assert*`,
uruchamianie testów przez `unittest.main()` i `python -m unittest`.
Odkrywanie testów (test discovery).

### Sekcje
1. 🔹 `TestCase` i metody `assert*`
2. 🔹 Uruchamianie i odkrywanie testów
3. 🔹 Testowanie wyjątków i komunikatów

### Ćwiczenia (12)
1. Klasa `TestCalculator` - testy dla `add`, `subtract`, `multiply`
2. Uzyj `assertEqual`, `assertNotEqual`, `assertTrue`, `assertFalse`
3. *(Trudniejsze)* Testy dla `divide` z testowaniem `ZeroDivisionError`
4. Uruchom testy przez `unittest.main()` i `python -m unittest discover`
5. Napisz testy dla klasy `Stack` (push, pop, is_empty, peek)
6. Uzyj `assertRaises` jako context manager i jako wywołanie
7. *(Trudniejsze)* Testy dla `BankAccount.withdraw` - walidacja, wyjątek, saldo
8. Uzyj `assertIn`, `assertIsNone`, `assertIsInstance`
9. Napisz testy dla `EmailValidator.is_valid()`
10. Uzyj `assertAlmostEqual` dla obliczeń zmiennoprzecinkowych
11. *(Trudniejsze)* Testy dla `StringProcessor` - edge cases (pusty string, None, unicode)
12. *(Trudniejsze)* Napisz `TestSuite` łączący dwie klasy testowe

---

## Moduł 02 — `unittest` - zaawansowane

**Plik:** `02_unittest_advanced/02_unittest_advanced.ipynb`

`setUp`/`tearDown` i `setUpClass`/`tearDownClass`. Pomijanie testów
(`@skip`, `@skipIf`, `@skipUnless`). `@expectedFailure`. `subTest`
do parametryzacji. Organizacja testów w zestawy (test suites).

### Sekcje
1. 🔹 `setUp` / `tearDown` i cykl zycia testu
2. 🔹 `@skip`, `@skipIf`, `@expectedFailure`
3. 🔹 `subTest` - parametryzacja w unittest

### Ćwiczenia (9)
1. Uzyj `setUp` by tworzyc swiezy obiekt `BankAccount` przed kazda metoda
2. Uzyj `setUpClass` do operacji kosztownych (np. tworzenie pliku)
3. *(Trudniejsze)* `setUp`/`tearDown` z plikiem tymczasowym (`tempfile`)
4. Pomiń test dla Pythona < 3.10 przez `@skipIf(sys.version_info < (3, 10), ...)`
5. Oznacz test jako `@expectedFailure` i sprawdź zachowanie
6. *(Trudniejsze)* Uzyj `subTest` by przetestowac `is_valid_age()` dla 10 wartości
7. Napisz `subTest` dla listy par wejście/oczekiwany wynik dla `slugify()`
8. Połącz dwie klasy testowe w `TestSuite` i uruchom razem
9. *(Trudniejsze)* Napisz base test case z `setUp` i odziedzicz po nim dwa zestawy

---

## Moduł 03 — `pytest` - podstawy

**Plik:** `03_pytest_basics/03_pytest_basics.ipynb`

Instalacja i filozofia `pytest`. Pisanie testów jako zwykłe funkcje.
Asercje przez `assert`. Odkrywanie testów, uruchamianie, flagi CLI.
Czytelne komunikaty błędów. Porównanie z `unittest`.

**Instalacja:** `pip install pytest`

### Sekcje
1. 🔹 Filozofia pytest - prostota i czytelność
2. 🔹 Asercje i komunikaty błędów
3. 🔹 Uruchamianie i konfiguracja (`pytest.ini`, `pyproject.toml`)

### Ćwiczenia (12)
1. Przetłumacz testy z modułu 01 z `unittest` na `pytest`
2. Napisz testy dla `fizzbuzz(n)` jako czyste funkcje pytest
3. *(Trudniejsze)* Testy dla `parse_date(text)` - poprawne i błędne formaty
4. Uzyj `pytest -v`, `-k "nazwa"`, `--tb=short` w terminalu
5. Napisz testy dla `Temperature` z modułu 19 intermediate
6. *(Trudniejsze)* Przetestuj wyjątek przez `pytest.raises` jako context manager
7. Sprawdź komunikat wyjątku przez `excinfo.value`
8. Napisz testy dla `UserValidator` sprawdzajac edge cases
9. Uzyj `pytest.approx` dla wartości zmiennoprzecinkowych
10. Porownaj czytelność: ten sam test w `unittest` vs `pytest`
11. *(Trudniejsze)* Testy dla klasy `ShoppingCart` (add, remove, total, discount)
12. *(Trudniejsze)* Skonfiguruj `pytest.ini` z `testpaths` i `addopts`

---

## Moduł 04 — `pytest` - fixtures

**Plik:** `04_pytest_fixtures/04_pytest_fixtures.ipynb`

Fixtures jako mechanizm dependency injection w pytest.
Scope: `function`, `class`, `module`, `session`.
`conftest.py`. Yield fixtures do teardown. Fixtures wbudowane
(`tmp_path`, `capsys`, `monkeypatch`).

**Instalacja:** `pip install pytest`

### Sekcje
1. 🔹 Fixtures - definicja i wstrzykiwanie zależności
2. 🔹 Scope i cykl zycia (`function`, `class`, `module`, `session`)
3. 🔹 Yield fixtures i `conftest.py`
4. 🔹 Wbudowane fixtures (`tmp_path`, `capsys`, `monkeypatch`)

### Ćwiczenia (12)
1. Napisz fixture `bank_account` zwracajacy swiezy obiekt `BankAccount`
2. Uzyj tej samej fixture w trzech testach
3. *(Trudniejsze)* Fixture z `scope='module'` dla połączenia z SQLite (`:memory:`)
4. Napisz fixture `populated_cart` zaleząca od fixture `empty_cart`
5. Uzyj `yield` w fixture do sprzatania pliku tymczasowego
6. *(Trudniejsze)* Fixture z parametrami - ten sam test dla dwóch implementacji
7. Uzyj `tmp_path` do testowania zapisu/odczytu pliku
8. Uzyj `capsys` do testowania funkcji piszacych na stdout
9. Uzyj `monkeypatch` do podstawienia zmiennej środowiskowej
10. *(Trudniejsze)* Uzyj `monkeypatch` do podmiany metody obiektu
11. Przenieś fixture do `conftest.py` i sprawdź ze działa z innego pliku
12. *(Trudniejsze)* Fixture fabryczna (`fixture` zwracajaca funkcję factory)

---

## Moduł 05 — `pytest` - parametryzacja i markery

**Plik:** `05_pytest_parametrize/05_pytest_parametrize.ipynb`

`@pytest.mark.parametrize` do testowania wielu przypadków.
Markery wbudowane: `@pytest.mark.skip`, `@pytest.mark.xfail`,
`@pytest.mark.slow`. Własne markery i filtrowanie przez `-m`.
Plugin `pytest-timeout`.

**Instalacja:** `pip install pytest pytest-timeout`

### Sekcje
1. 🔹 `@pytest.mark.parametrize` - wiele przypadków testowych
2. 🔹 Markery wbudowane: `skip`, `xfail`, `skipif`
3. 🔹 Własne markery i filtrowanie testów

### Ćwiczenia (9)
1. Przetestuj `is_even(n)` dla 8 wartości z `@parametrize`
2. Parametryzuj test wyjątku - różne błędne wejscia dla `parse_int()`
3. *(Trudniejsze)* Parametryzuj z `pytest.param(..., marks=pytest.mark.xfail)`
4. Pomiń test przez `@pytest.mark.skip(reason=...)`
5. Oznacz test jako `@pytest.mark.xfail(strict=True)`
6. *(Trudniejsze)* Zdefiniuj własny marker `@pytest.mark.slow` i uruchom testy z `-m "not slow"`
7. Parametryzuj fixture (parametrized fixture) dla testów na dwóch środowiskach
8. Zagnieżdź dwa `@parametrize` (iloczyn kartezjański przypadków)
9. *(Trudniejsze)* Parametryzuj test klasy `Matrix` dla operacji `add`, `multiply`, `transpose`

---

## Moduł 06 — `unittest.mock` - podstawy

**Plik:** `06_mock_basics/06_mock_basics.ipynb`

Czym jest atrapa (mock/stub/spy/fake). Moduł `unittest.mock`:
`Mock`, `MagicMock`, `patch` jako dekorator i context manager.
`return_value`, `side_effect`. Weryfikacja wywołań: `assert_called_*`.

**Moduł standardowy:** `unittest.mock` (brak instalacji)

### Sekcje
1. 🔹 Rodzaje atrap - Mock, Stub, Spy, Fake
2. 🔹 `Mock` i `MagicMock` - tworzenie i konfiguracja
3. 🔹 `patch` - podmiana obiektów w testach

### Ćwiczenia (12)
1. Utwórz `Mock()` i sprawdź `return_value`, `called`, `call_count`
2. Skonfiguruj `side_effect` jako wyjątek i jako listę wartości
3. *(Trudniejsze)* `MagicMock` dla klasy z `__len__` i `__iter__`
4. Uzyj `@patch('module.ClassName')` do podmany w dekoratorze
5. Uzyj `patch()` jako context manager
6. *(Trudniejsze)* Patch `requests.get` w tescie funkcji pobierajacej dane z API
7. Sprawdź `assert_called_once_with`, `assert_called_with`
8. Uzyj `call_args_list` do weryfikacji wielu wywołań
9. *(Trudniejsze)* Patch wbudowanej funkcji `open` przez `mock_open`
10. Mock dla metody klasy - `patch.object`
11. Uzyj `spec=` by mock respektował interfejs oryginału
12. *(Trudniejsze)* Przetestuj klasę `EmailSender` mockując SMTP

---

## Moduł 07 — `unittest.mock` - zaawansowane

**Plik:** `07_mock_advanced/07_mock_advanced.ipynb`

`patch.multiple`, `patch.dict`. `AsyncMock` dla kodu asynchronicznego.
`MagicMock` vs `NonCallableMock`. Weryfikacja kolejności wywołań
przez `call`. Wzorzec spy (szpieg). `sentinel`.

**Moduł standardowy:** `unittest.mock`

### Sekcje
1. 🔹 `call`, `call_args`, kolejność wywołań
2. 🔹 `patch.dict`, `patch.multiple`, `sentinel`
3. 🔹 `AsyncMock` i testowanie kodu asynchronicznego

### Ćwiczenia (9)
1. Uzyj `mock.call_args` i `mock.call_args_list` do inspekcji argumentów
2. Porównaj wywołania przez `assert_has_calls([call(1), call(2)])`
3. *(Trudniejsze)* Sprawdź kolejność wywołań dwóch różnych mocków przez `manager`
4. Podmień klucze w słowniku przez `patch.dict`
5. Uzyj `sentinel` jako unikalny obiekt wartowniczy
6. *(Trudniejsze)* Napisz wzorzec spy - opakuj prawdziwy obiekt, loguj wywołania
7. Przetestuj `async def fetch_user(id)` przez `AsyncMock`
8. Przetestuj `async def process_batch(items)` mockując wewnetrzny `await`
9. *(Trudniejsze)* Przetestuj serwis zaleząy od dwóch mockowanych klientów API

---

## Moduł 08 — `pytest-mock`

**Plik:** `08_pytest_mock/08_pytest_mock.ipynb`

Plugin `pytest-mock` jako lzejszy interfejs do `unittest.mock`.
Fixture `mocker`. `mocker.patch`, `mocker.spy`, `mocker.stub`.
Automatyczne czyszczenie po teście. Porównanie z `patch` dekoratorem.

**Instalacja:** `pip install pytest-mock`

### Sekcje
1. 🔹 Fixture `mocker` - prostszy interfejs do patch
2. 🔹 `mocker.spy` - szpiegowanie prawdziwych metod
3. 🔹 Kiedy `pytest-mock`, a kiedy `unittest.mock`

### Ćwiczenia (9)
1. Zamień `@patch(...)` dekorator na `mocker.patch(...)` w istniejacych testach
2. Uzyj `mocker.patch.object` do podmiany metody instancji
3. *(Trudniejsze)* Przetestuj `NotificationService` mockując trzy zależności przez `mocker`
4. Uzyj `mocker.spy(obj, 'method')` i sprawdź `call_count` prawdziwej metody
5. Porównaj: ten sam test przez dekorator `@patch` vs `mocker.patch`
6. *(Trudniejsze)* Fixture wielokrotnego uzytku opakowujaca `mocker.patch`
7. Uzyj `mocker.stub()` jako uproszczonego mocka bez spec
8. Sprawdź ze mock jest automatycznie czyszczony miedzy testami
9. *(Trudniejsze)* Przetestuj `PaymentService` z mockowanym `BankClient` i `AuditLogger`

---

## Moduł 09 — Pokrycie kodu (`coverage` / `pytest-cov`)

**Plik:** `09_coverage/09_coverage.ipynb`

Metryki pokrycia: line coverage, branch coverage. Narzędzie
`coverage.py`. Raport HTML, XML, terminal. Plugin `pytest-cov`.
`.coveragerc` konfiguracja. Co warto, a czego nie warto pokrywać.

**Instalacja:** `pip install coverage pytest-cov`

### Sekcje
1. 🔹 Metryki pokrycia kodu - line vs branch
2. 🔹 `coverage.py` i `pytest-cov` - uruchamianie i raporty
3. 🔹 Konfiguracja i dobre praktyki pokrycia

### Ćwiczenia (9)
1. Uruchom `coverage run -m pytest` i `coverage report -m`
2. Wygeneruj raport HTML i zidentyfikuj niepokryte linie
3. *(Trudniejsze)* Włącz `branch=True` i znajdź niepokryte gałęzie
4. Uruchom pytest z `--cov=src --cov-report=term-missing`
5. Dodaj `# pragma: no cover` do kodu który nie wymaga testów
6. *(Trudniejsze)* Skonfiguruj `.coveragerc` z `omit`, `include`, progiem minimalnym
7. Napisz testy zwiększające pokrycie od 60% do 90% dla gotowej klasy
8. Zinterpretuj raport: skad wynika roznica miedzy line a branch coverage
9. *(Trudniejsze)* Skonfiguruj `--cov-fail-under=85` i podłącz do CI (plik `Makefile`)

---

## Moduł 10 — `faker` - generowanie danych testowych

**Plik:** `10_faker/10_faker.ipynb`

Biblioteka `faker` do generowania realistycznych danych testowych.
Providery: `name`, `address`, `internet`, `date_time`, `company`.
Seed dla reprodukowalności. Locale. Własny provider.

**Instalacja:** `pip install faker`

### Sekcje
1. 🔹 Faker - podstawy i providery
2. 🔹 Seed i reprodukowalność testów
3. 🔹 Własny provider i integracja z pytest

### Ćwiczenia (9)
1. Wygeneruj 5 uzytkowników z `name`, `email`, `address`
2. Uzyj providera `date_time` do generowania dat w przedziale
3. *(Trudniejsze)* Napisz fixture pytest `fake_user` zwracajacą słownik z danymi
4. Ustaw `Faker.seed(42)` i sprawdź reprodukowalność danych
5. Uzyj lokalnego Fakera `Faker('pl_PL')` dla polskich danych
6. *(Trudniejsze)* Napisz własny provider `CompanyProvider` z metodą `nip()` (PL)
7. Wygeneruj listę 100 zamówień i przetestuj funkcje analizujące zamówienia
8. Uzyj `faker` razem z `@pytest.mark.parametrize` przez `faker.profile()`
9. *(Trudniejsze)* Fixture sesyjna zwracajaca bank 500 losowych uzytkowników

---

## Moduł 11 — `hypothesis` - property-based testing

**Plik:** `11_hypothesis/11_hypothesis.ipynb`

Testowanie własności (property-based testing) jako komplement
testów przykładowych. Biblioteka `hypothesis`: dekorator `@given`,
strategie (`integers`, `text`, `lists`, `composite`). `assume()`.
Shrinking (minimalizacja kontrprzykładu).

**Instalacja:** `pip install hypothesis`

### Sekcje
1. 🔹 Property-based testing - filozofia i zalety
2. 🔹 `@given` i strategie (`st.integers`, `st.text`, `st.lists`)
3. 🔹 `assume`, `composite` i strategie złożone

### Ćwiczenia (12)
1. Napisz property test dla `sorted(list)` - wynik jest posortowany
2. Sprawdź własność `reverse(reverse(lst)) == lst`
3. *(Trudniejsze)* Sprawdź własność przemienności `add(a, b) == add(b, a)`
4. Uzyj `st.integers(min_value=1)` i `assume(b != 0)` dla `divide(a, b)`
5. Testuj `encode/decode` - round-trip dla `base64`
6. *(Trudniejsze)* Własna strategia `st.composite` dla klasy `User`
7. Sprawdź własność idempotentności `strip(strip(s)) == strip(s)`
8. Testuj funkcję sortowania przez własność `len(sorted) == len(original)`
9. Uzyj `@settings(max_examples=500)` i obejrzyj shrinking przy błędzie
10. *(Trudniejsze)* Sprawdź własności klasy `BankAccount` przez wiele operacji
11. Przetestuj parser JSON - każdy poprawny JSON powinien sie sparsować
12. *(Trudniejsze)* Stateful testing - `@initialize`, `@rule`, `@invariant` dla `Stack`

---

## Moduł 12 — TDD i dobre praktyki

**Plik:** `12_tdd_patterns/12_tdd_patterns.ipynb`

Cykl Red-Green-Refactor w praktyce. Organizacja testów w projekcie.
Wzorce: Test Double, Object Mother, Test Data Builder.
Anti-patterny. Testy w CI/CD (GitHub Actions). `tox` / `nox`
do testowania na wielu wersjach Pythona.

**Instalacja:** `pip install tox nox`

### Sekcje
1. 🔹 TDD w praktyce - Red-Green-Refactor krok po kroku
2. 🔹 Organizacja testów i wzorce (Object Mother, Builder)
3. 🔹 CI/CD, `tox` i testowanie na wielu wersjach

### Ćwiczenia (9)
1. Zaprojektuj `BankAccount` przez TDD - zacznij od testu, napisz minimum kodu
2. Rozszerz `BankAccount` przez TDD o `transfer(to_account, amount)`
3. *(Trudniejsze)* TDD dla `ShoppingCart` z rabatem i podatkiem VAT
4. Refaktoryzuj testy uzywajac wzorca Object Mother dla `User`
5. Napisz `UserBuilder` z wzorcem Builder dla złożonych danych testowych
6. *(Trudniejsze)* Zidentyfikuj i napraw anti-patterny w podanym zestawie testów
7. Napisz `Makefile` z targetami `test`, `coverage`, `lint`
8. Napisz `.github/workflows/test.yml` uruchamiajacy pytest na push
9. *(Trudniejsze)* Skonfiguruj `tox.ini` dla Python 3.10 i 3.11 z `pytest` i `flake8`

---

## Zestawienie

| #  | Temat                              | Narzędzie            | Sekcje | Ćwiczenia | Czas   |
|----|-------------------------------------|----------------------|--------|-----------|--------|
| 00 | Wstęp do testowania                 | -                    | 3      | 9         | 1.5 h  |
| 01 | `unittest` - podstawy               | `unittest`           | 3      | 12        | 2.5 h  |
| 02 | `unittest` - zaawansowane           | `unittest`           | 3      | 9         | 2 h    |
| 03 | `pytest` - podstawy                 | `pytest`             | 3      | 12        | 2.5 h  |
| 04 | `pytest` - fixtures                 | `pytest`             | 4      | 12        | 3 h    |
| 05 | `pytest` - parametryzacja i markery | `pytest`             | 3      | 9         | 2 h    |
| 06 | `unittest.mock` - podstawy          | `unittest.mock`      | 3      | 12        | 3 h    |
| 07 | `unittest.mock` - zaawansowane      | `unittest.mock`      | 3      | 9         | 2.5 h  |
| 08 | `pytest-mock`                       | `pytest-mock`        | 3      | 9         | 2 h    |
| 09 | Pokrycie kodu                       | `coverage`/`pytest-cov` | 3   | 9         | 2 h    |
| 10 | Generowanie danych testowych        | `faker`              | 3      | 9         | 2 h    |
| 11 | Property-based testing              | `hypothesis`         | 3      | 12        | 3 h    |
| 12 | TDD i dobre praktyki                | `tox` / `nox`        | 3      | 9         | 2.5 h  |
| **Σ** |                                  |                      | **42** | **131**   | **~30 h** |

> ~30 h teorii i ćwiczeń = ok. **4 pełne dni szkoleniowe** (7.5 h/dzień).

### Kolejność narzędzi (od najpopularniejszego)

| Miejsce | Narzędzie | Moduł | Opis |
|---------|-----------|-------|------|
| 1 | `pytest` | 03-05 | Najpopularniejszy framework testowy Python |
| 2 | `unittest` | 01-02 | Wbudowany, standardowy (Java JUnit inspiracja) |
| 3 | `unittest.mock` | 06-07 | Wbudowany moduł do atrap |
| 4 | `pytest-mock` | 08 | Wrapper na `unittest.mock` dla pytest |
| 5 | `coverage` / `pytest-cov` | 09 | Pomiar pokrycia kodu |
| 6 | `faker` | 10 | Generowanie realistycznych danych |
| 7 | `hypothesis` | 11 | Property-based testing |
| 8 | `tox` / `nox` | 12 | Multi-env testowanie i CI |
