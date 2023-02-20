# Zadanie 12. Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.

from random import randint

nums = [0] * 100
n = 10
t = [randint(1, 10) for _ in range(n)]
counter = 0
print(t)


def licz_nki(t, n, p, x, nums):
    global counter
    if p == 1:
        for i in range(len(t)):
            if t[i] == n:
                print(nums)
                counter += 1
                nums += [t[i]]
                nums += [0]
                return True

    else:
        for j in range(x, len(t)):
            if n % t[j] == 0:
                if licz_nki(t, n // t[j], p - 1, x + 1, nums):
                    nums += [t[j]]
        return False


licz_nki(t, 4, 2, 0, nums)
print(counter)
