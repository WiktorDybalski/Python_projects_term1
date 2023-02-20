# Zadanie 6. Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
# o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.
# DONE
from math import sqrt


def product_of(num):
    q = int(sqrt(num))
    p = q
    curr_n = p * q
    while curr_n != num:
        if curr_n > num:
            p -= 1
        elif curr_n < num:
            q += 1
        curr_n = p * q
    return p, q


num = int(input())

print(product_of(num))
