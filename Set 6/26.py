# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)

from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    x = 5
    while x <= int(sqrt(number)):
        if number % x == 0:
            return False
        x += 2
        if number % x == 0:
            return False
        x += 4
    return True


def rek(A, B, x):
    if A == 0 and B == 0:
        if not is_prime(x):
            print(x)
            return 1
        return 0
    a = 0
    b = 0
    if A > 0:
        a = rek(A - 1, B, x + 2 ** (A + B - 1))
    if B > 0:
        b = rek(A, B - 1, x)
    return a + b


def func(A,B):
    x = 2 ** (A + B - 1)
    return rek(A-1, B, x)


print(func(2,3))

