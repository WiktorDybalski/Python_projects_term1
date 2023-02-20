# Zadanie 20. Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej
# cyfry. Proszę napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy
# systemu (w zakresie 2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę,
# jeżeli podstawa taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522
# odpowiedzią jest podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).
# DONE
x = int(input("x = "))
y = int(input("y = "))


def common_digit(x, y, s):
    D = [False] * s
    while x > 0:
        D[x % s] = True
        x //= s
    while y > 0:
        if D[y % s]:
            return True
        y //= s
    return False


for s in range(2, 17):
    if not common_digit(x, y, s):
        print(s)
        break
else:
    print("Nie ma")
