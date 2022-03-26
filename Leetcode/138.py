# Definition for a Node.
'''

思路：
两次两次遍历 目标表
第一次遍历： 会略random， 拷贝next和val。
   字典 p_add2index 记录目标表p 指针->索引
   字典 q_index2add 记录目标表q 索引->指针

第二次遍历：
    从 p_add2index表知道 当前p.random->索引->q表指正，赋值给q.random
    从而赋值random关系

注意点：
    空指针的在 map中的处理
    头结点 尾插法简历链表
'''

class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head):
        p = head
        q_head = Node(-1)
        q = q_head
        index = 0
        q_index2add = {}
        p_add2index = {}

        while p:
            q.next = Node(p.val)
            p_add2index[p] = index
            q_index2add[index] = q.next

            q = q.next
            p = p.next
            index = index + 1
        q = q_head.next
        p = head

        while p:
            if p.random:
                index = p_add2index[p.random]
                q_random_point = q_index2add[index]
                q.random = q_random_point
            else:
                q.random = None
            p = p.next
            q = q.next

        return q_head.next

if __name__ == '__main__':
    p1 = Node(7)
    p2 = Node(13)
    p3 = Node(11)
    p4 = Node(10)
    p5 = Node(1)

    p1.next = p2
    p1.random = None

    p2.next = p3
    p2.random = p1

    p3.next = p4
    p3.random = p5

    p4.next = p5
    p4.random = p3

    p5.next = None
    p5.random = p1

    solution = Solution()
    q = solution.copyRandomList(p1)
    # q = p1
    while q:
        print("q.val = ", q.val)
        if q.next:
            print("q.next = ", q.next.val)
        else:
            print("q.next = null")
        if q.random:
            print("q.random = ", q.random.val)
        else:
            print("q.random = null")
        print('-----------------')
        q = q.next
