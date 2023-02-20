# Zadanie 8. Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
# z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
# sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
#DONE

t = [6, 1, 5, 2, 4, 3, 9, 9, 1, 2, 4]
n = len(t)
print(t)


def checker(t):
    t2 = [False for _ in range(n)]
    t[0] = True

    for i in range(n):
        if t[i]:
            temp = t[i]
            k = 2
            while temp != 1:
                while temp % k == 0:
                    if i + k < n:
                        t2[i + k] = True
                    temp //= k
                k += 1
    return t2[n - 1]


print(checker(t))
