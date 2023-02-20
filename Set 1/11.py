# Zadanie 11. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.
# DONE


def suma(n):
    sum = 1
    i = 2
    while i * i < n:
        if n % i == 0:
            sum = (sum + i + n // i)
        if i * i == n:
            sum += i
        i += 1
    return sum


def checking_func():
    for m in range(1, 1000000):
        x = suma(m)
        if suma(x) == m and x < m:
            if x != m:
                print(x, m)


checking_func()
