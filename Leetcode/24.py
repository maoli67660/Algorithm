# Definition for singly-linked list.
'''

在纸上画好图， 用红笔一链接指针一条链接指针的切。 标上操作序号，注意切断的顺序

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if not (head and head.next):
            return head


        new_head = head.next
        head.next = new_head.next
        new_head.next = head


        prev = new_head.next
        curr = prev.next
        while curr and curr.next:
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = curr

            prev = curr
            curr = prev.next

        return new_head

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
    result = solution.swapPairs(head)
    print(result)
    print_ls(result)
