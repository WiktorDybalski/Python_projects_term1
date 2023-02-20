# Zadanie 18. Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.

def newton_cube(num):
    b, c = 1, num
    while abs(c-b) > 0.0000000001:
        b = (b*2+c)/3
        c = num/b/b
    return b


print(newton_cube(int(input())))