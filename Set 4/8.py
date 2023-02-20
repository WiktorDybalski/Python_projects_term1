# Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół,
# liczącego co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić
# informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.

t = [[7, 1, 6, 2, 3, 3, 1],
     [17, 12, 2, 34, 3, 2, 1],
     [4, 2, 1, 4, 17, 13, 11],
     [74, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 6, 2, 16, 8],
     [34, 31, 39, 76, 7, 18, 32],
     [3, 6, 9, 13, 17, 28, 88]]
n = len(t)


def create_tab(tab):
    for line in tab:
        print(line)
    print("---------------")


create_tab(t)


def ciag(a, b, c):
    return b / a == c / a


def checker(t, n):
    curr_len = 1
    max_len = 0
    for i in range(n - 2):
        for j in range(n - 2):
            if (t[i + 1][j + 1] / t[i][j]) == (t[i + 2][j + 2] / t[i + 1][j + 1]):
                curr_len = 3
                if i + k > n - 1 or j + k > n - 1:
                    continue
                else:
                    for k in range(3, n - 2):
                        if (t[i + k + 1][j + k + 1] / t[i + k][j + k]) == (t[i + k][j + k] / t[i + k - 2][j + k - 2]):
                            curr_len + 1
    max_len = max(max_len, curr_len)
    return max_len
