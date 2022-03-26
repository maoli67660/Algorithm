class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def list2int(ls):
            str_int = ""
            p = ls
            while p:
                str_int = str_int + str(p.val)
                p = p.next
            return int(str_int)

        result_int = list2int(l1) + list2int(l2)
        head = ListNode(-1)
        p = head
        for item in str(result_int):
            i = int(item)
            p.next = ListNode(i)
            p = p.next
        return head.next


if __name__ == "__main__":
    #  test [1 -> 2 -> 3] + [2 -> 3] = [1 -> 4 -> 6]
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)

    p1.next = p2
    p2.next = p3
    solution = Solution()
    ls3 = solution.addTwoNumbers(p1, p2)
    while ls3:
        print(ls3.val)
        ls3 = ls3.next
