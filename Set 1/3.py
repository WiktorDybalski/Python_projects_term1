# DONE
# Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
# sumie.


def func():
    sum_to_find = int(input("Sum = "))
    sum = 1
    larg = 1
    sec_larg = 0
    small = 1
    sec_small = 1

    while small < sum_to_find:
        sec_larg, larg = larg, sec_larg + larg
        sum += larg
        if sum == sum_to_find:
            return True
        while sum > sum_to_find:
            sum -= small
            small, sec_small = sec_small, sec_small + small
            if sum == sum_to_find:
                return True
    return False

print(func())