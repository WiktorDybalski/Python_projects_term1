# Zadanie 2. Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
#DONE
a, b = input("Numbers: ").split()
digits = [0] * 10

for d in a:
    digits[int(d)] += 1
for d in b:
    digits[int(d)] -= 1

for i in range(10):
    if digits[i] != 0:
        print("NO")
        break
else:
    print("YES")

