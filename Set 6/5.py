# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.
from math import sqrt

T = [1, 0, 1, 0, 1, 1]


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 and n % 3 == 0:
        return False
    x = 5
    while x <= sqrt(n):
        if n % x == 0:
            return False
        x += 2
        if n % x == 0:
            return False
        x += 4
    return True


def zadanie(T):
    num = 0
    n = len(T)
    if n == 1:
        return False
    for i in range(n):
        num += T[i] * (10 ** (n-i-1))
    if is_prime(num):
        return True
    else:
        for i in range(1,min(n,30)):
            if zadanie(T[:i]):
                return zadanie(T[i:])
    return False

zadanie(T)
