# 22. Dana jestlista, który być może zakończona jest cyklem.
# Napisać funkcję, która sprawdza ten fakt.


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


def hasCycle(pointer):
    if pointer is None:
        return False
    else:
        fast = pointer
        slow = pointer
        if slow.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        while slow.next is not None and fast.next is not None and fast.next.next is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False


print(hasCycle(a))
