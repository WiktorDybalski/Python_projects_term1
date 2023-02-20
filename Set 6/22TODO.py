# Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.

from random import randint
from math import sqrt

t = [randint(1, 20) for _ in range(20)]
print(t)


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if (num % 2 == 0 and num % 3 == 0):
        return False
    x = 5
    while num <= int(sqrt(num)):
        if num % x == 0:
            return False
        x += 2
        if num % x == 0:
            return False
        x += 4
    return True


def is_possible(t, i, k):
    if k > t[i]:
        return False
    if is_prime(k) and t[i] % k == 0:
        return True
    return False


def check(t):
    leng = len(t)
    mark = [leng + 2] * leng
    mark[0] = 0

    for i in range(0, leng):
        if mark[i] > leng:
            continue

        for div in range(2, int(t[i] ** 0.5) + 2):
            if t[i] % div == 0:
                mark[i + div] = min(mark[i] + 1, mark[i + div])

                while t[i] % div == 0:
                    t[i] //= div

    # print(mark)
    return mark[-1] if mark[-1] <= leng else -1


arr = [6, 5, 1, 2, 4, 3, 7, 2, 6, 7]
print(check(arr))
