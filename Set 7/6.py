# 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def put_at_the_end(p, value):
    curr = p
    curr.next = p.next
    while True:
        if curr.next is None:
            g = Node(value)
            curr.next = g
            return p
        curr = curr.next


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
print_all(put_at_the_end(a, 17))
