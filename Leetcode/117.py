class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        queue = [(root, 0)]
        while queue:
            top = queue.pop(0)
            level = top[1] + 1
            print('val=', top[0].val, '    level=', top[1])
            if top[0].next:
                print('   next = ', top[0].next.val)

            if top[0].left is not None:
                if queue and queue[-1][1] == level:
                    queue[-1][0].next = top[0].left
                queue.append((top[0].left, level))
            if top[0].right is not None:
                if queue and queue[-1][1] == level:
                    queue[-1][0].next = top[0].right
                queue.append((top[0].right, level))


p1 = Node(1)
p2 = Node(2)
p3 = Node(3)
p1.left = p2
p1.right = p3
p4 = Node(4)
p5 = Node(5)
p2.left = p4
p2.right = p5

p6 = Node(6)
p7 = Node(7)
p3.left = p7
p3.right = p7

solution = Solution()
solution.connect(p1)
