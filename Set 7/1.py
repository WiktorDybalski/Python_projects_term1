# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next


def is_present(g, el):
    if g.next is None:
        return False
    else:
        if g.next.val > el:
            return False
        if g.next.val == el:
            return True
        if g.next.val < el:
            return is_present(g.next, el)


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


def delete(g, el):
    if g.next is None:
        return

    while g.next is not None:
        if g.next.val == el:
            g.next = g.next.next
            return
        else:
            g = g.next


def delete_rek(g, el):
    if g.next is None:
        return

    if g.next.val == el:
        g.next = g.next.next
        return
    else:
        return delete(g.next, 7)


g = Node(0)
add(g, 7)
add(g, 3)
add(g, 13)
add(g, 23)
print_all(g.next)
print(is_present(g, 7))
delete(g, 3)
print_all(g.next)


