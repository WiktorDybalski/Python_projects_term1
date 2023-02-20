# 2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, idx, val, next=None):
        self.idx = idx
        self.val = val
        self.next = next


def atIdx(ll, idx):
    if ll.val is None:
        curr = ll.next
    else:
        curr = ll
    while curr is not None:
        if curr.idx == idx:
            return curr.val
        curr = curr.next


a = Node(0, 23)
b = Node(39, 42)
c = Node(55, 23)

a.next = b
b.next = c

print(atIdx(a, 0))
print(atIdx(a, 39))
