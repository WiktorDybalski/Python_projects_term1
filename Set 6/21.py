# Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.

t = [[1, 1, 6, 2, 3, 3, 1],
     [1, 12, 2, 34, 3, 2, 1],
     [1, 2, 1, 4, 17, 13, 11],
     [1, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 6, 2, 16, 8],
     [1, 31, 39, 76, 7, 18, 32],
     [1, 6, 9, 13, 17, 28, 88]]
x = w * N + k
sum = 24


def is_possible(w1, k1, w2, k2):
    return True if (w1 != w2 and k1 != k2) else False


def suma(digits):
    x = 0
    for i in range(len(digits)):
        x += digits[i]
    return x


def func(t, p, digits, sum):
    n = len(t)

    if p == n - 1:
        return
    if t[i][p] > sum:
        return False
    for i in range(n * n):
        p = i + 1
        w1 = i // n
        k1 = i % n
        w2 = p // n
        k2 = p % n
        func(t, p + 1, digits, sum) or func(t, p + 1, digits + [t[p]], sum)


digits = [0] * len(t)

func(t, 0, digits, sum)
