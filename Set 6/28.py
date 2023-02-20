# Zadanie 28. Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję, która zwraca
# informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym podzbiorze, łączna liczba
# jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była jednakowa. Na przykład:
# [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek, [5, 7, 15] → false, podział nie
# istnieje.
T = [5, 7, 15]
T1 = []
T2 = []
T3 = []


def amount_of_1(t):
    n = len(t)
    count = 0
    for i in range(n):
        temp = t[i]
        while temp != 0:
            if temp % 2 != 0:
                count += 1
                temp //= 2
            else:
                temp //= 2
        t[i] = count
        count = 0
    return t


def sum_of_1(t):
    n = len(t)
    suma = 0
    for i in range(n):
        suma += t[i]
    return suma


def rek(T, T1, T2, T3, i=0):
    n = len(T)

    if n == i:
        if T1 and T2 and T3:
            if sum_of_1(T1) == sum_of_1(T2) == sum_of_1(T3):
                print('TUTAJ',T1, T2, T3)
                return True
            else:
                return False
        return False
    else:
        return rek(T, T1 + [T[i]], T2, T3, i + 1) or rek(T, T1, T2 + [T[i]], T3, i + 1) \
               or rek(T, T1, T2, T3 + [T[i]], i + 1)


Tj = amount_of_1(T).copy()
print('tj',Tj)
print(rek(Tj, T1, T2, T3, 0))


# [2,7] [3,5] [15]
# [1,3] [2,2] [3]