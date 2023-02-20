# 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end=" => ")
        p = p.next
    print("")


head = Node(0)
a = Node(15)
b = Node(34)
c = Node(1)
d = Node(5)
e = Node(19)

head.next = a
a.next = b
b.next = c
c.next = d
d.next = e

print_all(head)


def ile_5_w_ósemkowym(value):
    temp = value
    counter = 0

    while temp > 0:
        if temp % 8 == 5:
            counter += 1
        temp //= 8
    return counter % 2 == 0


def func(head):
    curr = head
    curr = curr.next

    while curr.next is not None:
        if ile_5_w_ósemkowym(curr.next.val):
            p = curr.next
            curr.next = curr.next.next
            p.next = head.next
            head.next = p
        else:
            curr = curr.next

    return head


print_all(func(head))


