# Zadanie 7. Napisać program wypełniający N-elementową tablicę t liczbami pseudolosowymi
# z zakresu 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
#DONE
import random

N = int(input("N = "))
t = [0] * N
for i in range(N):
    el = random.randint(1, 1000)
    t[i] = el

print(t)

for j in range(N):
    temp = t[j]
    while temp > 0:
        if (temp % 10) % 2 == 0:
            print(False)
            exit()
print(True)
