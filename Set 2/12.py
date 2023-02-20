# Zadanie 12. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta zawiera cyfrę równą liczbie swoich cyfr.
# DONE

num = int(input("num = "))


def number_of_digits(num):
    counter = 0
    while num > 0:
        num //= 10
        counter += 1
    return counter


def checker(num):
    new_num = num
    while new_num > 0:
        if number_of_digits(num) == new_num % 10:
            return True
        new_num = new_num // 10
    return False


print(checker(num))
