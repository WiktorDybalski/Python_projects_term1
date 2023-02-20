# Zadanie 1. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
# czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
# DONE
import math


def func():
    n = int(input("n = "))
    a = b = 1
    while a <= (math.sqrt(n)):
        if n % a == 0:
            x = n // a
            c, d = b, a + b
            while c <= x:
                if x == c:
                    return True
                c, d = d, c + d
        a, b = b, a + b
    return False


print("Czy liczba jest iloczynem dowolnych dwóch wyrazów ciągu? ", func())
