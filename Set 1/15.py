# Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
# sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π.
# DONE

import math


def calc_pi(prec=10):
    pi = 2
    a = math.sqrt(0.5)
    for _ in range(prec):
        pi /= a
        a = math.sqrt(0.5 + 0.5 * a)
    return pi


print(calc_pi())
