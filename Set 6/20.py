# Zadanie 20. Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej
# kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu.

from math import floor
from math import log10

t = [[33, 1, 6, 2, 3, 3, 16, 5],
     [22, 2, 6, 2, 3, 3, 16, 5],
     [33, 22, 1, 34, 3, 2, 1, 6],
     [44, 2, 31, 4, 17, 13, 11, 33],
     [55, 86, 7, 43, 8, 9, 12, 76],
     [66, 3, 2, 6, 52, 16, 8, 87],
     [77, 31, 39, 76, 7, 83, 32, 22],
     [88, 6, 9, 13, 17, 28, 88, 97]]


def get_first(num):
    n = floor(log10(num)) + 1
    return num // 10 ** (n - 1)


def get_last(num):
    return num % 10


# If possible row 00
def is_possible00(t, w, k, next_w, next_k):
    n = len(t)
    if n - 1 >= next_w >= 0 and n - 1 >= next_k >= 0 and n - 1 >= w >= 0 and n - 1 >= k >= 0:
        return True
    return False


def king00(t, w, k):
    if w == 0 and k == 0:
        print("Naroznik: ", (k, w))
        return

    moves = [(0, -1), (-1, 0), (-1, -1)]
    for move in moves:
        next_k = k + move[0]
        next_w = w + move[1]
        if is_possible00(t, w, k, next_w, next_k):
            if get_last(t[k][w]) < get_first(t[next_k][next_w]) and king00(t, next_k, next_w):
                return True
    return False


# If possible row 0n
def is_possible0n(t, w, k, next_w, next_k):
    n = len(t)
    if n - 1 >= next_w >= 0 and n - 1 >= next_k >= 0 and n - 1 >= w >= 0 and n - 1 >= k >= 0:
        return True
    return False


def king0n(t, w, k):
    n = len(t)
    if w == n - 1 and k == 0:
        print("Naroznik: ", (k, w))
        return True

    moves = [(0, 1), (-1, 0), (-1, 1)]
    for move in moves:
        next_k = k + move[0]
        next_w = w + move[1]
        if is_possible0n(t, w, k, next_w, next_k):
            if get_last(t[k][w]) < get_first(t[next_k][next_w]) and king0n(t, next_w, next_k):
                return True
    return False


# If possible row nn
def is_possiblenn(t, w, k, next_w, next_k):
    n = len(t)
    if n - 1 >= next_w >= 0 and n - 1 >= next_k >= 0 and n - 1 >= w >= 0 and n - 1 >= k >= 0:
        return True
    return False


def kingnn(t, w, k):
    n = len(t)
    if w == n - 1 and k == n - 1:
        print("Naroznik: ", (k, w))
        return True

    moves = [(0, 1), (1, 0), (1, 1)]
    for move in moves:
        next_k = k + move[0]
        next_w = w + move[1]
        if is_possiblenn(t, w, k, next_w, next_k):
            if get_last(t[k][w]) < get_first(t[next_k][next_w]) and kingnn(t, next_k, next_w):
                return True
    return False


# If possible row n0
def is_possiblen0(t, w, k, next_w, next_k):
    n = len(t)
    if n - 1 >= next_w >= 0 and n - 1 >= next_k >= 0 and n - 1 >= w >= 0 and n - 1 >= k >= 0:
        return True
    return False


def kingn0(t, w, k):
    n = len(t)
    if w == 0 and k == n - 1:
        print("Naroznik: ", (k, w))
        return

    moves = [(0, -1), (1, -1), (1, 0)]
    for move in moves:
        next_k = k + move[0]
        next_w = w + move[1]
        if is_possiblen0(t, w, k, next_w, next_k):
            if get_last(t[k][w]) < get_first(t[next_k][next_w]) and kingn0(t, next_w, next_k):
                return True
    return False


def func(t, w=2, k=2):
    king00(t, w, k)
    king0n(t, w, k)
    kingnn(t, w, k)
    kingn0(t, w, k)


print(func(t))
