# Zadanie 19. Napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
# ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)
def find_expansion(a, b):
    digits = []
    modulo = []

    while a > 0:
        a *= 10
        digits.append(a // b)

        if not a in modulo:
            modulo.append(a)
        else:
            break

        #        print("a:", a)

        a %= b

    #        print("digits:", digits)
    #        print("modulo:", modulo)

    if a == 0:
        return "".join(map(str, digits))

    repeating_from = modulo.index(a)

    return "".join(map(str, digits[:repeating_from])) + "(" + "".join(map(str, digits[repeating_from:-1])) + ")"


a = int(input())
b = int(input())

print(a // b, "." if a % b != 0 else "", sep="", end="")
a %= b
# print()

print(find_expansion(a, b))