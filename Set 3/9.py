# Zadanie 9. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym
# wyznacza długość najdłuższego, spójnego podciągu rosnącego.
#DONE

N = int(input("N = "))
t = [0] * N
for i in range(N):
    el = int(input("el = "))
    t[i] = el

print(t)

counter = 0
for j in range(1, N):
    if t[j] > t[j - 1]:
        counter += 1
    else:
        if counter != 0:
            temp_counter = counter
            counter = 0
print(counter + 1)
