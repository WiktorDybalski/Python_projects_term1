# Wzorcowy program sprawdzający czy dana liczba jest pierwsza
import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    x = 5
    while x <= int(math.sqrt(num)):
        if num % x == 0:
            return False
        x += 2
        if num % x == 0:
            return False
        x += 4
    return True
