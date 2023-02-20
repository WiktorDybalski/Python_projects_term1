# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end=" => ")
        p = p.next
    print("")


tab = [Node(0) for _ in range(10)]

a = Node(15)
b = Node(34)
c = Node(1)
d = Node(6)
e = Node(19)
f = Node(11)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


def rozdziel(List, T):
    n = len(T)

    curr = List
    while curr is not None:
        last_digit = curr.val % 10
        x = curr
        curr = curr.next
        x.next = T[last_digit].next
        T[last_digit].next = x

    return T

def marche(T):
    g = Node(0)
    curr = g
    for i in range(0, len(T)):
        if T[i].next is not None:
            curr.next = T[i].next
            while curr.next is not None:
                curr = curr.next

    return g


tab = rozdziel(a, tab)

# for i in range(0, len(tab)):
#     print("Lista"+ str(i))
#     print_all(tab[i])

print_all(marche(tab))
















# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#     def __repr__(self):
#         return f'Node({str(self.val)})'
#
#
# def print_ll(ll: Node):
#     while ll is not None:
#         print(ll.val, end=' ')
#         ll = ll.next
#     print()
#
#
# def split(ll: Node):
#     curr = ll.next if ll.val is None else ll
#
#     part = [Node(None) for _ in range(10)]
#     lasts = [n for n in part]
#     while curr is not None:
#         nex = curr.next
#         i = curr.val % 10
#
#         lasts[i].next = curr
#         lasts[i] = lasts[i].next
#         lasts[i].next = None #curr.next = None
#
#         curr = nex
#
#     last = lasts[0]
#     for i in range(9):
#         last.next = part[i+1].next
#         if lasts[i+1].val is not None:
#             last = lasts[i+1]
#
#     return part[0]
#
#
#
# a = Node(3)
# b = Node(14)
# c = Node(4)
# d = Node(30)
#
# a.next = b
# b.next = c
# c.next = d
#
# ans = split(a)
# print_ll(ans)
