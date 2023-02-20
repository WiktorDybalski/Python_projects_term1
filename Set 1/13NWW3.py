# Zadanie 13. Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.
# DONE
a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))


def NWD2(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def NWW2(a, b):
    return (a * b) // NWD2(a, b)


def NWW3(a, b, c):
    return NWW2(NWW2(a, b), c)


print(NWW3(a, b, c))
