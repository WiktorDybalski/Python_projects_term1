# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.

T = [4, 6, 5, 2245, 634, 23, 42, 4, 6, 7, 2, 324]


# T = [4, 6, 5]


def main(T, k):
    T1 = []
    T2 = []

    print(rek(T, T1, T2, 0, k))


def rek(T, T1, T2, i, k):
    N = len(T)
    n1 = len(T1)
    n2 = len(T2)
    if i == N:
        if sum(T1) == sum(T2) and n1 + n2 == k:
            print(T1, T2, n1, n2)
            return True
        return False

    else:
        return rek(T, T1 + [T[i]], T2, i + 1, k) or rek(T, T1, T2 + [T[i]], i + 1, k) or rek(T, T1, T2, i + 1, k)


main(T, 3)
main(T, 4)
