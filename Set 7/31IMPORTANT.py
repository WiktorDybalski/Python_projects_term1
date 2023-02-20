# 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next


def counter_deleted(pointer, pd, npu):
    counter = 0
    while pointer.next is not None:
        if pointer.next.val > 0 and pointer.next.val % 2 == 0:
            pd.next = pointer.next
            pointer.next = pointer.next.next
            counter += 1
        elif pointer.next.val < 0 and pointer.next.val % 2 == 1:
            npu.next = pointer.next
            pointer.next = pointer.next.next
            counter += 1
        else:
            pointer = pointer.next
    return counter


a0 = Node(0)
a = Node(-15)
b = Node(34)
c = Node(1)
d = Node(6)
e = Node(19)

a0.next = a
a.next = b
b.next = c
c.next = d
d.next = e

p = Node(0)
q = Node(0)

print_all(a0)
print("-----")
print(counter_deleted(a0, p, q))
print("-----")
print_all(p)
print("-----")
print_all(q)
print("-----")
print_all(a0)
