# Zadanie 4. Napisać program obliczający i wypisujący stałą e z rozwinięcia  w szereg
# e = 1/0! + 1/1! + 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
#DONE

n = int(input("n = "))
t = [1] + [0] * (n + 10)


def division(a, b, t):
    for i in range(1, len(t)):
        a *= 10
        t[i] += a // b
        a %= b
        if a == 0:
            return


def func(t, n):
    fact = 1
    k = 1

    while fact <= 10 ** (n + 1):
        fact *= k
        k += 1
        division(1, fact, t)

    for j in range(len(t) - 1, 0, -1):
        t[j - 1] += t[j] // 10
        t[j] %= 10

    print(str(t[0]) + ".", end="")
    for z in range(1, n + 1):
        print(t[z], end="")


func(t, n)
