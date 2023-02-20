# 23. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.

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
f = Node(19)
g = Node(19)
h = Node(19)
i = Node(19)


a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = d


def cycleLength(pointer):
    counter = 0
    fast = pointer
    slow = pointer
    while fast.next is not None or slow.next is not None:
        if fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
    else:
        return counter
    counter += 1
    if fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    while fast != slow:
        counter += 1
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
    return counter

print(cycleLength(a))





    