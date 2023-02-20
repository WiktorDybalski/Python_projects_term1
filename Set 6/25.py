# Zadanie 25. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola o indeksach
# i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję, która sprawdza, czy da się
# przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca -1.
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


def zad25(T):
    def rek(i, steps):
        if i == len(T) - 1:
            return steps
        min_steps = float("inf")
        for k in range(2, len(T) - i):
            if is_prime(k) and T[i] % k == 0 and k < T[i]:
                min_steps = min(min_steps, rek(i + k, steps + 1))
        return min_steps

    result = rek(0, 0)
    if result == float("inf"):
        return -1
    return result


print(zad25(T))
