# Zadanie 24. Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru.


import math

T = [(13, 8), (3, 7), (3, 4), (8, 6), (1, 2), (6, 6), (1, 4), (2, 8)]
T1 = []
T2 = []


def srodek_ciezkosci(T):
    xS, yS = 0, 0
    n = len(T)
    for i in range(n):
        # print(T[i])
        xS += T[i][0]
        yS += T[i][1]

    xS /= n
    yS /= n
    return (xS, yS)


def fun(T):
    min_lenght = 10 ** 7

    def rek(T, T1=[], T2=[], i=0):
        nonlocal min_lenght
        n = len(T)
        if T1 and T2:
            if n == i:
                S1 = srodek_ciezkosci(T1)
                S2 = srodek_ciezkosci(T2)
                r = math.sqrt((S2[0] - S1[0]) ** 2 + (S2[1] - S1[1]) ** 2)
                min_lenght = min(min_lenght, r)
                print(min_lenght)

        else:
            if i < n:
                rek(T, T1 + [(T[i][0], T[i][1])], T2, i + 1)
                rek(T, T1, T2 + [(T[i][0], T[i][1])], i + 1)
                rek(T, T1, T2, i + 1)

    rek(T)
    return min_lenght


print(fun(T))
