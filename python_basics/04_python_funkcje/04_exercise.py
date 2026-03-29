# 04_exercise.py — 004 Funkcje


# ─── Ćwiczenie 1 ──────────────────────────────────────────────────────────────
# Napisz funkcję fizz_buzz(n), która zwraca listę napisów dla liczb 1..n:
#   - "FizzBuzz" jeśli liczba dzieli się przez 3 i przez 5
#   - "Fizz"     jeśli dzieli się tylko przez 3
#   - "Buzz"     jeśli dzieli się tylko przez 5
#   - str(liczba) w pozostałych przypadkach
def fizz_buzz(n):
    pass


def test_fizz_buzz():
    assert fizz_buzz(1) == ["1"]
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(15)[-1] == "FizzBuzz"
    assert fizz_buzz(0) == []


# ─── Ćwiczenie 2 ──────────────────────────────────────────────────────────────
# Napisz funkcję flatten(nested), która spłaszcza listę zagnieżdżoną o dowolnej
# głębokości do jednej płaskiej listy.
# Przykład: flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
def flatten(nested):
    pass


def test_flatten():
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
    assert flatten([]) == []


# ─── Ćwiczenie 3 ──────────────────────────────────────────────────────────────
# Napisz funkcję make_counter(start=0), która zwraca funkcję wewnętrzną.
# Każde wywołanie zwróconej funkcji zwiększa licznik o 1 i zwraca jego wartość.
# Przykład:
#   counter = make_counter(10)
#   counter()  →  11
#   counter()  →  12
def make_counter(start=0):
    pass


def test_make_counter():
    c = make_counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3

    c2 = make_counter(10)
    assert c2() == 11
    assert c2() == 12
