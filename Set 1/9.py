# Zadanie 9. Napisać program wypisujący podzielniki liczby.
# DONE
import math


def func(num):
    x = 1
    while x <= math.sqrt(num):
        if num % x == 0:
            print(x)
            print(num // x)

        x += 1


func(25)
