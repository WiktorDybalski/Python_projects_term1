# 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def delete_at_the_end(a):
    curr = a
    if curr.next.next is None:
        curr.next = curr.next.next
    else:
        delete_at_the_end(curr.next)
    return a


a = Node(15)
b = Node(34)
c = Node(1)
d = Node(6)

a.next = b
b.next = c
c.next = d


def print_all(a):
    while a is not None:
        print(a.val)
        a = a.next


print_all(a)
print("-------------")
p = delete_at_the_end(a)
print_all(p)
