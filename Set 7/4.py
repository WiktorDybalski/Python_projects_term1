# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next


def add(p, new_val):
    if p.next is None:
        q = Node(new_val)
        p.next = q
        return
    if p.next is not None:
        if p.next.val == new_val:
            return
        if p.next.val > new_val:
            q = Node(new_val)
            q.next = p.next
            p.next = q
            return
        else:
            add(p.next, new_val)


def reverse_rek(p):
    if p.next is None:
        return p
    else:
        prev = reverse_rek(p.next)
        q = prev
        while q.next is not None:
            q = q.next
        q.next = p
        p.next = None
    return prev
p = Node(2)
add(p, 4)
add(p, 7)
add(p, 1)
add(p, 16)
print_all(p)
print("____________")
print_all(reverse_rek(p))