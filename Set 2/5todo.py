# Zadanie 5. Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma
# zera. Ile różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych
# cyfr w tej liczbie. Np. dla 2315 będą to 21, 35, 231, 315.
#!
import math


def get_leng(num):
    return math.floor(math.log10(num)) + 1


def create_number(org_num, mask):
    new_rev_num = 0
    while org_num > 0:
        # print(org_num)
        # print(mask, new_rev_num)
        if mask % 2 == 1:
            new_rev_num *= 10
            new_rev_num += org_num % 10
        mask //= 2
        org_num //= 10

    new_num = 0
    while new_rev_num > 0:
        new_num *= 10
        new_num += new_rev_num % 10
        new_rev_num //= 10

    return new_num


n = int(input())

counter = 0
for i in range(1, 2 ** get_leng(n)):
    if create_number(n, i) % 7 == 0:
        counter += 1

print(counter)