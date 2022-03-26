class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


'''class Solution:
    def flatten(self, head):
        p = head
        while p.child:
            p = p.next

if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("abc3[cd]xyz"))
'''

# --------------- test case -------------------
# p1 = Node(1)
# p2 = Node(2)
# p3 = Node(3)
# p4 = Node(4)
# p5 = Node(5)
# p6 = Node(6)
#
# p1.next = p2
# p2.prev = p1
#
# p2.next = p3
# p3.prev = p2
#
# p3.next = p4
# p4.prev = p3
#
# p4.next = p5
# p5.prev = p4
#
# p5.next = p6
# p6.prev = p5
#
# p7 = Node(7)
# p8 = Node(8)
# p9 = Node(9)
# p10 = Node(10)
#
# p3.child = p7
# p7.next = p8
# p8.prev = p7
#
# p8.next = p9
# p9.prev = p8
#
# p9.next = p10
# p10.prev = p9
#
# p11 = Node(11)
# p12 = Node(12)
# p8.child = p11
# p11.next = p12
# p12.prev = p11

p1 = Node(1)
p2 = Node(2)
p3 = Node(3)

p1.child = p2
p2.child = p3


# -------------------------------------------

def flat(head):
    p = head
    tail = p
    while p:
        tail = p
        # print('-- ', p.val)
        if p.child:
            q = p.next
            # get flatten child
            cp, cp_tail = flat(p.child)
            p.child = None
            print('cp = ', cp.val, '     cp_tail = ', cp_tail.val)
            # link flatten child
            p.next = cp
            cp.prev = p
            # link next nodes to tail of child
            cp_tail.next = q
            if q != None:
                q.prev = cp_tail
            else:
                q = cp_tail
            p = q
            print(p.val)
        else:
            p = p.next
    return head, tail


head, tail = flat(p1)
p = head
print('*' * 50)
while p:
    print(p.val)
    p = p.next
p = tail
print('=' * 50)
while p:
    print(p.val)
    p = p.prev
