""" Contains functions commonly used in algorithms"""

import math
import random


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def num_len(n: int):
    if n == 0:
        return 1
    x = 0
    while n > 0:
        x += 1
        n //= 10
    return x


def digits_number(n: int):
    if n == 0: return 1
    digits_counter = 0
    while n > 0:
        n //= 10
        digits_counter += 1
    return digits_counter


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    x = 5
    while x < math.sqrt(n):
        if n % x == 0: return False
        x += 2
        if n % x == 0: return False
        x += 4
    return True


def fraction(n: int, d: int):
    n, d = reduce_fraction(n, d)
    print(n // d, end='')
    n = n % d
    if n > 0:
        print('.', end='')


def reduce_fraction(numerator: int, denominator: int):
    gcf_of_n_and_d = gcf(numerator, denominator)
    numerator, denominator = int(numerator / gcf_of_n_and_d), int(denominator / gcf_of_n_and_d)
    return numerator, denominator


def gcf(a: int, b: int):
    """Greatest common factor"""
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


def permutation(arr: list, pos=0):
    if pos == len(arr):
        print(arr)
    else:
        for i in range(pos, len(arr)):
            arr[i], arr[pos] = arr[pos], arr[i]
            permutation(arr, pos + 1)
            arr[i], arr[pos] = arr[pos], arr[i]


def suma_podzielnikow(n):
    i = 2
    suma = 1

    while i * i < n:
        if n % i == 0:
            suma += i + n // i
        i += 1
    print(suma)


def czy_pierwsza(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    x = 5
    while x < math.sqrt(n):
        if n % x == 0: return False
        x += 2
        if n % x == 0: return False
        x += 4
    return True


""" Contains functions commonly used in algorithms"""

import math


def num_len(n: int):
    if n == 0:
        return 1
    x = 0
    while n > 0:
        x += 1
        n //= 10
    return x


def digits_number(n: int):
    if n == 0: return 1
    digits_counter = 0
    while n > 0:
        n //= 10
        digits_counter += 1
    return digits_counter


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    x = 5
    while x < math.sqrt(n):
        if n % x == 0: return False
        x += 2
        if n % x == 0: return False
        x += 4
    return True


def fraction(n: int, d: int):
    n, d = reduce_fraction(n, d)
    print(n // d, end='')
    n = n % d
    if n > 0:
        print('.', end='')


def reduce_fraction(numerator: int, denominator: int):
    gcf_of_n_and_d = gcf(numerator, denominator)
    numerator, denominator = int(numerator / gcf_of_n_and_d), int(denominator / gcf_of_n_and_d)
    return numerator, denominator


def gcf(a: int, b: int):
    """Greatest common factor"""
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


def nwd(a: int, b: int):
    """Greatest common factor"""
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


def permutation(arr: list, pos=0):
    if pos == len(arr):
        print(arr)
    else:
        for i in range(pos, len(arr)):
            arr[i], arr[pos] = arr[pos], arr[i]
            permutation(arr, pos + 1)
            arr[i], arr[pos] = arr[pos], arr[i]


def prime_factors(n):
    k = 2
    while n != 1:
        while n % k == 0:
            print(k)
            n //= k
        k += 1


def stirling_2(n: int, k: int):
    if n == k or k == 1:
        return 1
    if k == 0 or k > n:
        return 0

    return stirling_2(n - 1, k - 1) + k * stirling_2(n - 1, k)


def bell_number(n: int):
    b_n = 0
    for k in range(1, n + 1):
        b_n += stirling_2(n, k)
    return b_n


def czy_da_sie_odwazyc(waga: int, i: int = 0):
    odwazniki = [1, 3, 5, 10, 16, 24]
    if waga == 0:
        return True
    if i == len(odwazniki) or waga < 0:
        return False
    # print(f'czy_da_sie_odwazyc({waga-odwazniki[i]},{i+1})')
    return czy_da_sie_odwazyc(waga - odwazniki[i], i + 1) or czy_da_sie_odwazyc(waga, i + 1)


# for i in range(1,50):
#     print(i,czy_da_sie_odwazyc(i))

def licz_trojki(tab, iloczyn):
    licz = 0
    for i in range(len(tab)):
        for j in range(i + 1, len(tab)):
            for k in range(j + 1, len(tab)):
                if tab[i] * tab[j] * tab[k] == iloczyn:
                    licz += 1
                    print(f"tab[{i}]={tab[i]},tab[{j}]={tab[j]},tab[{k}]={tab[k]}")
    print('trojki', licz)


def print_Tab(t):
    for i in range(len(t)):
        print(t[i])


def linked_print_all(p):
    while p is not None:
        print(p.val, end=" => ")
        p = p.next
    print("")


def linked_print_all_with_guardian(p):
    while p.next is not None:
        print(p.next.val, end=" => ")
        p = p.next
    print("")


def linked_insert_at_the_end(g, val):
    cur = g
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(val)


def create_linked_list(T):
    if len(T) > 0:
        g = Node(T[0])
        for i in range(1, len(T)):
            linked_insert_at_the_end(g, T[i])
    return g


# licz_trojki([random.randint(1,20) for i in range(100)],24)

if __name__ == "__main__":
    suma_podzielnikow(20)
