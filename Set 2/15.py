# Zadanie 15. Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych
# potęg cyfr liczby jest równa tej liczbie, np. 153 = 1**3 + 5**3 + 3**3.
#DONE
N = int(input("N = "))

for real_number in range(1 * (10 ** (N-1)), 10 * (10 ** (N-1))):
    number = real_number
    sum = 0
    digit = 0
    while number > 0:
        digit = number % 10
        sum += (digit ** N)
        number //= 10
    if real_number == sum:
        print(real_number)











