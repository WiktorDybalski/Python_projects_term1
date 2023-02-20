# 24. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów przed cyklem.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next


a = Node(15)
b = Node(34)
c = Node(1)
d = Node(6)
e = Node(19)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c
