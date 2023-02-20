# Zadanie 16. Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
# początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.
# DONE
def find_number():
    best_number = 0
    best_counter = 0
    for start_number in range(2, 10000):
        number = start_number
        counter = 0
        while abs(number - 1) > 0.00000001:
            number = (number % 2) * (3 * number + 1) + (1 - number % 2) * number / 2
            counter += 1
        if counter > best_counter:
            best_counter = counter
            best_number = start_number
    return best_number, best_counter


print(find_number())
