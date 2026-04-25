# Pomysły i rozszerzenia

## Potencjalne dodatkowe moduły

- Flyweight - optymalizacja pamięci (współdzielenie małych obiektów)
- Visitor - oddzielenie algorytmu od struktury danych (double dispatch)
- Memento - zapisywanie i przywracanie stanu obiektu (undo history)
- Interpreter - prosta gramatyka wyrażeń (mini DSL)

## Pomysły na projekty zaawansowane

- Mini-framework webowy: Singleton (config), Decorator (middleware),
  Observer (events), Strategy (routing), Chain of Responsibility (request
  pipeline)
- CLI task manager: Command (undo/redo), State (task states),
  Builder (task creation), Iterator (task lists)
- System logowania: Observer (handlers), Decorator (formatters),
  Chain of Responsibility (log levels), Strategy (output target)

## Pomysły na ćwiczenia zaawansowane

- Porównanie wydajności Singleton z Lock vs. bez Lock
  (moduł `timeit`, 1000 iteracji wątkowych)
- Benchmark dekoratorów: narzut wywołań vs. "nagie" funkcje
- Profilowanie `functools.lru_cache`: fibonacci(30), fibonacci(40),
  fibonacci(50) - czas z cache i bez
- Zmiana pamięci dla Flyweight vs. zwykłych obiektów (`tracemalloc`)

## Linki i zasoby

- "Design Patterns" - Gamma, Helm, Johnson, Vlissides (GoF, 1994)
- "Head First Design Patterns" - Freeman & Robson (2004)
- refactoring.guru/design-patterns/python
- python-patterns.guide (Brandon Rhodes)
- docs.python.org/3/library/abc.html
- docs.python.org/3/library/functools.html
- docs.python.org/3/library/weakref.html
