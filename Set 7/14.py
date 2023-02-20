# 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość dzieli bez reszty wartość bezpośrednio następujących po nich
# elementów.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end=" => ")
        p = p.next
    print("")


def length(a):
    counter = 0
    while a is not None:
        counter += 1
        a = a.next
    return counter


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


def cos_tam(h):
    curr = h
    while curr.next is not None:
        if curr.val % curr.next.val == 0:
            curr.next = curr.next.next
        curr = curr.next
    return h.next


print_all(cos_tam(h))
