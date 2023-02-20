# Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
# Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.


def print_split(num, j, split):
    if num == 0:
        print(split)
        return
    if j == 0:
        mini = 1
    else:
        mini = split[j - 1]
    for i in range(mini, num + 1):
        split[j] = i
        print_split(num - i, j + 1, split)
        split[j] = 0


num = 8

print_split(num, 0, [0] * num)
