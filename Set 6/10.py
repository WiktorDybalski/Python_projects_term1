# Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)

T = [[1, 1, 6, 2],
     [1, 12, 2, 34],
     [1, 2, 1, 4],
     [1, 86, 7, 7]]

suma = 0


def przepisz(T, j, n):
    M = [[0]*n]*n
    for i in range(0,n):
        for y in range(0,n):
            if i !=0 and y != j:
                print(M)
                M[y][i] = T[y][i]
    return M
print(przepisz(T, 1, 4))

