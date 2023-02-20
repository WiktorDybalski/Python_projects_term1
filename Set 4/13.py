# Zadanie 13. Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy
# nie posiadające liczby komplementarnej.

import math

T = [[1000000000, 1, 6, 2, 3, 3, 1],
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
            return True
        x += 4
    return True


def func(T, n):
    for line in T:
        print(line)
    print("---------------------------")

    for i in range(n):
        for j in range(n):
            a = T[i][j]
            flag = False
            for k in range(n):
                for l in range(n):
                    b = T[l][k]
                    if primes(a + b):
                        print(a, b)
                        flag = True
                        break
            if flag == False:
                T[i][j] = 0
    for line in T:
        print(line)
func(T,n)
