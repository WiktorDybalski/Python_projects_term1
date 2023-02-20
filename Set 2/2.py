# Zadanie 2 Napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
# ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
#DONE

def func():
    a = int(input("a = "))
    b = int(input("b = "))
    n = int(input("n = "))

    if a % b == 0:
        print(a // b)
    else:
        print(a // b,".", sep="",end="")
        a %= b
        while n > 0 and a > 0:
            a *= 10
            print(a // b,end="")
            a %= b
            n -= 1
func()










