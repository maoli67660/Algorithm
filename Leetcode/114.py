# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        pass

# ===================
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)
p6 = TreeNode(6)
p1.left = p2
p1.right = p5
p2.left = p3
p2.right = p4
p5.right = p6


def flat(root):
    if root == None:
        print('None节点')
        return None, None
    if root.left == None and root.right == None:
        print('叶子')
        return root, root
    if root.left != None and root.right == None:
        print('右空')
        return root, flat(root.left)[1]

    if root.left == None and root.right != None:
        print('左空')
        root.left = root.right
        root.right = None
        return root, flat(root.left)[1]

    if root.left != None and root.right != None:
        left_head, left_tail = flat(root.left)
        right_head, right_tail = flat(root.right)
        left_tail.left = right_head
        root.right = None
        return root, right_tail


root, tail = flat(p1)
p = root
while p != None:
    p.right = p.left
    p.left = None
    p = p.right

p = root
while p != None:
    print(p.val)
    p = p.right