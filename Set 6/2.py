# Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
T = [4, 6, 30, 26, 3, 210]


def czynniki(num):
    i = 2
    counter = 0
    flag = True
    while num != 1:
        while num % i == 0:
            num //= i
            if flag:
                counter += 1
                flag = False
        i += 1
        flag = True
    return counter


def czy_rowne(T):
    x = T[0]
    n = len(T)
    for i in range(n):
        if x != T[i]:
            return False
    return True


def int_to_waga(T):
    n = len(T)
    for i in range(n):
        T[i] = czynniki(T[i])
    return T


def rek(Twaga, T1, T2, T3, i=0):
    if i == len(Twaga):
        if not T1 or not T2 or not T3:
            return False

        return czy_rowne(T1) and czy_rowne(T2) and czy_rowne(T3)

    return rek(Twaga, T1 + [Twaga[i]], T2, T3, i + 1) or rek(Twaga, T1, T2 + [Twaga[i]], T3, i + 1) \
           or rek(Twaga, T1, T2, T3 + [Twaga[i]], i + 1)


def kon(Tab):
    T1 = T2 = T3 = []
    print(Tab)
    Tab = int_to_waga(Tab)
    print(Tab)
    return rek(Tab, T1, T2, T3)


print(kon(T))
