# Zadanie 11. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość
# najdłuższego, spójnego podciągu geometrycznego.

T = [4, 1, 3, 7, 2, 4, 8, 16, 32]


def func(T):
    n = len(T)
    najw = 0
    for i in range(n - 2):
        q = T[i + 1] / T[i]
        counter = 2
        j = 1
        while (T[i + j + 1] / T[i + j]) == q and i + j + 1 <= n - 2:
            counter += 1
            j += 1
        if T[n - 1] / T[n - 2] == q:
            counter += 1
        najw = max(najw, counter)
    return najw


print(func(T))
