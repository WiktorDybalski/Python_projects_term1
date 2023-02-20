# Zadanie 14. Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego,
# że w grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku.
# Wyznaczyć wartości prawdopodobieństwa dla N z zakresu 20-40.
#DONE

from random import randint

m = int(input("m = "))
n = int(input("n = "))


def prob(m, n):
    year = [-1 for _ in range(366)]
    counter = 0

    for i in range(m):
        for j in range(n):
            birthday = randint(0, 365)
            if year[birthday] == i:
                counter += 1
                break
            year[birthday] = i
        year = [i for _ in range(366)]
    return counter / m


print(prob(m, n))
