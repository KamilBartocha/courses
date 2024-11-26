# 1. Stwórz listę kwadratów liczb od 1 do 10.
squares = [x**2 for x in range(1, 11)]
print("1. Kwadraty liczb od 1 do 10:", squares)

# 2. Stwórz listę parzystych liczb od 0 do 20.
evens = [x for x in range(21) if x % 2 == 0]
print("2. Parzyste liczby od 0 do 20:", evens)

# 3. Zamień wszystkie litery w liście ['a', 'b', 'c', 'd'] na wielkie litery.
uppercase_letters = [x.upper() for x in ['a', 'b', 'c', 'd']]
print("3. Wielkie litery:", uppercase_letters)

# 4. Stwórz listę długości słów z listy ['apple', 'banana', 'cherry', 'date'].
word_lengths = [len(word) for word in ['apple', 'banana', 'cherry', 'date']]
print("4. Długości słów:", word_lengths)

# 5. Stwórz listę liczb podzielnych przez 3 z zakresu od 1 do 50.
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print("5. Liczby podzielne przez 3 od 1 do 50:", divisible_by_3)

# 6. Stwórz listę liczb będących iloczynem odpowiednich elementów z dwóch list: [1, 2, 3] i [4, 5, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
products = [x * y for x, y in zip(list1, list2)]
print("6. Iloczyny odpowiednich elementów:", products)

# 7. Zamień listę liczb [1, -2, 3, -4, 5] na ich wartości bezwzględne.
absolute_values = [abs(x) for x in [1, -2, 3, -4, 5]]
print("7. Wartości bezwzględne:", absolute_values)

# 8. Stwórz listę liczb od 1 do 100, ale zamień wszystkie liczby podzielne przez 5 na słowo "Buzz".
fizz_buzz = [x if x % 5 != 0 else 'Buzz' for x in range(1, 101)]
print("8. Liczby od 1 do 100 z 'Buzz':", fizz_buzz)

# 9. Filtruj tylko te słowa z listy ['dog', 'cat', 'rabbit', 'mouse'], które mają więcej niż 3 litery.
filtered_words = [word for word in ['dog', 'cat', 'rabbit', 'mouse'] if len(word) > 3]
print("9. Słowa mające więcej niż 3 litery:", filtered_words)

# 10. Stwórz listę tupli (liczba, jej kwadrat) dla liczb od 1 do 10.
number_squares = [(x, x**2) for x in range(1, 11)]
print("10. Tuples (liczba, kwadrat):", number_squares)

# 11. Stwórz listę liter z ciągu znaków "python" tylko dla tych, które są samogłoskami.
vowels = [char for char in "python" if char in 'aeiou']
print("11. Samogłoski z 'python':", vowels)

# 12. Stwórz listę liczb od 0 do 9 podniesionych do sześcianu, ale tylko dla tych liczb, które są nieparzyste.
cubes_of_odds = [x**3 for x in range(10) if x % 2 != 0]
print("12. Sześciany nieparzystych liczb od 0 do 9:", cubes_of_odds)

# 13. Stwórz listę liczb od 1 do 30, które są zarówno podzielne przez 3, jak i 5.
divisible_by_3_and_5 = [x for x in range(1, 31) if x % 3 == 0 and x % 5 == 0]
print("13. Liczby od 1 do 30 podzielne przez 3 i 5:", divisible_by_3_and_5)

# 14. Zamień wszystkie liczby ujemne z listy [-1, -2, 3, 4, -5] na 0, a dodatnie pozostaw bez zmian.
non_negative = [x if x >= 0 else 0 for x in [-1, -2, 3, 4, -5]]
print("14. Liczby nieujemne lub 0:", non_negative)

# 15. Stwórz listę liczb od 1 do 100, ale dla liczb podzielnych przez 3 podstaw "Fizz", a dla liczb podzielnych przez 5 "Buzz".
fizz_buzz_custom = ['Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, 101)]
print("15. Liczby od 1 do 100 z 'Fizz' i 'Buzz':", fizz_buzz_custom)

# 16. Utwórz listę pierwszych liter słów z listy ['Alice', 'Bob', 'Charlie', 'David'].
first_letters = [word[0] for word in ['Alice', 'Bob', 'Charlie', 'David']]
print("16. Pierwsze litery słów:", first_letters)

# 17. Stwórz listę wszystkich liczb od 1 do 100, które są liczbami pierwszymi.
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print("17. Liczby pierwsze od 1 do 100:", primes)

# 18. Utwórz listę odwrotnych postaci słów z listy ['hello', 'world', 'python'].
reversed_words = [word[::-1] for word in ['hello', 'world', 'python']]
print("18. Odwrotne postacie słów:", reversed_words)

# 19. Wygeneruj macierz kwadratową o rozmiarze 3x3 wypełnioną liczbami od 1 do 9.
matrix = [[x + y * 3 + 1 for x in range(3)] for y in range(3)]
print("19. Macierz 3x3:", matrix)

# 20. Utwórz listę liczb od 1 do 50, ale dla liczb podzielnych przez 2 zwróć "even", a dla pozostałych zwróć "odd".
even_odd = ['even' if x % 2 == 0 else 'odd' for x in range(1, 51)]
print("20. 'Even' i 'odd' dla liczb od 1 do 50:", even_odd)





# Ćwiczenia z Dictionary Comprehensions

# 1. Stwórz słownik, w którym klucze to liczby od 1 do 5, a wartości to ich kwadraty.
squares = {x: x**2 for x in range(1, 6)}
print("1. Kwadraty liczb od 1 do 5:", squares)

# 2. Stwórz słownik, w którym klucze to litery z napisu "hello" (unikalne litery), a wartości to liczba wystąpień każdej litery w tym napisie.
letter_count_hello = {char: 'hello'.count(char) for char in set('hello')}
print("2. Liczba wystąpień liter w 'hello':", letter_count_hello)

# 3. Stwórz słownik, w którym klucze to imiona z listy ['Alice', 'Bob', 'Charlie'], a wartości to długości tych imion.
name_lengths = {name: len(name) for name in ['Alice', 'Bob', 'Charlie']}
print("3. Długości imion:", name_lengths)

# 4. Stwórz słownik, w którym klucze to liczby od 1 do 5, a wartości to liczby podzielne przez 2.
even_values = {x: x if x % 2 == 0 else 0 for x in range(1, 6)}
print("4. Liczby podzielne przez 2 (lub 0):", even_values)

# 5. Stwórz słownik, w którym klucze to liczby od 1 do 10, a wartości to ich potęgi trzeciej.
cubes = {x: x**3 for x in range(1, 11)}
print("5. Potęgi trzecie liczb od 1 do 10:", cubes)

# 6. Stwórz słownik, w którym klucze to słowa z listy ['apple', 'banana', 'cherry'], a wartości to długości tych słów.
word_lengths = {word: len(word) for word in ['apple', 'banana', 'cherry']}
print("6. Długości słów:", word_lengths)

# 7. Stwórz słownik, w którym klucze to litery z napisu "world", a wartości to ich pozycje w alfabecie (a=1, b=2, itd.).
alphabet_positions = {char: ord(char) - ord('a') + 1 for char in 'world'}
print("7. Pozycje liter w alfabecie:", alphabet_positions)

# 8. Stwórz słownik, w którym klucze to liczby od 1 do 5, a wartości to ich liczby pierwsze (jeśli liczba jest pierwsza, to wartość jest równa kluczowi, w przeciwnym razie None).
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
prime_values = {x: (x if is_prime(x) else None) for x in range(1, 6)}
print("8. Liczby pierwsze (lub None):", prime_values)

# 9. Stwórz słownik, w którym klucze to litery z napisu "python", a wartości to liczby ich wystąpień w napisie.
letter_count_python = {char: 'python'.count(char) for char in 'python'}
print("9. Liczba wystąpień liter w 'python':", letter_count_python)



# Rozwiązania ćwiczeń z map() i filter()

# Ćwiczenia z map()

# Ćwiczenie 1
numbers = list(range(1, 11))
squared_numbers = map(lambda x: x ** 4, numbers)
print("Ćwiczenie 1:", list(squared_numbers))

# Ćwiczenie 2
words = ['hello', 'world', 'python']
word_lengths = map(len, words)
print("Ćwiczenie 2:", list(word_lengths))

# Ćwiczenie 3
import math
numbers = [10, 20, 30, 40, 50]
square_roots = map(math.sqrt, numbers)
print("Ćwiczenie 3:", list(square_roots))

# Ćwiczenie 4
numbers = [2, 4, 6, 8]
formatted_numbers = map(lambda x: f"Liczba: {x}", numbers)
print("Ćwiczenie 4:", list(formatted_numbers))

# Ćwiczenia z filter()

# Ćwiczenie 1
numbers = list(range(1, 21))
greater_than_ten = filter(lambda x: x > 10, numbers)
print("Ćwiczenie 1:", list(greater_than_ten))

# Ćwiczenie 2
words = ['cat', 'dog', 'elephant', 'fish']
contains_e = filter(lambda s: 'e' in s, words)
print("Ćwiczenie 2:", list(contains_e))

# Ćwiczenie 3
numbers = [12, 15, 22, 29, 35]
divisible_by_five = filter(lambda x: x % 5 == 0, numbers)
print("Ćwiczenie 3:", list(divisible_by_five))

# Ćwiczenie 4
words = ['apple', 'banana', 'cherry', 'date']
starts_with_b_or_c = filter(lambda s: s[0] in 'bc', words)
print("Ćwiczenie 4:", list(starts_with_b_or_c))
