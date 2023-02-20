# Zadanie 6. Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru. Na przykład dla tablicy:
# [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

T = [1, 7, 3, 5, 11, 2]
value = []
index = []


def equals(T, value, index):
    n = len(value)
    sum_of_index = 0
    sum_of_values = 0
    for i in range(n):
        sum_of_values += value[i]
        sum_of_index += index[i]
    return sum_of_index == sum_of_values


def search(T, i, value, index):
    n = len(T)
    if i == n:
        if equals(T, value, index):
            print(value)
            return
        return

    iterator = i
    return search(T, i + 1, value + [T[iterator]], index + [iterator]) or search(T, i + 1, value, index)


search(T, 0, value, index)
