# Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.
#DONE
n = 9
t = [[0] * n for _ in range(n)];
for line in t:
    print(line)
print("---------------------------")
x = 1
a = 0
b = n - 1
while a <= b:
    for i in range(a, b):
        t[a][i] = x
        x += 1
    for j in range(a, b):
        t[j][b] = x
        x += 1
    for k in range(b, a, -1):
        t[b][k] = x
        x += 1
    for l in range(b, a, -1):
        t[l][a] = x
        x += 1
    a += 1
    b -= 1
if n % 2 != 0:
    t[n//2][n//2] = x
for line in t:
    print(line)
