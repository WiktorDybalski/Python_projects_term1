# 12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
# jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
# leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
# dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
# oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
# czy w wyniku operacji moc zbioru uległa zmianie.


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


w = Node(None)
a = Node("aa")
b = Node("ab")
c = Node("abc")
d = Node("fs")
e = Node("gh")
f = Node("tt")

w.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


def compare(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        cha, chb = ord(a[i]), ord(b[i])
        if cha < chb:
            return -1
        elif cha > chb:
            return 1
    if len(a) == len(b):
        return 0
    elif len(a) > len(b):
        return 1
    else:
        return -1


def func(p, s):
    while p.next is not None:
        cmp = compare(s, p.next.val)
        if cmp == -1:
            x = Node(s)
            x.next = p.next
            p.next = x
            return True
        elif cmp == 0:
            return False
        else:
            p = p.next
    p.next = Node(s)
    return True


print_all(w)

func(w, "bb")

print_all(w)

#
# def fun(List, key):
#     curr = List
#     flag = True
#     while curr.next is not None:
#         if curr.val == key:
#             flag = False
#         if curr.next.val > key:
#             curr.next = Node(key, curr.next)
#
#             break
#         curr = curr.next
#     print(flag)
#     return List
#
#
# print_all(fun(a, "bb"))
