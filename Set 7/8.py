# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def delete_elements(p):
    curr = p
    i = 0
    while curr.next is not None:
        i += 1
        if i % 2 == 1:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return p


a = Node(15)
b = Node(34)
c = Node(1)
d = Node(6)
e = Node(19)

a.next = b
b.next = c
c.next = d
d.next = e


def print_all(a):
    while a is not None:
        print(a.val)
        a = a.next


print_all(a)
print("-------------")
p = delete_elements(a)
print_all(p)
