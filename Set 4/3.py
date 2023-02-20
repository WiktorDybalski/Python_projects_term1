# Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera
# przynajmniej jedna cyfrę parzystą.
# DONE

t = [[6, 762, 261, 66, 62], [5, 8, 3, 1, 2], [9, 13, 34, 8, 9], [1, 7, 1, 8, 7], [1, 9, 43, 34, 87]]
n = len(t)


def checker(t, n):
    for i in range(n):
        counter = 0
        for j in range(n):
            flag = False
            temp = t[i][j]
            while temp > 0:
                if (temp % 10) % 2 == 0:
                    flag = True
                    break
                temp //= 10
            if flag:
                counter += 1
        if counter == 5:
            return True
    return False


print(checker(t, n))
