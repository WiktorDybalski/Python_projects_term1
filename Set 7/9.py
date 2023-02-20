# 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują kolejne cyfry.
# Proszę napisać funkcję zwiększającą taką liczbę o 1.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end="")
        p = p.next


g = Node(0)
b = Node(3)
c = Node(7)
d = Node(2)
e = Node(1)
g.next = b
b.next = c
c.next = d
d.next = e

print_all(g.next)
print("")


def increase_by_one(p):
    if p is None:
        return 0
    else:

        curr = p

        while curr.next is not None:
            curr = curr.next
        curr.val += 1
        return p


print_all(increase_by_one(g.next))
print("")
print_all(increase_by_one(g.next))
print("")
print_all(increase_by_one(g.next))
