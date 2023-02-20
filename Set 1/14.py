# Zadanie 14. Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina
# DONE
from math import factorial


def szereg_Maclaurina(x, nmax):
    n = 2
    s = 0
    s1 = 0
    s2 = 0
    for n in range(2, nmax):
        s1 = s1 + (x ** n) / (factorial(n))
        s2 = s2 + (x ** (n + 2)) / (factorial(n + 2))
        n += 4
    s = 1 - s1 + s2
    return s


print(szereg_Maclaurina((3.14), 100))

# s = 0
#     for i in range(dok):
#         s += ((-1)**i)*(x**(2*i))/factorial(2*i)
#     return s
#
#
# print(szereg_Maclaurina(3.14/4))
