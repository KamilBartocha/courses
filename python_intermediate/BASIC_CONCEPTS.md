# Python od podstaw - przegląd pojęć

## 01 Instalacja, IDE i środowiska

**Python**
- Interpreter języka Python - wymagany do uruchamiania kodu
- Instalacja Windows: `python.org` → `.exe` → zaznacz **"Add Python to PATH"**
- Instalacja macOS: `python.org` → `.pkg` lub `brew install python`
- Weryfikacja: `python --version` / `python3 --version`

**IDE (Integrated Development Environment)**
- Edytor kodu vs. IDE: edytor = lekki, IDE = pełne środowisko z debuggerem
- PyCharm Community: darmowy, gotowy od razu, dedykowany Pythonowi
- Visual Studio Code: lekki, wymaga wtyczek (Python, Pylance, Jupyter)
- Wtyczki Python: Python, Pylance, Python Debugger, Ruff
- Wtyczki Jupyter: Jupyter, Jupyter Keymap, Jupyter Notebook Renderers
- Wtyczki Git: GitLens, Git History, Git Graph

**Algorytm**
- Skończony ciąg jasno zdefiniowanych kroków prowadzący do rozwiązania problemu
- Cechy: skończoność, jednoznaczność, poprawność, ogólność
- Pseudokod: nieformalny zapis algorytmu, niezależny od języka

**Schemat blokowy (flowchart)**
- Owal `╭─╮` - terminal: START / STOP
- Prostokąt `┌─┐` - process: operacja, obliczenie, przypisanie
- Romb / prostokąt z boczną strzałką `TAK ◄─┤ ├─► NIE` - decision: warunek
- Strzałka `▼` - kierunek przepływu

**Pierwsze programy w Pythonie**
- `print()` - wypisywanie na ekran
- `# komentarz` - ignorowany przez interpreter
- `name = "Alice"` - przypisanie zmiennej
- `f"Cześć, {name}!"` - f-string: wstawianie wartości do tekstu

**Jak działa interpreter?**
- `python.exe` (Windows) / `python3` (macOS/Linux) - plik wykonywalny z python.org
- Kod źródłowy (source code) - plik `.py` pisany przez programistę
- Kompilacja do bytecode - Python automatycznie tworzy pliki `.pyc` w `__pycache__/`
- Bytecode - pośredni format binarny z instrukcjami (LOAD_GLOBAL, CALL itp.)
- Interpreter / Python VM - wykonuje bytecode instrukcja po instrukcji
- CPython - standardowa implementacja interpretera, napisana w C
- `dis.dis(funkcja)` - podgląd bytecode funkcji

**Edytor kodu**
- Podświetlanie składni, autouzupełnianie, snippety, multi-kursor, wtyczki
- Popularne: VS Code, Sublime Text, Vim/Neovim, Emacs, Notepad++

**IDE vs. edytor**
- IDE dodatkowo: wbudowany debugger, testy jednostkowe, refaktoryzacja, Git

**IDLE**
- Dostarczany razem z Pythonem, bez dodatkowej instalacji
- Tryb Shell: interaktywne wykonywanie linijka po linijce
- Tryb Editor: pisanie i uruchamianie skryptów `.py`

**PyCharm**
- Community (darmowy) vs. Professional (płatny)
- Funkcje: debugger z breakpointami, konsola Python, obsługa Git, pytest

**Visual Studio Code**
- Kluczowe rozszerzenia: Python, Pylance, Jupyter, GitLens, Black Formatter
- Porównanie z PyCharm: szybszy start, niższe RAM, wymaga konfiguracji wtyczek

**Jupyter Notebook**
- Komórki Code (`Y`) i Markdown (`M`)
- Skróty: `Shift+Enter` (wykonaj + przejdź), `Esc` (tryb komend), `A`/`B` (nowa komórka), `DD` (usuń)
- Zmienne żyją we wspólnej przestrzeni nazw; kolejność wykonania ma znaczenie

**Git**
- Pojęcia: `repository`, `commit`, `branch`, `merge`, `push`, `pull`
- Komendy: `git init`, `git add .`, `git commit -m`, `git status`, `git log --oneline`, `git push`

---

## 02 Składnia i typy proste

**`print()` i formatowanie**
- Konkatenacja: `"Wiek: " + str(age)`
- `%` operator (legacy): `"Wiek: %d" % age` - najstarszy styl (Python 2)
- `.format()` (Python 2.6+): `"Wiek: {}".format(age)` - nadal popularny
- f-string (zalecany): `f"Wiek: {age}"`, formatowanie `f"{price:.2f}"`

**Komentarze**
- Jednolinijkowy: `# tekst`
- Wielolinijkowy: `"""tekst"""` lub `'''tekst'''`

**Zmienne i typy danych**
- Typy liczbowe: `int` (`42`), `float` (`3.14`), `complex` (`1+2j`)
- Przypisanie skrócone: `+=`, `-=`, `*=`
- `type()` - sprawdzenie typu; Python sam rozpoznaje typ (dynamiczne typowanie)
- `NameError` przy użyciu zmiennej przed przypisaniem
- 9 typów wbudowanych: `int`, `float`, `complex`, `bool`, `str`, `list`, `tuple`, `set`, `dict`

**Arytmetyka i operatory**
- `+` `-` `*` `/` `//` `%` `**` - operatory arytmetyczne
- `/` zawsze zwraca `float`; `//` dzielenie całkowite
- Porównania: `==` `!=` `>` `<` `>=` `<=` - zwracają `bool`
- Logiczne: `not`, `and`, `or`
- Zamiana zmiennych: `a, b = b, a` (tuple unpacking)

**Typ logiczny (bool), None i konwersja**
- `bool(0)` → `False`; `bool("")` → `False`; `bool([])` → `False`
- `None` - jedyna wartość typu `NoneType`; oznacza "brak wartości"
- Porównujemy `None` przez `is`: `if x is None:`
- `isinstance(obj, Klasa)` - sprawdza typ z uwzględnieniem podklas
- `isinstance(obj, (int, float))` - sprawdzenie wielu typów naraz
- `int(x)`, `float(x)`, `str(x)`, `bool(x)` - konwersja typów
- `int(3.9)` → `3` (obcięcie, nie zaokrąglenie)

**Łańcuchy znaków (strings)**
- Sekwencje specjalne: `\n` (nowa linia), `\t` (tabulator), `\\`, `\'`
- Raw string: `r"C:\Users\name"` - wyłącza interpretację `\`
- Stringi są **immutable** (niezmienne)
- Indeksowanie: `s[0]` (pierwszy), `s[-1]` (ostatni)
- Slicing: `s[start:stop]`, `s[::-1]` (odwrócony)
- Metody: `s.upper()`, `s.lower()`, `s.strip()`, `s.replace(a, b)`
- `s.split(sep)`, `s.count(sub)`, `s.startswith(p)`

**Dane wejściowe (`input()`)**
- Zawsze zwraca `str`; konwersja: `int(input())`, `float(input())`
- Błędny typ wejściowy → `ValueError`

---

## 03 Kolekcje i sterowanie przepływem

**Lista (list)**
- Ordered, **mutable** kolekcja; obsługuje indeksowanie i slicing
- `lst.append(x)`, `lst.insert(i, x)`, `lst.remove(x)`, `lst.pop(i)`
- `lst.sort()` - modyfikuje oryginał; `sorted(lst)` - zwraca nową listę
- `len(lst)`, `lst.count(x)`, `lst.index(x)`
- Lista zagnieżdżona: `matrix[1][0]`

**Krotka (tuple)**
- Immutable lista; bezpieczna jako klucz słownika
- Slicing działa tak samo jak dla listy

**Słownik (dict)**
- `d[key]`, `d[key] = value`, `del d[key]`, `key in d`
- `d.keys()`, `d.values()`, `d.items()`

**Zbiór (set)**
- Bez duplikatów, bez kolejności
- Operacje: `|` (suma), `&` (część wspólna), `-` (różnica)

**Instrukcje warunkowe**
- `if` / `elif` / `else`
- Wyrażenie ternarne: `result = x if warunek else y`
- Wcięcia: Python używa 4 spacji zamiast `{}` jak w C/Java

**Pętle**
- `for x in iterable:` - iteracja po kolekcji
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- `while warunek:` - dopóki warunek prawdziwy
- `break` - przerywa pętlę; `continue` - następna iteracja; `pass` - nic nie robi
- `enumerate(iterable, start=0)` - zwraca pary `(indeks, wartość)`;
  `for i, v in enumerate(lst):` zamiast ręcznego licznika

---

## 04 Funkcje

**Definiowanie funkcji**
- `def nazwa(parametry):` + wcięty blok kodu
- Wywołanie: `nazwa(argumenty)`

**Parametry i argumenty**
- Parametry pozycyjne (positional), domyślne (default): `def f(x, y=0)`
- Argumenty słownikowe (keyword arguments): `f(y=5, x=2)`
- ⚠️ Mutable default argument: `def f(lst=[])` - pułapka! Lista tworzona raz
- Poprawny wzorzec: `def f(lst=None): if lst is None: lst = []`

**`*args` i `**kwargs`**
- `*args` - zbiera dodatkowe argumenty pozycyjne w krotkę
- `**kwargs` - zbiera dodatkowe argumenty słownikowe w słownik
- Kolejność: `def f(stałe, *args, **kwargs)`
- Gwiazdki `*` `**` to składnia, nie nazwy

**Zakres zmiennych - reguła LEGB**
- **L**ocal - wewnątrz bieżącej funkcji
- **E**nclosing - w funkcji zewnętrznej (zagnieżdżone funkcje)
- **G**lobal - poziom modułu (plik `.py`)
- **B**uilt-in - wbudowane nazwy Pythona (`len`, `print`)
- `global counter` - modyfikacja zmiennej globalnej wewnątrz funkcji
- Zmienna lokalna przysłania globalną o tej samej nazwie

**Wartość zwracana**
- `return wartość` - zwraca i kończy funkcję
- Bez `return` → funkcja zwraca `None`
- Różnica: `print()` wypisuje, `return` zwraca wartość do użycia

**Docstring**
- `"""Opis funkcji."""` - bezpośrednio po `def`
- Dostępny przez `help(funkcja)` i `funkcja.__doc__`

**Rekurencja**
- Funkcja wywołuje samą siebie
- Wymaga warunku bazowego (base case) aby uniknąć `RecursionError`
- Iteracja vs. rekurencja: rekurencja elegancka dla problemów drzewiastych

---

## 05 Pliki i moduły

**Otwieranie pliku**
- `open(ścieżka, tryb)` - zwraca obiekt pliku
- Tryby: `'r'` (read), `'w'` (write, nadpisuje), `'a'` (append)

**Czytanie pliku**
- `f.read()` - cały plik jako string
- `f.readline()` - jedna linia
- `f.readlines()` - lista linii
- `for line in f:` - linia po linii (wydajne dla dużych plików)

**Zapis do pliku**
- `f.write(tekst)` - zapis stringa
- Tryb `'w'` nadpisuje; `'a'` dopisuje na koniec

**Menadżer kontekstu (context manager)**
- `with open(...) as f:` - automatycznie zamyka plik nawet przy błędzie
- Zalecany sposób pracy z plikami

**Moduły**
- `import moduł` - importuje cały moduł
- `from moduł import nazwa` - importuje konkretny element
- `import moduł as alias` - alias dla skrócenia nazwy
- Biblioteka standardowa: `os`, `sys`, `math`, `random`, `datetime` i wiele innych ("Batteries Included")

**Instalowanie pakietów**
- `pip install nazwa` - instalacja z PyPI
- `pip list` - lista zainstalowanych pakietów

**Wirtualne środowiska (virtual environments)**
- `python -m venv venv` - tworzenie środowiska
- `source venv/bin/activate` (macOS/Linux) / `venv\Scripts\activate` (Windows)
- `pip freeze > requirements.txt` - zapis zależności
- `pip install -r requirements.txt` - instalacja z pliku
- `deactivate` - dezaktywacja; katalog `venv/` dodajemy do `.gitignore`

**`__name__ == "__main__"`**
- `__name__` = `'__main__'` gdy plik uruchomiony bezpośrednio
- `__name__` = nazwa pliku gdy plik zaimportowany jako moduł
- Wzorzec: `if __name__ == '__main__': main()` - kod tylko przy uruchomieniu
- Umożliwia tworzenie plików, które są jednocześnie skryptami i modułami

---

## 06 Wyjątki

**Wyjątki (exceptions)**
- Obiekt reprezentujący błąd podczas wykonania programu
- Nie złapany wyjątek → `Traceback` i crash

**Wbudowane wyjątki**
- `ZeroDivisionError` - dzielenie przez zero
- `NameError` - niezdefiniowana zmienna
- `TypeError` - niezgodne typy
- `ValueError` - poprawny typ, zła wartość (np. `int("abc")`)
- `IndexError` - indeks poza zakresem listy
- `KeyError` - brakujący klucz w słowniku
- `FileNotFoundError` - plik nie istnieje
- `AttributeError` - obiekt nie ma danego atrybutu

**Obsługa wyjątków**
- `try:` - blok chroniony
- `except TYP as e:` - obsługa konkretnego wyjątku
- `else:` - wykonuje się gdy NIE było wyjątku
- `finally:` - wykonuje się zawsze (np. zamknięcie pliku)

**Podnoszenie wyjątków**
- `raise ValueError("komunikat")` - zgłaszamy własny wyjątek
- `raise` (bez argumentu) - ponowne zgłoszenie złapanego wyjątku

**Własne wyjątki (custom exceptions)**
- `class MyError(Exception): pass` - własna klasa wyjątku
- Dziedziczymy po `Exception`, `ValueError`, `TypeError` itp.
- Własny wyjątek można łapać konkretnie lub przez klasę bazową
- Dobieramy klasę bazową do rodzaju błędu (np. `ValueError` dla złej wartości)

---

## 07 Programowanie funkcyjne

### Część podstawowa

**Paradygmat funkcyjny**
- Funkcje jako wartości (first-class functions)
- Brak efektów ubocznych (side effects) - funkcja nie zmienia stanu zewnętrznego
- Imperatywny: *jak* (pętla + append); Funkcyjny: *co* (transformacja)

**Lambda (funkcje anonimowe)**
- `lambda x: x * 2` - jednolinijkowa funkcja bez nazwy
- `sorted(lst, key=lambda x: x[1])` - sortowanie po kluczu

**List comprehension**
- `[wyrażenie for x in iterable if warunek]`
- Zagnieżdżone: `[x for row in matrix for x in row]`

**Set comprehension**
- `{wyrażenie for x in iterable}`

**Dict comprehension**
- `{k: v for k, v in słownik.items()}`
- `zip()` - łączenie dwóch sekwencji w pary: `zip(keys, values)`

---

### Część zaawansowana

**`map()` i `filter()`**
- `map(func, iterable)` - stosuje funkcję do każdego elementu
- `filter(func, iterable)` - zachowuje elementy gdzie `func` → `True`
- Zwracają obiekty leniwe (lazy); `list()` żeby zmaterializować
- Gdy masz gotową funkcję → `map()`; gdy piszesz logikę → comprehension

**`reduce()`**
- `from functools import reduce`
- `reduce(func, iterable)` - redukuje sekwencję do jednej wartości kumulatywnie
- Opcjonalna wartość początkowa: `reduce(func, iterable, initializer)`

**Wyrażenia generatorowe (generator expressions)**
- `(wyrażenie for x in iterable)` - nawiasy okrągłe
- Leniwe obliczenia (lazy): jeden element na raz, nie ładuje całości do pamięci
- Generator można przejść tylko raz

---

## 08 Programowanie obiektowe (OOP)

### Część podstawowa — Wprowadzenie

**Czym jest OOP**
- Klasa (class) = przepis / foremka; Obiekt (object/instance) = konkretny egzemplarz
- Atrybut (attribute) = dane obiektu; Metoda (method) = funkcja obiektu

**Wszystko jest obiektem**
- W Pythonie każda wartość (int, str, lista) jest obiektem z atrybutami i metodami

**Tożsamość, typ, wartość**
- `id(obj)` - unikalny adres w pamięci (tożsamość)
- `type(obj)` - klasa, do której należy obiekt
- `is` - porównuje tożsamość (ten sam obiekt); `==` - porównuje wartość

**Atrybuty i metody**
- Atrybuty: dane przechowywane na obiekcie (`obj.name`)
- Metody: funkcje należące do obiektu (`obj.bark()`)

**Funkcje vs. metody**
- Funkcja: `sorted(lst)` - nie modyfikuje oryginału, zwraca nowy obiekt
- Metoda: `lst.sort()` - modyfikuje oryginał in-place

**Tworzenie klas**
- `class NazwaKlasy:` - definicja klasy
- `__init__(self, ...)` - konstruktor, wywoływany przy tworzeniu obiektu
- `self` - referencja do bieżącego obiektu (odpowiednik `this` w innych językach)

---

### Część zaawansowana — kontynuowana w kolejnym kursie

**Cztery filary OOP**
- **Enkapsulacja (encapsulation)** - ukrycie szczegółów wewnętrznych
- **Dziedziczenie (inheritance)** - budowanie klas na bazie innych klas
- **Polimorfizm (polymorphism)** - różne obiekty reagują na tę samą metodę inaczej
- **Abstrakcja (abstraction)** - praca z obiektami na wysokim poziomie

**Dziedziczenie (inheritance)**
- `class Dog(Animal):` - `Dog` dziedziczy po `Animal`
- `super().__init__(...)` - wywołanie konstruktora klasy bazowej
- Nadpisanie metody (method overriding) - klasa potomna redefiniuje metodę
- `super().metoda()` - wywołanie metody rodzica z klasy potomnej
- `isinstance(obj, Klasa)` - sprawdza przynależność do klasy i jej podklas
- Zasada "is-a": `Dog` is-a `Animal`

**Metody specjalne (dunder methods)**
- `__str__(self)` - wywoływana przez `print(obj)` i `str(obj)`; czytelna wersja dla użytkownika
- `__repr__(self)` - wywoływana przez `repr(obj)` i konsolę; wersja dla dewelopera
- `__len__(self)` - wywoływana przez `len(obj)`; zwraca rozmiar obiektu
- Jeśli brak `__str__`, Python używa `__repr__` jako fallback
- Zawsze definiujemy przynajmniej `__repr__` - ułatwia debugowanie
