# Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
from random import randint

n = 10
t = [randint(1, 10) for _ in range(n)]
counter = 0
print(t)


def licz_nki(t, n, p, x):
    global counter
    if p == 1:
        for i in range(len(t)):
            if t[i] == n:
                counter += 1
                return

    else:
        for j in range(x, len(t)):
            if n % t[j] == 0:
                licz_nki(t, n // t[j], n - 1, x + 1)


licz_nki(t, 4, 2, 0)
print(counter)
