# Python Intermediate — Syllabus

Kurs obejmuje 17 modułów (notebooks 100–116).
Łącznie **186 ćwiczeń** w **67 sekcjach** tematycznych.

---

## Moduł 100 — Powtórka podstaw

**Plik:** `100_python_interm_basics/100_python_interm_bacics_retake.ipynb`

Przegląd materiału z kursu podstawowego, który jest wymagany przed
przystąpieniem do modułów 101–110.

Tematy: arytmetyka, łańcuchy tekstowe, typy danych, pętle, funkcje,
wyrażenia lambda, list comprehensions, obsługa błędów, operacje na plikach.

---

## Moduł 101 — Programowanie obiektowe (zaawansowane)

**Plik:** `101_python_interm_oop_advanced/101_python_interm_oop_advanced.ipynb`

### Sekcje
1. 🔹 Podstawy OOP
2. 🔹 Dziedziczenie i `super()`
3. 🔹 Hermetyzacja (enkapsulacja)
4. 🔹 Metody specjalne (dunder)
5. 🔹 Metody klasowe: `self` vs `cls`

### Ćwiczenia (15)
1. Klasa `Rectangle` z atrybutami `width` / `height`
2. Klasa `Book` z atrybutami `title`, `author`, `year`
3. *(Trudniejsze)* Klasa `ShoppingCart`
4. Dziedziczenie: `Animal` → `Dog`
5. Klasa bazowa `Shape` z metodą `area()`
6. Nadpisywanie metod (`override`)
7. `super()` w konstruktorze
8. Atrybut prywatny i getter/setter
9. *(Trudniejsze)* `@property` z walidacją
10. `__str__` i `__repr__`
11. `__eq__` i `__lt__`
12. *(Trudniejsze)* `__add__` i `__len__`
13. `@classmethod` jako alternatywny konstruktor
14. `@staticmethod` — metoda niezależna od instancji
15. *(Trudniejsze)* Kombinacja metod klasowych i instancji

---

## Moduł 102 — Lambda, map, filter, Comprehensions

**Plik:** `102_python_interm_lambda/102_python_interm_lambda_map_filter_comp.ipynb`

### Sekcje
1. 🔹 List comprehensions
2. 🔹 Dictionary comprehensions
3. 🔹 Set i Generator comprehensions
4. 🔹 Funkcje lambda
5. 🔹 `map()` i `filter()`

### Ćwiczenia (15)
1. List comprehension — kwadraty, parzyste, uppercase
2. Filtrowanie i transformacja słów
3. *(Trudniejsze)* Krotki `(liczba, kwadrat, sześcian)` dla liczb nieparzystych
4. Słownik długości nazw
5. Filtrowanie i zaokrąglanie cen w słowniku
6. *(Trudniejsze)* Uśrednianie ocen uczniów
7. Unikalnych pierwsze litery z `set` comprehension
8. Suma kwadratów z generatorem
9. *(Trudniejsze)* Generator `countdown()`
10. Funkcje `lambda`: kwadrat, `is_even`
11. Sortowanie łańcuchów lambdą (alfabetycznie, po długości, po ostatnim znaku)
12. *(Trudniejsze)* Filtrowanie produktów po cenie z `filter()` i `sorted()`
13. Konwersja Celsius → Fahrenheit z `map()`
14. Filtrowanie liczb dodatnich i podniesienie do kwadratu
15. *(Trudniejsze)* Filtrowanie ciągów alfabetycznych i `title()`

---

## Moduł 103 — `*args` i `**kwargs`

**Plik:** `103_python_interm_args_kwargs/103_python_interm_args_kwargs.ipynb`

### Sekcje
1. 🔹 `*args`
2. 🔹 `**kwargs`
3. 🔹 Łączenie `*args` i `**kwargs`
4. 🔹 Rozpakowywanie `*` i `**`

### Ćwiczenia (12)
1. Funkcja `multiply_all(*args)`
2. Funkcja `merge_lists(*args)`
3. *(Trudniejsze)* `calculate_stats(*args)` — count, total, average, min, max
4. Funkcja `greet(**kwargs)` z opcjonalnym tytułem
5. `filter_params(**kwargs)` — zwracanie par z wartością > 10
6. *(Trudniejsze)* `validate_user(**kwargs)` — sprawdzanie wymaganych pól
7. `format_message(*args, separator, end)`
8. `build_html(tag, *content, **attributes)`
9. *(Trudniejsze)* `log(level, *messages, **context)`
10. Scalanie słowników operatorem `**`
11. Rozszerzone rozpakowywanie z `*`
12. *(Trudniejsze)* Wywołanie funkcji z rozpakowanymi `args` i `kwargs`

---

## Moduł 104 — Wirtualne środowisko i Debugger

**Plik:** `104_python_interm_venv/104_python_interm_virtual_env_debuger.ipynb`

### Sekcje
1. 🔹 Wirtualne środowisko (`venv`)
2. 🔹 `requirements.txt`
3. 🔹 Debugger

### Ćwiczenia (9)
1. Polecenia tworzenia `venv`, aktywacji i instalacji pakietu
2. Dwa projekty z różnymi wersjami Selenium (3.141.0 vs 4.18.0)
3. *(Trudniejsze)* Weryfikacja aktywnego `venv` przez `sys.prefix`
4. Analiza formatu i operatorów w `requirements.txt`
5. Lista zainstalowanych pakietów i generowanie `requirements.txt`
6. *(Trudniejsze)* Wersja pakietu przez `importlib.metadata`
7. Znalezienie i naprawa błędu w `sum_to_n`
8. Znalezienie i naprawa błędu w `count_vowels`
9. *(Trudniejsze)* Znalezienie i naprawa błędu w `primes_up_to`

---

## Moduł 105 — Własne moduły i biblioteki

**Plik:** `105_python_interm_modules/105_python_interm_own_modules.ipynb`

### Sekcje
1. 🔹 Moduły i pakiety
2. 🔹 Tworzenie biblioteki — projekt `datareader`
3. 🔹 Testy i instalacja

### Ćwiczenia (9)
1. Moduł `mathutils` — `add`, `subtract`, `multiply`, `average`
2. Moduł `stringutils` — `clean`, `capitalize_words`, `count_words`
3. *(Trudniejsze)* `__init__.py` dla pakietu `myutils`
4. Struktura pakietu i `__init__.py` dla `calculator`
5. Klasa `SimpleJSON`
6. *(Trudniejsze)* `SimpleJSON` z metodami `keys()` i `summary()`
7. Testy jednostkowe dla funkcji `mathutils`
8. Test obsługi `FileNotFoundError`
9. *(Trudniejsze)* Konfiguracja `setup.py` dla `myutils`

---

## Moduł 106 — JSON

**Plik:** `106_python_interm_json/106_python_interm_json.ipynb`

### Sekcje
1. 🔹 Format JSON i typy danych
2. 🔹 Serializacja i deserializacja
3. 🔹 Praca z plikami JSON
4. 🔹 Obsługa błędów

### Ćwiczenia (12)
1. `dict` → JSON string z `indent`
2. Parsowanie JSON string → `dict`
3. *(Trudniejsze)* Round-trip: `dict` → JSON → `dict`
4. `json.dumps()` z `sort_keys`
5. Zapis `dict` do pliku JSON z `ensure_ascii=False`
6. *(Trudniejsze)* Wczytanie, modyfikacja i zapis pliku JSON
7. Zapis i odczyt listy słowników
8. Wczytanie zagnieżdżonego `config.json`
9. *(Trudniejsze)* Filtrowanie zamówień po statusie i zapis wyniku
10. Walidacja wielu JSON string z obsługą `JSONDecodeError`
11. Funkcja `load_or_default(path, default)`
12. *(Trudniejsze)* Funkcja `update_json(path, key, value)`

---

## Moduł 107 — Wyjątki

**Plik:** `107_python_interm_exception/107_python_interm_exception.ipynb`

### Sekcje
1. 🔹 `try` / `except` / `else` / `finally`
2. 🔹 Wbudowane wyjątki
3. 🔹 Podnoszenie wyjątków (`raise`)
4. 🔹 Własne wyjątki (custom exceptions)

### Ćwiczenia (12)
1. Funkcja `safe_open` z `try/except/finally`
2. `try/except/else` — konwersja na `int`
3. *(Trudniejsze)* `safe_divide` — `ZeroDivisionError` i `TypeError`
4. Pętla z obsługą `ValueError` i `ZeroDivisionError`
5. Funkcja `get_item` z `IndexError`
6. *(Trudniejsze)* Funkcja `safe_get` z `TypeError`
7. Funkcja `validate_score` z `TypeError` i `ValueError`
8. Funkcja `to_upper` z `TypeError`
9. *(Trudniejsze)* `BankAccount.withdraw` z `ValueError`
10. Własny wyjątek `NegativeValueError`
11. *(Trudniejsze)* `AgeError` z atrybutem `age`
12. *(Trudniejsze)* Hierarchia wyjątków: `StorageError` → `FileReadError`, `FileWriteError`

---

## Moduł 108 — Dekoratory

**Plik:** `108_python_interm_decorators/108_python_interm_decorators.ipynb`

### Sekcje
1. 🔹 Podstawy dekoratorów
2. 🔹 Dekoratory z parametrami
3. 🔹 Wbudowane dekoratory
4. 🔹 `@dataclass`

### Ćwiczenia (12)
1. Dekorator `shout` dodający wykrzykniki
2. Dekorator `print_args` wyświetlający typy argumentów
3. *(Trudniejsze)* Dekorator `count_calls` zliczający wywołania
4. Dekorator `repeat(n)` wywołujący funkcję `n` razy
5. Dekorator `validate_type` sprawdzający typy
6. *(Trudniejsze)* Dekorator `retry(times)` z obsługą wyjątków
7. Klasa `Converter` z `@staticmethod` — `km_to_miles`, `celsius_to_fahrenheit`
8. Klasa `Date` z `@classmethod` — `from_string`, `today`
9. *(Trudniejsze)* Klasa `Rectangle` z `@property` — `width`, `height`, `area`, `perimeter`
10. `@dataclass` dla klasy `Book` z metodą `age()`
11. `@dataclass(frozen=True)` dla `Coordinate` jako klucz słownika
12. *(Trudniejsze)* `@dataclass` dla `Student` z listą ocen i metodą `average()`

---

## Moduł 109 — Menedżer kontekstu

**Plik:** `109_python_interm_context_man/109_python_interm_context_man.ipynb`

### Sekcje
1. 🔹 Blok `with`
2. 🔹 CM przez klasę (`__enter__` i `__exit__`)
3. 🔹 `@contextmanager`
4. 🔹 Praktyczne wzorce

### Ćwiczenia (12)
1. Zapis i odczyt pliku z blokiem `with`
2. Funkcja `copy_file` z dwoma uchwytami pliku
3. *(Trudniejsze)* Funkcja `word_count` z obsługą błędów
4. Klasa `Indenter` — CM kontrolujący wcięcia
5. Klasa `SuppressError` — CM tłumiący wyjątki
6. *(Trudniejsze)* `TemporaryFile` — CM tworzący i usuwający plik
7. `@contextmanager` `log_block`
8. `@contextmanager` `open_write` z obsługą błędów
9. *(Trudniejsze)* `@contextmanager` `temp_env` dla zmiennych środowiskowych
10. Klasa `ReadOnlyFile` — CM blokujący zapis
11. *(Trudniejsze)* `@contextmanager` `managed_db` z SQLite
12. *(Trudniejsze)* CM `APISession` z `requests.Session`

---

## Moduł 110 — Metaklasy

**Plik:** `110_python_interm_metaclass/110_python_interm_metaclass.ipynb`

### Sekcje
1. 🔹 Metaklasy i `type`
2. 🔹 Tworzenie metaklasy
3. 🔹 Praktyczne wzorce
4. 🔹 `__init_subclass__` — nowoczesna alternatywa

### Ćwiczenia (12)
1. Sprawdzenie metaklas typów wbudowanych
2. Dynamiczne tworzenie klasy `Rectangle` przez `type()`
3. *(Trudniejsze)* Funkcja `make_class` tworząca klasy dynamicznie
4. `UpperAttrsMeta` — wymuszanie wielkich liter w nazwach atrybutów
5. `VersionedMeta` — automatyczne dodawanie `version` i `created_by`
6. *(Trudniejsze)* `ReadOnlyMeta` — blokowanie modyfikacji atrybutów
7. `TypeRegistryMeta` — rejestrowanie podklas
8. `CountInstancesMeta` — liczenie instancji
9. *(Trudniejsze)* `AbstractMeta` — blokowanie tworzenia instancji klas abstrakcyjnych
10. `__init_subclass__` — rejestr komend (`Command`)
11. `__init_subclass__` — wymuszanie walidatorów (`Validator`)
12. *(Trudniejsze)* Porównanie podejść: metaklasa vs `__init_subclass__`

---

---

## Moduł 111 — Abstrakcyjne klasy bazowe (`abc`)

**Plik:** `111_python_interm_abc/111_python_interm_abc.ipynb`

### Sekcje
1. 🔹 Klasy abstrakcyjne i `abc.ABC`
2. 🔹 `@abstractmethod` i `@abstractproperty`
3. 🔹 `isinstance()` / `issubclass()` z ABC

### Ćwiczenia (9)
1. Abstrakcyjna klasa `Animal` - podklasy `Dog` i `Bird`
2. Abstrakcyjna klasa `Vehicle` - `Car` i `Bicycle` z `@property`
3. *(Trudniejsze)* `Serializable` z `to_dict()` i `from_dict()` (classmethod)
4. `Logger` z abstrakcyjną właściwością `level` - `ConsoleLogger`, `FileLogger`
5. `Parser` z abstrakcyjną metodą klasową `supported_format()`
6. *(Trudniejsze)* `Validator` z metodą `check()` rzucającą `ValueError`
7. `Iterable_` z `__subclasshook__` sprawdzającym `__iter__`
8. `Printable` - rejestracja klasy bez dziedziczenia przez `register()`
9. *(Trudniejsze)* `Plugin` z automatycznym rejestrem przez `__init_subclass__`

---

## Moduł 112 — Generatory i iteratory

**Plik:** `112_python_interm_generators/112_python_interm_generators.ipynb`

### Sekcje
1. 🔹 Protokół iteratora (`__iter__`, `__next__`)
2. 🔹 Funkcje generatorowe (`yield`)
3. 🔹 `yield from` i generatory zaawansowane
4. 🔹 Moduł `itertools`

### Ćwiczenia (12)
1. Klasa `Range_` imitująca wbudowany `range(start, stop, step)`
2. Iterator `Fibonacci` z parametrem `limit`
3. *(Trudniejsze)* Iterator `Cycle` - nieskończone powtarzanie sekwencji
4. Generator `evens(n)` - parzyste liczby do n
5. Generator `running_average(numbers)` - bieżąca średnia
6. *(Trudniejsze)* Generator `flatten(nested)` - rekurencyjne spłaszczanie
7. Generator `tree_values(node)` z `yield from` - pre-order DFS
8. Generator `interleave(*iters)` - splot wielu sekwencji
9. *(Trudniejsze)* Generator `moving_window(iterable, size)` - okno przesuwne
10. `itertools.chain.from_iterable` i `compress`
11. `itertools.combinations` i `permutations`
12. *(Trudniejsze)* `sorted` + `itertools.groupby` - sumy transakcji per osoba

---

## Moduł 113 — `functools`

**Plik:** `113_python_interm_functools/113_python_interm_functools.ipynb`

### Sekcje
1. 🔹 `functools.partial`
2. 🔹 `functools.lru_cache` i memoizacja
3. 🔹 `functools.reduce` i `total_ordering`

### Ćwiczenia (9)
1. `partial` - wersja `greet` z polskim powitaniem
2. `partial` - gotowe loggery `log_info` i `log_error`
3. *(Trudniejsze)* `partial` + `map()` - masowe ustawianie pola w słownikach
4. `@lru_cache` - liczba sposobów wejścia po schodach
5. `@lru_cache` - pomiar przyspieszenia kosztownej funkcji
6. *(Trudniejsze)* Własny dekorator `memoize` bez `lru_cache`
7. `reduce` - maksimum i suma kwadratów bez `max()`
8. `reduce` - scalanie listy słowników
9. *(Trudniejsze)* `@total_ordering` - klasa `Card` do sortowania talii

---

## Moduł 114 — `collections` i `enum`

**Plik:** `114_python_interm_collections/114_python_interm_collections.ipynb`

### Sekcje
1. 🔹 `Counter` i `defaultdict`
2. 🔹 `deque` i `namedtuple`
3. 🔹 `enum.Enum` i `IntEnum`
4. 🔹 `enum.auto()` i `Flag`

### Ćwiczenia (12)
1. `Counter` - analiza tekstów: top-5, część wspólna, różnica
2. `defaultdict` - grupowanie i sumowanie transakcji per użytkownik
3. *(Trudniejsze)* `word_frequency()` z usuwaniem interpunkcji + hapax legomena
4. Klasa `Queue` (FIFO) oparta na `deque`
5. `namedtuple Employee` - sortowanie i średnie wynagrodzenie per wydział
6. *(Trudniejsze)* `LRUCache(capacity)` z `deque` i `dict`
7. Wyliczenie `Direction` z metodą `opposite()`
8. `IntEnum Priority` z funkcją `filter_tasks(min_priority)`
9. *(Trudniejsze)* Wyliczenie `Planet` z `surface_gravity` i `weight()`
10. Wyliczenie `Weekday` z `auto()` i metodą `is_weekend()`
11. `Flag FileMode` z funkcją `open_mode()` zwracającą string dla `open()`
12. *(Trudniejsze)* Wyliczenie `Status` z `can_transition_to()` i słownikiem dozwolonych przejść

---

## Moduł 115 — Adnotacje typów (`typing`)

**Plik:** `115_python_interm_typing/115_python_interm_typing.ipynb`

### Sekcje
1. 🔹 Podstawy adnotacji typów
2. 🔹 Moduł `typing` (`Optional`, `Union`, `Callable`)
3. 🔹 `TypeVar`, `Generic` i `Protocol`

### Ćwiczenia (9)
1. Dodanie adnotacji do `calculate_bmi`, `get_initials`, `flatten_once`
2. Klasa `Point` z adnotowanymi polami i metodami `distance_to`, `midpoint`
3. *(Trudniejsze)* Generyczna funkcja `group_by(items, key_func) -> dict`
4. `safe_parse_int() -> Optional[int]` i `parse_list() -> list[int]`
5. Generyczna `transform(data, func)` z `Callable` w adnotacji
6. *(Trudniejsze)* `deep_get(d, *keys)` - bezpieczny dostęp do zagnieżdżonych dict
7. Generyczne `last(items)` i `zip_with(a, b, func)` z `TypeVar`
8. Generyczna klasa `Pair[T, U]` z `swap()` i `map_first()`
9. *(Trudniejsze)* `Protocol Comparable` + generyczny `binary_search`

---

---

## Moduł 116 — Pydantic

**Plik:** `116_python_interm_pydantic/116_python_interm_pydantic.ipynb`

### Sekcje
1. 🔹 `BaseModel` — definiowanie i walidacja modeli danych
2. 🔹 `Field` i typy złożone — ograniczenia, wartości domyślne, aliasy
3. 🔹 Walidatory — `@field_validator`, `@model_validator`
4. 🔹 Konfiguracja i ustawienia — `model_config`, `BaseSettings`

### Ćwiczenia (12)
1. Model `Product` z podstawowymi polami i walidacją
2. Zagnieżdżone modele `Author` i `Book`
3. *(Trudniejsze)* `load_users()` — wczytywanie listy z JSON z obsługą błędów
4. Model `Order` z ograniczeniami `Field` (`gt`, `min_length`, `ge`)
5. Model `Config` z aliasami (`server_host`, `server_port`)
6. *(Trudniejsze)* `Cart` z `@computed_field` `total`
7. `@field_validator` — walidacja siły hasła (długość, cyfra, wielka litera)
8. `@model_validator(mode='after')` — `DateRange` (start < end)
9. *(Trudniejsze)* `Invoice` z `@computed_field` `subtotal` i `total_after_discount`
10. `ConfigDict` — `Tag` z `str_strip_whitespace`, `str_to_lower`, `frozen`
11. `extra='forbid'` — `ApiResponse` blokujący nieznane pola
12. *(Trudniejsze)* `DatabaseConfig` z `@computed_field` `url` (connection string)

---

## Zestawienie

| #   | Temat                                 | Sekcje | Ćwiczenia |
|-----|---------------------------------------|--------|-----------|
| 100 | Powtórka podstaw                      | —      | —         |
| 101 | OOP zaawansowane                      | 5      | 15        |
| 102 | Lambda, map, filter, comprehensions   | 5      | 15        |
| 103 | `*args` i `**kwargs`                  | 4      | 12        |
| 104 | Wirtualne środowisko i debugger       | 3      | 9         |
| 105 | Własne moduły i biblioteki            | 3      | 9         |
| 106 | JSON                                  | 4      | 12        |
| 107 | Wyjątki                               | 4      | 12        |
| 108 | Dekoratory                            | 4      | 12        |
| 109 | Menedżer kontekstu                    | 4      | 12        |
| 110 | Metaklasy                             | 4      | 12        |
| 111 | Abstrakcyjne klasy bazowe (`abc`)     | 3      | 9         |
| 112 | Generatory i iteratory                | 4      | 12        |
| 113 | `functools`                           | 3      | 9         |
| 114 | `collections` i `enum`               | 4      | 12        |
| 115 | Adnotacje typów (`typing`)            | 3      | 10        |
| 116 | Pydantic                              | 4      | 12        |
| **Σ** |                                     | **67** | **186**   |
