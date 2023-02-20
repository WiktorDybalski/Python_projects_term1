#Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy
# z liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n^2.
#DONE

liczba = int(input("Write number: "))

suma = 0
el = 1
i = 0

while suma < liczba:
    suma += el
    i += 1
   # Jesli suma = liczbie to zwykły pierwiastek
    if suma == liczba:
        print(i)
    # musi być taki przypadek żeby pierw z 15 dał jeszcze 3 a nie 4
    elif suma > liczba:
        print(i - 1)
    el += 2