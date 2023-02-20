# Zadanie 8. Napisać program sprawdzający czy zadana liczba jest pierwsza
# DONE
import math

number = int(input("Number: "))


def firts_numbers():
    a = 2
    while a <= math.sqrt(number):
        if number % a == 0:
            print("Not number first")
            return
        a += 1
    print("Number first")
    return


firts_numbers()
