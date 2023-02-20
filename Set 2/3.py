# Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
#DONE
num = int(input())

rev_num = 0
num_copy = num
while num_copy > 0:
    rev_num = rev_num*10 + num_copy%10
    num_copy //= 10

print(rev_num == num)


# binary
num = int(input())

rev_num = 0
num_copy = num
while num_copy > 0:
    rev_num = rev_num*2 + num_copy%2
    num_copy //= 2

print(rev_num == num)