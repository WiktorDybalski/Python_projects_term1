# Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
# 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
# od 1 do N włącznie.
#DONE
n = int(input("n = "))
counter = 0
x = y = z = 1

while z <= n:
    y = z
    while y <= n:
        x = y
        while x <= n:
            counter += 1
            x *= 5
        y *= 3
    z *= 2
print(counter)