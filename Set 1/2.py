# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

def checker(a1, b1, year):
    while b1 <= year:
        a1, b1 = b1, a1 + b1
        if a1 == year:
            return True
    return False


def func():
    year = 2022
    curr_sum = 1
    while True:
        for a in range(curr_sum):
            b = curr_sum - a
            if checker(a, b, year):
                return a, b
        curr_sum += 1


print(func())
