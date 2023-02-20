# Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby.
# Na przykład waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca
# liczby naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3
# podzbiory o równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić
# wartość typu Bool.

T = [23, 23, 23, 42, 5, 4, 6, 2, 3]


def waga(num):
    temp = num
    counter = 0
    i = 2
    while temp != 1:
        flaga = False
        while temp % i == 0:
            flaga = True
            temp //= i
        if flaga:
            counter += 1
        i += 1
    return counter


def spr(t):
    suma = 0
    odw = [0] * len(t)
    for i in range(len(t)):
        odw[i] = waga(t[i])
        suma += odw[i]
    if suma % 3 == 0:
        if podzial(odw):
            return True
    else:
        return False


def podzial(t, n1=0, n2=0, n3=0, i=0):
    if i == len(t):
        return n1 == n2 and n2 == n3
    return podzial(t, n1 + t[i], n2, n3, i + 1) or podzial(t, n1, n2 + t[i], n3, i + 1) or podzial(t, n1, n2, n3 + t[i],
                                                                                                   i + 1)


print(spr(T))
