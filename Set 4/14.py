# Zadanie 16. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję
# która odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną
# wyłącznie z cyfr  będących liczbami pierwszymi?

import math

T = [[384776, 1, 6, 2, 3, 3, 1],
     [17, 12, 2, 34, 3, 2, 1],
     [4, 2, 1, 4, 17, 13, 11],
     [74, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 6, 2, 16, 8],
     [34, 31, 39, 76, 7, 18, 32],
     [3, 6, 9, 13, 17, 28, 88]]
n = len(T)


def primes(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    x = 5
    while x <= math.sqrt(num):
        if num % x == 0:
            return False
        x += 2
        if num % x == 0:
            return False
        x += 4
    return True


def func(T, n):
    counter = 0
    for i in range(n):
        flag = False
        for j in range(n):
            temp = T[i][j]
            length = int(math.log10(temp)) + 1
            M = 0
            while temp != 0:
                copy_temp = temp
                while copy_temp != 0:
                    if primes(copy_temp):
                        flag = True
                    copy_temp //= 10
                temp %= 10 ** (length - M)
                M += 1
        if flag:
            counter += 1
    if counter == n:
        return True
    return False


print(func(T, n))
