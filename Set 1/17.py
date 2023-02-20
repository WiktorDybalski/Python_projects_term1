# Zadanie 17. Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
# ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.
# DONE

def golden_ratio():
    a = 1
    b = 1
    old_ratio = 1
    ratio = 0

    while abs(ratio - old_ratio) > 0.0000000001:
        a = b
        b = a + b

        old_ratio = ratio
        ratio = b / a
    return ratio


print(golden_ratio())
