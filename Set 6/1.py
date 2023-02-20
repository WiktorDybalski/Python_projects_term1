# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje
# wszystkie co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co
# najmniej jednej cyfry.

import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    x = 5
    while x <= int(math.sqrt(num)):
        if num % x == 0:
            return False
        x += 2
        if num % x == 0:
            return False
        x += 4
    return True


# 128176
def int_to_list(num):
    l = math.floor((math.log10(num))) + 1
    tab = [0] * l
    for i in range(0, l):
        liczba = num % 10
        tab[l - i - 1] = liczba
        num //= 10
    return tab


def rek(num, i=0, l=0, liczba=0):
    tab = int_to_list(num)
    n = len(tab)
    if i == n:
        if is_prime(liczba):
            print(liczba, end=" ")

    else:
        return rek(num, i + 1, l + 1, liczba + tab[n - i - 1] * (10 ** l)) or rek(num, i + 1, l, liczba)


rek(12345)
print(is_prime(123))
