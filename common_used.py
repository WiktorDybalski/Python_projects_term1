import math
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    x = 5
    while x <= sqrt(n):
        if n % x == 0:
            return False
        x += 2
        if n % x == 0:
            return False
        x += 4
    return True


def NWD(x, y):
    while y > 0:
        temp = y
        y = x % y
        x = temp
    return x


def NWW(x, y):
    return x * y // NWD(x, y)


def is_fibb(num):
    a, b = 1, 1
    while num > a:
        a, b = b, a + b
    return num == a


print(is_fibb(13))


def zamiana(num, sys):
    n = math.floor(math.log(num, sys)) + 1
    temp = num
    multi = 1
    result = 0
    while temp > 0:
        digit = temp % sys
        temp //= sys
        result += digit * multi
        multi *= 10
    return result


print(zamiana(3, 2))


def zamianaT(num, sys):
    n = math.floor(math.log10(num)) + 1
    T = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        digit = num % sys
        T[i] = digit
        num //= sys
    return T


print(zamianaT(5, 2))


def NWD(a, b):
    temp = b
    b = a % b
    a = temp
    return a


def długosc(num):
    n = math.floor(math.log10(num)) + 1
    return n


print(długosc(124))
