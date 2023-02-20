a = int(input("Number1 = "))
b = int(input("Number2 = "))
temp = 0

while b != 0:
    temp = b
    b = a % b
    a = temp
print(a)
