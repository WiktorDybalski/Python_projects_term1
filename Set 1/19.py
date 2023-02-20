# Zadanie 19. Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
# 1/2! + 1/3! + ...
# DONE

def factorial(x):
    sum = 1
    if x == 0:
        return 0
    for i in range(1, x + 1):
        sum *= i
    return sum


def number_euler():
    euler = 1
    old_euler = 2
    i = 1

    while abs(euler - old_euler) > 0.0000001:
        old_euler = euler
        euler = euler + 1 / factorial(i)
        i += 1
    return euler


print(number_euler())
