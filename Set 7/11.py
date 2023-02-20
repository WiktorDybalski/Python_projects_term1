# 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end=" => ")
        p = p.next
    print("")


def length(a):
    counter = 0
    while a is not None:
        counter += 1
        a = a.next
    return counter


w = Node(0)
a = Node(356)
b = Node(34)
c = Node(1)
d = Node(6)
e = Node(15)
f = Node(16)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

tab = [0 for _ in range(length(a))]


# Wyrzuca powtórzenia z listy
# Przepisz tablice do listy wskaznikow bez powtorzen
def czy_usuwamy(a):
    curr = a
    i = 0
    while curr.next is not None:
        if curr.next.val in tab:
            curr.next = curr.next.next
        else:
            tab[i] = curr.next.val
            i += 1
            curr = curr.next
    return a


# print_all(czy_usuwamy(a))

# No i koks

def fun(List, key):
    curr = List
    flag = True
    while curr.next is not None:
        if curr.next.val == key:
            curr.next = curr.next.next
            flag = False
            break
        curr = curr.next
    if flag:
        curr.next = Node(key)
    return List


print_all(fun(a, 1))
