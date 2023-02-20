# Zadanie 11. Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane
# są liczby są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona
# liczbami naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje
# wyłącznie z przyjaciółkami
#DONE

t = [[7, 1, 6, 2, 3, 3, 1],
     [17, 12, 2, 34, 3, 2, 1],
     [4, 2, 1, 4, 17, 13, 11],
     [74, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 366, 63, 16, 8],
     [34, 31, 39, 76, 7, 18, 32],
     [3, 6, 9, 137, 173, 28, 88]]
n = len(t)

for i in range(n):
    for j in range(1, n):
        temp1 = t[i][j-1]
        temp2 = t[i][j]
        tab1 = [False for _ in range(10)]
        tab2 = [False for z in range(10)]

        while temp1 > 0:
            x1 = temp1 % 10
            tab1[x1] = True
            temp1 //= 10

        while temp2 > 0:
            x2 = temp2 % 10
            tab2[x2] = True
            temp2 //= 10
        for k in range(len(tab1)):
            if tab1[k] != tab2[k]:
                break
        else:
            print(t[i][j-1], t[i][j])







