# Definition for singly-linked list.
'''


'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode):
        if not head:
            return False
        p_fast, p_slow = head.next, head

        while p_slow and p_fast and p_fast.next:
            if p_fast == p_slow:
                return True
            p_fast = p_fast.next.next
            p_slow = p_slow.next
        return False


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(3)

    solution = Solution()
    result = solution.hasCycle(head)
    print(result)
