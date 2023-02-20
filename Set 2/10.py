# Zadanie 10. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz
# jest równy 2.
# DONE

import math


def func():
    n = int(input("n = "))
    An = 2

    while An < int(math.sqrt(n)):
        if n % An == 0:
            return True
        An = 3 * An + 1
    return False


print(func())
