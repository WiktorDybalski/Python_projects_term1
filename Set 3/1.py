# Zadanie 1. Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.
#DONE
n = int(input(""))


def to_system(num, base):
    base_number = []
    chars = [str(i) for i in range(10)] + [chr(i) for i in range(ord("A"), ord("F") + 1)]

    while num > 0:
        base_number.append(chars[num % base])
        num //= base
    return "".join(base_number[::-1])


for i in range(2, 17):
    print("base", i, ":", to_system(n, i))
