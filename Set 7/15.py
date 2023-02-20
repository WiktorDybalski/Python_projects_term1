# 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end=" => ")
        p = p.next
    print("")


h = Node(0)
a = Node(15)
b = Node(30)
c = Node(2)
d = Node(6)
e = Node(19)

h.next = a
a.next = b
b.next = c
c.next = d
d.next = e

print_all(a)


def czy_usunac(value):
    temp = value
    counter1 = 0
    counter2 = 0

    while temp > 0:
        if temp % 3 == 1:
            counter1 += 1
            temp //= 3
        elif temp % 3 == 2:
            counter2 += 1
            temp //= 3
        else:
            temp //= 3
    print(counter1, counter2)
    print(value)
    return counter1 > counter2


def usun(h):
    curr = h
    while curr.next is not None:
        if czy_usunac(curr.next.val):
            curr.next = curr.next.next
            
        else:
            curr = curr.next
    return h.next


print_all(usun(h))
