# Zadanie 12. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.
# DONE NWD 3 liczb
a = int(input("Number1 = "))
b = int(input("Number2 = "))
c = int(input("Number3 = "))
temp1 = 0


def NWD2(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def NWD3(a, b, c):
    return NWD2(NWD2(a, b), c)


print(NWD3(a, b, c))
