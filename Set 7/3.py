# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next

# def add(g, el):
#     if g.next is None:
#         q = Node(el)
#         g.next = q
#         return
#     else:
#         if g.next.val == el:
#             return
#         if g.next.val > el:
#             q = Node(el)
#             q.next = g.next
#             g.next = q
#             return
#         else:
#             add(g.next, el)


def merge_rek(p, q):
    if p is None:
        return q
    if q is None:
        return p
    if p.val <= q.val:
        p.next = merge_rek(p.next, q)
        return p
    q.next = merge_rek(p, q.next)
    return q


p = Node(0)
add(p, 4)
add(p, 7)
add(p, 1)
add(p, 16)

add(p, 2)
q = Node(0)
add(q, 3)
add(q, 5)
add(q, 9)
add(q, 12)

add(q, 1)
print_all(p.next)
print("_________________")
print_all(q.next)

print("_________________")

print_all(merge_rek(p.next, q.next))
print("_________________")


def merge(p, q):
    g = Node(0)
    if p.next is None and q.next is None:
        return None
    while p.next is not None or q.next is not None:
        while p.val <= q.val:
            add(g, p.val)
            p = p.next
        while p.val > q.val:
            add(g, q.val)
            q = q.next
    if p.next is None:
        while q is not None:
            add(g, q.val)
            q = q.next
    else:
        while p is not None:
            add(g, p.val)
            p = p.next
    return g.next


print_all(merge(p.next, q.next))
