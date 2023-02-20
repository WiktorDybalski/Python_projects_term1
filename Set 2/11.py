# Zadanie 11. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# jej cyfry stanowią ciąg rosnący.
# DONE
def func():
    n = int(input("n = "))
    a = n % 10
    n //= 10

    while n > 0:
        if a <= n % 10:
            return False
        a = n % 10
        n //= 10
    return True


print(func())
