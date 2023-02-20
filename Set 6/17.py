# Zadanie 17. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić
# wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, (17, 23, 2) itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
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


def func(num1, num2):
    def int_to_list(num):
        n = math.floor(math.log10(num)) + 1
        T = [0 for _ in range(n)]
        for i in range(n):
            liczba = num % 10
            T[i] = liczba
            num //= 10
        return T

    res = 0
    counter = 0
    T1 = int_to_list(num1)
    T2 = int_to_list(num2)
    liczby = set()

    def rek(T1, T2, res: int, i=0, I1=0, I2=0):
        # nonlocal counter
        n = len(T1) + len(T2)
        if I1 + I2 == n and res > 0:

            if is_prime(res):
                liczby.add(res)
                # counter += 1

        else:
            if I1 < len(T1):
                rek(T1, T2, res + T1[I1] * 10 ** i, i + 1, I1 + 1, I2)
                rek(T1, T2, res, i, I1 + 1, I2)
            if I2 < len(T2):
                rek(T1, T2, res + T2[I2] * 10 ** i, i + 1, I1, I2 + 1)
                rek(T1, T2, res, i, I1, I2 + 1)

    rek(T1, T2, res)
    return len(liczby)


print(func(123, 75))
