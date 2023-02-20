# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next


def delete_elements(pointer):
    p = pointer
    if p.next is None:
        return
    else:
        delete_elements(p.next)
        if p.val > p.next.val:
            p.next = p.next.next


a = Node(15)
b = Node(34)
c = Node(1)
d = Node(6)
e = Node(19)

a.next = b
b.next = c
c.next = d
d.next = e

print_all(a)
print("-------")
delete_elements(a)
print_all(a)
