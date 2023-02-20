# Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki
T = [13, 10, 8, 3, 1]
stop = False


def func():
    def waga(T, i, r, w1, w2):
        # global stop
        n = len(T)

        # if stop:
        #     return False
        if r == 0:
            # stop = True
            return w1, w2
        if i == n:
            return False
        return waga(T, i + 1, r, w1, w2) or waga(T, i + 1, r - T[i], w1 + [T[i]], w2) or waga(T, i + 1, r + T[i], w1,
                                                                                              w2 + [T[i]])

    return waga(T, 0, 22, [], [])


print(func())
