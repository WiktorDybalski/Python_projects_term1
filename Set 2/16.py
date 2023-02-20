# Zadanie 16. Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich
# liczb występujących w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5∗17, 8+5 = 5+1+7.
# Napisać program wypisujący liczby Smitha mniejsze od 1000000.
#DONE
import math

# Idę od 4 ponieważ 1,2 oraz 3 nie ma dzielników
for real_number in range(4, 1000):
    num1 = real_number
    num2 = real_number
    sum1 = 0
    sum2 = 0
# Liczymy sumę cyfr liczby
    while num1 > 0:
        sum1 += num1 % 10
        num1 //= 10
# Liczymy sumę dzielników
    i = 2
    while i <= (real_number/2):
        if num2 % i == 0:
            if i >= 10:
                j = i
                while j > 0:
                    sum2 += j % 10
                    j //= 10
                num2 //= i
            else:
                sum2 += i
                num2 //= i
        else:
            i += 1

    if sum1 == sum2:
        print(real_number)


