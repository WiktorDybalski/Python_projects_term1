# Zadanie 15. Problem 8 Hetmanów (treść oczywista)
# Problem ośmiu hetmanów – problem polegający na wyznaczeniu liczby różnych rozmieszczeń ośmiu hetmanów na tradycyjnej
# szachownicy 8×8 tak, aby wzajemnie się nie atakowały. Przez rozstawienie bądź rozwiązanie podstawowe należy rozumieć
# takie z dokładnością do izomorfizmu, tzn. z uwzględnieniem wszystkich pokrewnych pozycji wynikających z odbić
# zwierciadlanych i obrotów.

def hetmany(N):
    T = [0] * N

    def rek(w):
        if w == N:
            print(T)
        else:
            for k in range(N):
                for i in range(w):
                    if T[i] == k or abs(T[i] - k) == w - i:
                        break
                else:
                    T[w] = k
                    rek(w + 1)

    rek(0)


hetmany(5)
