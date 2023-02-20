# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym
# leży element do sumy elementów wiersza w którym leży element jest największa.
# DONE
t = [[6, 7, 1, 6, 2],
     [5, 8, 3, 1, 2],
     [9, 13, 34, 8, 9],
     [1, 7, 1, 8, 7],
     [19, 43, 34, 87, 1]]
n = len(t)


def col_and_rows(tab, n):
    col_sums = [0] * n
    row_sums = [0] * n
    for i in range(n):
        for j in range(n):
            col_sums[j] += tab[i][j]
            row_sums[i] += tab[i][j]
    print("col_sums =", col_sums)
    print("row_sums =", row_sums)

    max_col = col_sums[0]
    min_row = row_sums[0]

    for x in range(1, n):
        if col_sums[x] > col_sums[x - 1]:
            max_col = col_sums[x]

    for y in range(1, n):
        if row_sums[y] < row_sums[y - 1]:
            min_row = row_sums[y]
    index_max_col = col_sums.index(max_col)
    index_min_row = row_sums.index(min_row)

    print(index_min_row, index_max_col, max_col / min_row)


def print_t(tab):
    for line in tab:
        print(line)
    print("----------------")


print_t(t)
col_and_rows(t, n)
