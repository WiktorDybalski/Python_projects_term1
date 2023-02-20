# Zadanie 5. Poprzednie zadanie z tablicą wypełnioną liczbami całkowitymi.

t = [[7, 1, 6, 2, 3, 3, 1],
     [17, 12, 2, 34, 3, 2, 1],
     [4, 2, 1, 4, 17, 13, 11],
     [74, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 6, 2, 16, 8],
     [34, 31, 39, 76, 7, 18, 32],
     [3, 6, 9, 13, 17, 28, 88]]
n = len(t)


def cols_and_rows(t, n):
    cols_sum = [0] * n
    rows_sum = [0] * n

    for i in range(n):
        for j in range(n):
            cols_sum[j] += t[i][j]
            rows_sum[i] += t[i][j]
    max_col = cols_sum[0]
    min_row = rows_sum[0]

    index_max_col = cols_sum.index([max_col])
    index_min_row = rows_sum.index([min_row])
