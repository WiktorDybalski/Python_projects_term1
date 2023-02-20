# Zadanie 13. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba zakończona jest unikalną cyfrą
# DONE

number = int(input("number = "))


def checker(number):
    unique = number % 10
    number //= 10
    while number > 0:
        if unique == number % 10:
            return False
        number //= 10
    return True


print(checker(number))
