# Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

def wypisz(T):
    for line in T:
        print(line)
    print("======================")


def czy_mozliwe(T, w, k):
    n = len(T)
    if 0 <= w <= n - 1 and 0 <= k <= n - 1:
        return True
    return False


def skoczek(T, w, k, l=1):
    T[w][k] = l
    n = len(T)
    if l == n * n:
        wypisz(T)
        return True
    skoki = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)]

    for skok in skoki:
        next_w = w + skok[0]
        next_k = k + skok[1]
        if czy_mozliwe(T, next_w, next_k):
            if T[next_w][next_k] == 0:
                if skoczek(T, next_w, next_k, l + 1):
                    return True

    T[w][k] = 0
    return False


n = 6
T = [[0] * n for _ in range(n)]
wypisz(T)

skoczek(T, 0, 0, 1)
