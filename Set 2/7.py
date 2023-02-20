# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.
#DONE
from math import sqrt
number = int(input("number = "))

for n in range(1, int(sqrt(number))):
    An = n ** 2 + n + 1
    if number % An == 0:
        print("YES")
        break
    else:
        print("NO")
        break


