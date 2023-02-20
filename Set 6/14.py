# Zadanie 14. Problem wież w Hanoi (treść oczywista)
counter = 0


def hanoi(n, poczatkowe, docelowe):
    global counter
    if n == 1:
        print("1: z", poczatkowe, "do", docelowe)
        counter += 1
    else:
        tymczasowe = 6 - docelowe - poczatkowe
        hanoi(n - 1, poczatkowe, tymczasowe)
        print("El", n, ": z", poczatkowe, "na", docelowe)
        counter += 1
        hanoi(n - 1, tymczasowe, docelowe)


hanoi(3, 1, 3)
print(counter)