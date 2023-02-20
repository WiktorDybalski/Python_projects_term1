# Zadanie 27. Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
# napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
# na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.

def suma_2012(x1, x2, y1, y2):
    suma = 0
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            suma += j
    return suma
print(suma_2012(T[0], T[1], T[2], T[3]))



