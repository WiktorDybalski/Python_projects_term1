# Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.

T = [13, 10, 8, 3, 1]


def waga(T, i, r):
    n = len(T)
    if r == 0:
        return True
    if i == n:
        return False
    return waga(T, i + 1, r) or waga(T, i + 1, r - T[i]) or waga(T, i + 1, r + T[i])

print(waga(T, 0, 20))
