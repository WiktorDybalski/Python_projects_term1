# Zadanie 10. Napisać program wyszukujący liczby doskonałe mniejsze od miliona.
#DONE

def func():
    number = 2
    while number < 1000000:
        a = 0
        sum = 0
        number += 1
        while number > a + 1: # Trzeba dodać do a 1 bo pętla wykonuje o jeden bieg za dużo (sprawdzić w debbugerze)
            a += 1
            if number % a == 0:
                sum += a
        if sum == number:
            print(number)
func()