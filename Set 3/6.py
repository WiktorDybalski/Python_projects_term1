# Zadanie 6. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi
# 1-1000 i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
#DONE
n = int(input("n = "))

t = [0] * n
for i in range(n):
    el = int(input("el = "))
    t[i] = el

for j in range(n):
    temp = t[j]
    while temp > 0:
        if ((temp % 10) % 2) == 0:
            print(False)
            exit()
        temp //= 10
print(True)
