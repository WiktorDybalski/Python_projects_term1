# Zadanie 17. Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne.
# Z wartości w obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden
# element (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4]
# i t2 = [9,7,4,8] poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
# Proszę napisać funkcje generującą i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi.
# Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.

import math

t1 = [1, 3, 2, 4]
t2 = [9, 7, 4, 8]


def is_prime(sum):
    if sum < 2:
        return False

    if sum == 2 or sum == 3:
        return True

    if sum % 2 == 0 or sum % 3 == 0:
        return False
    x = 5
    while x <= int(math.sqrt(sum)):
        if sum % x == 0:
            return False
        x += 2
        if sum % x == 0:
            return False
        x += 4
    return True


def print_sums(t1, t2):
    n = len(t1)
    counter = 0
    masks = 3 ** n
    for mask in range(masks):
        decrypt = 3 ** (n - 1)
        sum = 0
        for i in range(n):
            if mask - 2 * decrypt >= 0:
                sum += t2[n - 1 - i]
                mask -= 2 * decrypt
            elif mask - decrypt == 0:
                sum += t1[n - 1 - i]
                mask -= decrypt
            else:
                sum += t1[n - 1 - i] + t2[n - 1 - i]
            decrypt //= 3
        if is_prime(sum):
            print("number: ", sum)
            counter += 1
    return counter


print(print_sums(t1, t2))
