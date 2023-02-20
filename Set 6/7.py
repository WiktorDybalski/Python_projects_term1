# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy.
# Odważniki można umieszczać tylko na jednej szalce

T = [6, 2, 4, 1]


def waga(T, i, r):
    n = len(T)
    if r == 0:
        return True
    if i == n:
        return False
    return waga(T, i + 1, r) or waga(T, i + 1, r - T[i])


print(waga(T, 0, 5))
