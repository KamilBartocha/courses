# Wzorce projektowe w Pythonie - Syllabus

---

## Moduł 01 - Wprowadzenie i zasady SOLID

1. Czym jest wzorzec projektowy (design pattern) - definicja, historia
2. Książka GoF (Gang of Four) "Design Patterns" (1994) - geneza wzorców
3. Trzy kategorie wzorców: kreacyjne (creational), strukturalne
   (structural), behawioralne (behavioral)
4. UML - diagram klas, związki: dziedziczenie (inheritance),
   kompozycja (composition), agregacja (aggregation), zależność
   (dependency)
5. Zasada S - Single Responsibility Principle (SRP): klasa ma jeden
   powód do zmiany
6. Zasada O - Open/Closed Principle (OCP): otwarta na rozszerzenie,
   zamknięta na modyfikację
7. Zasada L - Liskov Substitution Principle (LSP): podklasa zastępuje
   klasę bazową bez naruszenia poprawności
8. Zasada I - Interface Segregation Principle (ISP): wiele małych
   interfejsów lepiej niż jeden duży
9. Zasada D - Dependency Inversion Principle (DIP): zależność od
   abstrakcji, nie od konkretnych klas
10. Protokoły Pythona (`typing.Protocol`) jako alternatywa dla
    interfejsów - duck typing, structural subtyping

---

## Moduł 02 - Singleton

1. Problem: zapewnienie dokładnie jednej instancji klasy w całym systemie
2. Implementacja naiwna - atrybut klasy `_instance = None`
3. Metoda `__new__` - kontrola tworzenia obiektu przed `__init__`
4. Singleton bezpieczny wątkowo (thread-safe) - `threading.Lock`,
   podwójne sprawdzanie (double-checked locking)
5. Wzorzec Borg (monostate) - różne instancje, współdzielony `__dict__`
6. Moduł Pythona jako Singleton - idiom języka, gwarancja jednej
   instancji przez mechanizm importu
7. Zastosowania: konfiguracja aplikacji, połączenie z bazą danych,
   logger, pula zasobów
8. Singleton a testowalność - globalny stan, `_reset_instance()`,
   dependency injection, `unittest.mock.patch`

---

## Moduł 03 - Factory Method (Metoda Fabrykująca)

1. Problem: tworzenie obiektów bez znajomości konkretnej klasy -
   oddzielenie tworzenia od użycia
2. Uczestnicy: twórca (creator), konkretny twórca (concrete creator),
   produkt (product), konkretny produkt (concrete product)
3. Implementacja z metodą abstrakcyjną - `abc.ABC`, `@abstractmethod`
4. Implementacja z rejestrem fabryk - słownik mapujący klucz na klasę
5. `@classmethod` jako fabryka - alternatywny konstruktor
   (`from_string`, `from_dict`, `from_file`)
6. Zastosowania: parsery formatów danych (JSON/XML/CSV), serializacja,
   sterowniki baz danych, logowanie

---

## Moduł 04 - Abstract Factory (Fabryka Abstrakcyjna)

1. Problem: tworzenie rodzin powiązanych obiektów bez znajomości
   konkretnych klas
2. Uczestnicy: fabryka abstrakcyjna (abstract factory), konkretna
   fabryka (concrete factory), abstrakcyjny produkt (abstract product),
   konkretny produkt (concrete product)
3. Różnica między Factory Method a Abstract Factory -
   Factory Method: jeden produkt, Abstract Factory: rodzina produktów
4. Implementacja: hierarchia fabryk dziedziczących po `abc.ABC`
5. Przykład: motywy UI (jasny/ciemny) - przyciski, pola tekstowe,
   dialogi spójne wizualnie
6. Zastosowania: adaptery baz danych (SQL/NoSQL), zestawy widgetów,
   cross-platform UI

---

## Moduł 05 - Builder (Budowniczy)

1. Problem: budowanie złożonych obiektów krok po kroku - oddzielenie
   konstrukcji od reprezentacji
2. Uczestnicy: budowniczy (builder), dyrektor (director),
   produkt (product)
3. Fluent interface (interfejs płynny) - łańcuchowanie metod,
   każda metoda zwraca `self`
4. Builder z walidacją - sprawdzanie spójności i kompletności przed
   wywołaniem `build()`
5. `@dataclass` jako uproszczony builder - `field(default=...)`,
   `__post_init__` do walidacji
6. Zastosowania: budowanie zapytań SQL, konfiguracja połączeń sieciowych,
   konstruktory dokumentów (PDF, HTML)

---

## Moduł 06 - Prototype (Prototyp)

1. Problem: kopiowanie istniejących obiektów bez zależności od ich
   konkretnych klas
2. Płytka kopia (shallow copy) - moduł `copy`, `copy.copy()` -
   kopiuje obiekt, nie zagnieżdżone obiekty
3. Głęboka kopia (deep copy) - `copy.deepcopy()` - rekurencyjna kopia
   całego drzewa obiektów
4. Metody `__copy__` i `__deepcopy__` - kontrola zachowania kopiowania
5. Rejestr prototypów (prototype registry) - słownik przechowujący
   gotowe szablony
6. Zastosowania: klonowanie konfiguracji, obiekty gry (postacie, tereny),
   szablony dokumentów

---

## Moduł 07 - Adapter

1. Problem: niezgodność interfejsów dwóch klas - stary/nowy kod,
   biblioteki zewnętrzne
2. Adapter obiektowy (object adapter) - kompozycja, preferowany w
   Pythonie
3. Adapter klasowy (class adapter) - wielodziedziczenie
4. `__getattr__` jako adapter dynamiczny - przekazywanie atrybutów do
   opakowanego obiektu
5. Różnica: Adapter (zmiana interfejsu) vs. Facade (uproszczenie) vs.
   Proxy (kontrola dostępu)
6. Zastosowania: integracja bibliotek zewnętrznych, konwersja formatów
   danych, stary kod (legacy)

---

## Moduł 08 - Decorator (Dekorator)

1. Problem: dodawanie nowego zachowania bez modyfikacji klasy i bez
   eksplozji hierarchii dziedziczenia
2. Dekorator obiektowy (klasyczny GoF) - owijanie obiektu (wrapping),
   delegacja przez `self._component`
3. Dekorator Pythona (`@`) - funkcja wyższego rzędu, `functools.wraps`
   do zachowania metadanych
4. Dekoratory parametryzowane - fabryka dekoratorów (trzy poziomy
   zagnieżdżenia)
5. Klasa z `__call__` jako dekorator - czytelniejsza alternatywa dla
   fabryki funkcji
6. Dekoratory z biblioteki standardowej: `functools.lru_cache`,
   `functools.cache`, `functools.singledispatch`,
   `contextlib.contextmanager`
7. Zastosowania: logowanie (logging), pomiar czasu (timing), retry,
   uwierzytelnianie, cache'owanie

---

## Moduł 09 - Facade (Fasada)

1. Problem: uproszczenie złożonego podsystemu - jeden punkt wejścia
   zamiast wielu klas
2. Fasada jako punkt wejścia - ukrywanie złożoności, zmniejszenie
   liczby zależności klienta
3. Implementacja: metody fasady delegują do klas podsystemu
4. Wielokrotne fasady - fasada wyższego poziomu na fasadzie
5. Różnica: Facade (uproszczenie) vs. Adapter (zmiana interfejsu) vs.
   Mediator (koordynacja)
6. Zastosowania: API biblioteki, warstwa dostępu do danych (DAO),
   serwis aplikacji (Application Service)

---

## Moduł 10 - Proxy (Pełnomocnik)

1. Problem: kontrola dostępu do obiektu - opóźnienie tworzenia,
   uprawnienia, cache, zdalny dostęp
2. Rodzaje proxy: wirtualne (virtual/lazy loading), ochronne (protection),
   zdalne (remote), cache'ujące (caching), logujące (logging)
3. Implementacja z `__getattr__` - przechwytywanie dostępu do atrybutów
4. `weakref.proxy` - proxy ze słabą referencją (nie blokuje garbage
   collection)
5. Różnica: Proxy (ten sam interfejs, kontrola) vs. Decorator
   (rozszerzanie zachowania)
6. Zastosowania: leniwe ładowanie danych z bazy, logowanie dostępu,
   sprawdzanie uprawnień

---

## Moduł 11 - Composite (Kompozyt)

1. Problem: traktowanie obiektów i ich grup (drzew) jednakowo -
   jeden interfejs dla liścia i kompozytu
2. Uczestnicy: komponent (component), liść (leaf), kompozyt (composite)
3. Rekurencja jako rdzeń wzorca - operacje na kompozycie wywołują
   operacje na dzieciach
4. Implementacja: drzewo plików i katalogów
5. Kiedy używać: drzewa, hierarchie, struktury rekurencyjne
6. Zastosowania: systemy plików, drzewa wyrażeń matematycznych, menu
   aplikacji, drzewa DOM

---

## Moduł 12 - Bridge (Most)

1. Problem: oddzielenie abstrakcji (abstraction) od implementacji
   (implementation) - zmiana niezależna po obu stronach
2. Uczestnicy: abstrakcja (abstraction), rozszerzona abstrakcja
   (refined abstraction), implementator (implementor),
   konkretny implementator (concrete implementor)
3. Różnica: Bridge (oddzielenie od początku) vs. Adapter (naprawienie
   niezgodności po fakcie)
4. Implementacja z kompozycją - abstrakcja trzyma referencję do
   implementatora
5. Zastosowania: sterowniki urządzeń, widoki i formaty danych,
   cross-platform UI, systemy renderowania

---

## Moduł 13 - Observer (Obserwator)

1. Problem: powiadamianie wielu obiektów o zmianach stanu innego
   obiektu - bez twardych zależności
2. Uczestnicy: podmiot (subject/observable), obserwator (observer),
   zdarzenie (event)
3. Implementacja: lista obserwatorów, metody `subscribe`,
   `unsubscribe`, `notify`
4. Callable jako obserwator - funkcje i lambdy zamiast klas,
   `typing.Callable`
5. Zdarzenia jako obiekty - `@dataclass Event` z polem `type`,
   rejestracja handlerów per typ zdarzenia
6. `weakref.WeakSet` - słabe referencje zapobiegające wyciekom pamięci
7. Zastosowania: GUI (event loop), systemy powiadomień,
   reaktywne strumienie danych, moduł `logging` (Handler jako Observer)

---

## Moduł 14 - Strategy (Strategia)

1. Problem: warunki `if/elif` zamiast algorytmów - naruszenie OCP przy
   dodawaniu nowych wariantów
2. Uczestnicy: kontekst (context), strategia (strategy), konkretna
   strategia (concrete strategy)
3. Strategia jako klasa - `abc.ABC`, `@abstractmethod`
4. Strategia jako funkcja - funkcje jako obiekty pierwszej klasy,
   `sorted(key=)` jako wbudowana strategia
5. Rejestr strategii - słownik mapujący nazwę na callable
6. Strategia parametryzowana - closure lub klasa z `__init__` i
   `__call__`
7. Zastosowania: sortowanie (key=), walidacja formularzy, algorytmy
   płatności, kompresja danych, routing

---

## Moduł 15 - Command (Polecenie)

1. Problem: enkapsulacja żądania jako obiektu - parametryzacja
   odbiorcy, kolejkowanie, logowanie, cofanie
2. Uczestnicy: polecenie (command), konkretne polecenie
   (concrete command), nadawca (invoker), odbiorca (receiver)
3. Interfejs polecenia: metody `execute()` i `undo()`
4. Historia poleceń - stos cofania (undo stack), lista `deque`
5. Kolejka poleceń - `queue.Queue`, asynchroniczne przetwarzanie
6. Polecenie jako funkcja - callable, `functools.partial`
7. Zastosowania: edytory tekstu (undo/redo), systemy transakcji,
   harmonogramowanie zadań (task scheduler), makra

---

## Moduł 16 - Template Method (Metoda Szablonowa)

1. Problem: szkielet algorytmu z krokami do nadpisania - powtarzający
   się kod w podklasach
2. Metoda szablonowa (template method) - `final` w bazie, abstrakcyjne
   metody w podklasach
3. Metody "hak" (hook methods) - opcjonalne nadpisanie, domyślna
   implementacja w bazie
4. Różnica: Template Method (dziedziczenie) vs. Strategy (kompozycja)
5. Zastosowania: parsery plików (CSV/JSON/XML), procesy ETL,
   walidatory formularzy, testy jednostkowe (`setUp`/`tearDown`)

---

## Moduł 17 - State (Stan)

1. Problem: zachowanie obiektu zmienia się wraz ze stanem - wielkie
   `if/elif` zależne od flagi stanu
2. Maszyna stanów (state machine, FSM) - stany, przejścia, wyzwalacze
3. Uczestnicy: kontekst (context), stan (state), konkretny stan
   (concrete state)
4. Implementacja z klasami stanów - każdy stan hermetyzuje zachowanie
5. Przejścia stanów - stan zmienia stan kontekstu (`context.state = NewState()`)
6. Różnica: State (zachowanie zależne od stanu) vs. Strategy
   (wymienne algorytmy)
7. Zastosowania: automaty biletowe, sesje użytkownika, protokoły
   sieciowe, stany zamówień e-commerce

---

## Moduł 18 - Iterator (Iterator)

1. Problem: sekwencyjny dostęp do elementów kolekcji bez ujawniania
   jej struktury wewnętrznej
2. Protokół iteratora w Pythonie - `__iter__` (zwraca self),
   `__next__` (następny element), `StopIteration`
3. Iterowalny (iterable) vs. iterator - `__iter__` bez `__next__`
   vs. oba
4. Generatory (`yield`) - pythonowy idiom iteratora, leniwe obliczanie
5. Generator expressions - `(x**2 for x in range(10))`
6. Moduł `itertools` - `chain`, `islice`, `groupby`, `product`,
   `combinations`, `permutations`
7. Zastosowania: drzewiaste struktury danych (pre/in/post-order),
   leniwe ładowanie (pagination), strumienie danych, przetwarzanie
   plików linia po linii

---

## Moduł 19 - Chain of Responsibility (Lancuch Odpowiedzialnosci)

1. Problem: przekazywanie żądania przez łańcuch obiektów - każdy
   decyduje czy obsłużyć, czy przekazać dalej
2. Uczestnicy: obsługujący (handler), konkretny obsługujący
   (concrete handler), żądanie (request)
3. Implementacja klasyczna - każdy handler trzyma referencję do
   następnego (`next_handler`)
4. Implementacja funkcyjna - lista callable, pętla lub rekurencja
5. Middleware HTTP jako łańcuch - każdy middleware może przerwać
   lub przekazać żądanie
6. Zastosowania: filtry logów (log levels), walidacja danych
   (pipeline walidatorów), autoryzacja (role chain),
   przetwarzanie żądań HTTP

---

## Moduł 20 - Mediator (Mediator)

1. Problem: zbyt wiele bezpośrednich zależności między obiektami -
   "spaghetti" komunikacji
2. Uczestnicy: mediator, kolega (colleague)
3. Mediator jako centralny punkt komunikacji - obiekty nie rozmawiają
   bezpośrednio, tylko przez mediatora
4. Implementacja: `notify(sender, event)` w mediatorze,
   rejestracja kolegów
5. Różnica: Mediator (centralizacja) vs. Observer (broadcast) vs.
   Facade (uproszczenie dla klienta)
6. Zastosowania: czaty grupowe, systemy rezerwacji (hotel, lot),
   kontrolery w MVC, koordynacja widgetów UI
