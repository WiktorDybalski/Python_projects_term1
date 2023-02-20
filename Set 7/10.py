# 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
# funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
# powstać nowa lista.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


pp = Node(0)
bp = Node(3)
cp = Node(7)
dp = Node(2)
ep = Node(1)
gp.next = bp
bp.next = cp
cp.next = dp
dp.next = ep

pq = Node(0)
bq = Node(3)
cq = Node(7)
dq = Node(2)
eq = Node(1)
gq.next = bq
bq.next = cq
cq.next = dq
dq.next = eq

pg = Node(0)
qg = Node(0)
gg = Node(0)
bg = Node(3)
cg = Node(7)
dg = Node(2)
eg = Node(1)
gg.next = bg
bg.next = cg
cg.next = dg
dg.next = eg



def print_all(p):
    while p is not None:
        print(p, end="")
        p = p.next
    print("")


def add(p, q, g):
    curr_p = p
    curr_q = q
    curr_g = g
    while curr_p is not None or curr_q is not None:

        if curr_p is not None and curr_q is None:
            curr_g.val += curr_p.val
            curr_g.next = curr_p.next
            return g
        elif curr_q is not None and curr_p is None:
            curr_g.val += curr_q.val
            curr_g.next = curr_q.next
            return g
        else:
            curr_g.val = curr_p.val + curr_q.val
            curr_p = curr_p.next
            curr_q = curr_q.next
            curr_g = curr_g.next


print_all(add(p.next, q.next, g.next))
