# Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę
# napisać funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym
# wyłącznie z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
# DONE

t = [2, 7, 3, 5, 3, 7, 4, 6, 7]
n = len(t)


def func(t, n):
    longest = 0
    for x in range(n):
        for y in range(x + 1, n):
            flag = True
            for i in range(y - x + 1):
                if t[x + i] != t[y - i] or t[x + i] % 2 == 0:
                    flag = False
                    break
            if flag == True:
                longest = max(longest, y - x + 1)
    return longest


print(func(t, n))
