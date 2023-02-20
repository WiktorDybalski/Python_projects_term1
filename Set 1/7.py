# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
# DONE
number = int(input("Number: "))


def fibbonaci():
    a = 0
    b = 1
    # rób pętle do momentu aż liczba będzie większa od b
    while number > a:
        a, b = b, a + b
        if a * b == number:
            print("YES", a, "*", b, "=", number)
            return
        elif a * b > number:
            print("NO")
            return


fibbonaci()
