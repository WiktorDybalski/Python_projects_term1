# Zadanie 10. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca
# wartość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz
# wartość False w przeciwnym przypadku.
#DONE
t = [[7, 1, 6, 2, 3, 3, 0],
     [17, 12, 2, 34, 3, 0, 1],
     [4, 2, 1, 4, 0, 13, 11],
     [74, 86, 7, 0, 8, 9, 12],
     [1, 3, 0, 6, 2, 16, 8],
     [34, 0, 39, 76, 7, 18, 32],
     [0, 6, 9, 13, 17, 28, 88]]
n = len(t)


def is_0_in_cols(t, n):
    counter_c = 0
    for j in range(n):
        for k in range(n):
            temp = t[k][j]
            if temp == 0:
                counter_c += 1
                break
    return counter_c == n


def is_0_in_rows(t, n):
    counter_r = 0
    for j in range(n):
        for k in range(n):
            temp = t[j][k]
            if temp == 0:
                counter_r += 1
                break
    return counter_r == n


if is_0_in_cols(t, n) and is_0_in_rows(t, n):
    print(True)
else:
    print(False)
