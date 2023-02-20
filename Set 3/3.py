# Zadanie 3. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N
# metodą Sita Eratostenesa.
# DONE
n = 27


def sito(n):
    temp = [1] * (n + 1)

    for i in range(2, n + 1):
        for j in range(i + 1, n + 1):
            if j % i == 0:
                temp[j] = 0
    primes = []
    for i in range(2, n + 1):
        if temp[i] != 0:
            primes.append(i)
    return primes


print(sito(n))
