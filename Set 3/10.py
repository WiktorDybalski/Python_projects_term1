# Zadanie 10. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami
# naturalnym wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.
#DONE
N = int(input("N = "))
t = [0] * N
g = [0] * (N-1)

for i in range(N):
    el = int(input("el = "))
    t[i] = el

print(t)

for j in range(1, N):
    if j == N:
        break
    g[j-1] = t[j] - t[j-1]

counter = 0
m = 0
for k in range(1,N-1):
    if g[m] == g[k]:
        counter += 1
    else:
        m = k
print(counter + 2)