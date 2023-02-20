# Zadanie 15. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję,\
# która odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej
# jedną cyfrę będącą liczbą pierwszą?
import math

t = [[7, 77, 53, 2, 3, 4, 37],
     [29, 29, 29, 29, 29, 29, 29],
     [4, 2, 1, 4, 17, 13, 11],
     [74, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 6, 2, 16, 8],
     [34, 31, 39, 76, 7, 18, 32],
     [3, 6, 9, 13, 17, 28, 88]]
n = len(t)


def is_first(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2
        if x % i == 0:
            return False
        i += 4
    return True


def checker(t, n):
    for i in range(n):
        counter = 0
        for j in range(n):
            temp = t[i][j]
            while temp > 0:
                if is_first(temp % 10):
                    counter += 1
                    break
                temp //= 10
        if counter == n:
            return counter == n
    return counter == n


print(checker(t, n))
