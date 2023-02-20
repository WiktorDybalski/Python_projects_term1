# Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów elementów wszystkich
# niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć, że liczba podzielników pierwszych nie przekracza 20,
# zatem w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej.
# Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

def dzielniki(num):
    dzieln = set()
    x = 2
    while num != 1:
        while num % x == 0:
            num //= x
            dzieln.add(x)
        x += 1
    return list(dzieln)


def func(dzieln, p, il):
    return il if p == len(dzieln) else func(dzieln, p + 1, il) + func(dzieln, p + 1, il * dzieln[p])

def minus(num):
    return func(dzielniki(num), 0, 1) - 1

print(minus(30))
