# Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1,
# którego iloczyn 4 pól narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja
# powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka
# kwadratu.

t = [[1, 1, 6, 2, 6, 3, 1],
     [17, 12, 2, 34, 3, 2, 1],
     [4, 2, 1, 4, 17, 13, 11],
     [74, 86, 7, 7, 8, 9, 12],
     [3, 3, 2, 6, 1, 16, 1],
     [34, 31, 39, 76, 7, 18, 32],
     [3, 6, 9, 13, 3, 28, 6]]
n = len(t)
k = 18





def func(t, n, k):
    flag = False
    for i in range(n):
        for j in range(n):
            for l in range(3, n, 2):
                if l + i >= n + 1 or l + j >= n + 1:
                    break
                result = 0
                result = t[i][j] * t[i + l - 1][j] * t[i + l - 1][j + l - 1] * t[i][j + l - 1]
                if result == k:
                    x = t[i + (l // 2)][j + (l // 2)]
                    flag = True
                    print(l // 2, l // 2)

    if flag == False:
        print("Nie ma")


func(t, n, k)
