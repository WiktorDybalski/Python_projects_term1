# Zadanie 5. Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
# Done

a = float(input("Wpisz liczbę: "))


def sqrt(x):
    l = x / 2
    while abs(l - x / l) > 0.000001:
        l = float((l + x / l) / 2)
    return round(l, 6)


print(sqrt(a))
