# Zadanie 5. Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych
# zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10
# co do wielkości wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się
# wystarczająca liczba elementów.
#DONE
digits = []
n = 1

while n != 0:
    n = int(input("number = "))
    digits.append(n)
digits.sort()
i = 0
j = 1
while j < len(digits):
    if digits[i] == digits[j]:
            digits.remove(digits[j])
    else:
        j += 1
        i += 1
print(digits)
print(digits[9])



