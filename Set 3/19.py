# Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]


def is_valid(n, product):
    if product % n:
        return False
    divisor = 2
    already_divided = False
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            if product % divisor == 0 or already_divided:
                return False
            already_divided = True
        else:
            divisor += 1
            already_divided = False
    return True


def func(t):
    i, j = 0, 0
    curr_len, max_len = 1, 1
    curr_product = t[0]
    while j != len(t) - 1:
        if is_valid(t[j + 1], curr_product):
            curr_product *= t[j + 1]
            j += 1
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        else:
            if curr_product == 1:
                i += 1
                j += 1
            else:
                curr_product //= t[i]
                i += 1
                curr_len -= 1
    return max_len


print(func(t))
