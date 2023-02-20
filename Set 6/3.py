# Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt
# przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.

T = [[1, 1, 6, 2, 3, 3, 1],
     [1, 12, 2, 34, 3, 2, 1],
     [1, 2, 1, 4, 17, 13, 11],
     [1, 86, 7, 7, 8, 9, 12],
     [1, 3, 2, 6, 2, 16, 8],
     [1, 31, 39, 76, 7, 18, 32],
     [1, 6, 9, 13, 17, 28, 88]]


def krol(T, k, w=0):
    n = len(T)
    if w == n:
        return 0
    if k < 0 or k > n - 1:
        return 10 ** 10
    return min(krol(T, k - 1, w + 1), krol(T, k, w + 1), krol(T, k + 1, w + 1)) + T[w][k]


for line in T:
    print(line)
print("-------------------------------")
print(krol(T, 0))
