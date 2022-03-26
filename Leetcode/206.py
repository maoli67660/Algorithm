# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


def print_ls(head):
    while head:
        print(head.val, '--->', end='')
        head = head.next
    print('')


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    solution = Solution()
    result = solution.reverseList(head)
    print(result)
    print_ls(result)
