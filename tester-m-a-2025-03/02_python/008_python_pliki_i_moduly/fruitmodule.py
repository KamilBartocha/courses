def lemon_number(l):
    print('Lemoniada nr', l)


def sum_two_numbers():
    """
    Read 2 numbers and returns sum
    """
    while True:
        x = input("Podaj pierwsza liczbe: ")
        y = input("Podaj druga liczbe: ")
        try:
            x2 = int(x)
            y2 = int(y)
        except Exception as e:
            print(f"Błąd konwersji: '{e}'. Podaj liczby całkowite")
        else:
            return x2 + y2
