# Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr.
# DONE
import math

t = [[6, 7, 1, 6, 2], [5, 8, 3, 1, 2], [9, 13, 34, 8, 9], [1, 7, 1, 8, 7], [1, 9, 43, 34, 87]]
print(t)


def checker(t):
    counter = 0
    for i in range(len(t)):
        for j in range(len(t)):
            temp = t[i][j]
            x = 3
            while x <= temp:
                while temp % x == 0:
                    temp //= x
                x += 2
            if temp == 1:
                counter += 1
                break
    if counter == 5:
        return True
    return False


print(checker(t))
