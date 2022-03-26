class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        p = self
        while p:
            yield p.value
            p = p.next

    def __repr__(self):
        return str(list(self))

    def delete(self, key):
        pre, p = None, self
        while p:
            if p.value == key:
                if pre:
                    pre.next = p.next
            pre = p
            p = p.next


def reverse(node):
    if node is None:
        return node
    pre, p = None, node
    while p:
        temp = p.next
        p.next = pre
        pre = p
        p = temp
    return pre


def has_circle(node):
    if node is None or node.next is None:
        return False
    p1, p2 = node, node.next
    while (p2 is not None) and (p2.next is not None):
        if p1 == p2:
            return True
        p1 = p1.next
        p2 = p2.next.next
    return False


def palindrome(node):
    pass


def merge_ll(n1, n2):
    head = Node(-1)
    tail = head
    while (n1 is not None) and (n2 is not None):
        if n1.value > n2.value:
            p = n2
            n2 = n2.next
        else:
            p = n1
            n1 = n1.next
        tail.next = p
        tail = tail.next
    if n1 is not None:
        tail.next = n1
    else:
        tail.next = n2

    return head.next


def delete_last_k(node, k):
    kp = node
    for i in range(k):
        if kp:
            kp = kp.next
        else:
            return False
    if kp is None:
        return node.next
    pre = node
    while kp.next:
        pre = pre.next
        kp = kp.next
    pre.next = pre.next.next
    return node


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n1.next = n2
    n2.next = n3

    l1 = Node(2)
    l2 = Node(6)
    l1.next = l2

    merge_ll = merge_ll(n1, l1)
    print(merge_ll)
    merge_ll.delete(3)
    print(merge_ll)
    print(delete_last_k(merge_ll, 4))
