# Zadanie 17. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję
# która zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest
# największa.

t = [[7, 1, 6, 2, 3, 3, 1],
     [17, 12, 2, 34, 3, 2, 1],
     [4, 2, 1, 4, 17, 13, 11],
     [74, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 6, 2, 16, 8],
     [34, 31, 39, 76, 7, 18, 32],
     [3, 6, 9, 13, 17, 28, 88]]
n = len(t)


def func(tab, n):
    sum = 0
    for x in range(n):
        for y in range(n):
            temp = t[x][y]
            if x == 0:
                if y == 0:
                    sum += t[0][1] + t[1][0] + t[1][1]
            # Dopisać warunek krańcowy
            sum += t[x - 1][y - 1] + t[x - 1][y] + t[x - 1][y + 1] + t[x][y - 1] + t[x][y + 1] + t[x + 1][y - 1] + \
                   t[x + 1][y] + t[x + 1][y + 1]
