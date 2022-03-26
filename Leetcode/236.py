# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_dic = {root: 0}  # mapping current p -> parent p

        def pre_visit(p):
            if p:
                if p.left:
                    parent_dic[p.left] = p
                if p.right:
                    parent_dic[p.right] = p
                pre_visit(p.left)
                pre_visit(p.right)

        pre_visit(root)

        p_parent_ls = []
        p_parent = p
        while p_parent != 0:
            p_parent_ls.append(p_parent)
            p_parent = parent_dic[p_parent]

        q_parent_ls = []
        q_parent = q
        while q_parent != 0:
            q_parent_ls.append(q_parent)
            q_parent = parent_dic[q_parent]
        q_parent_ls.reverse()
        p_parent_ls.reverse()

        for i in range(min(len(q_parent_ls), len(p_parent_ls))):
            if p_parent_ls[i] != q_parent_ls[i]:
                return p_parent_ls[i - 1]

        return p_parent_ls[i]


if __name__ == '__main__':
    p3 = TreeNode(3)
    p5 = TreeNode(5)
    p1 = TreeNode(1)
    p3.left = p5
    p3.right = p1

    p6 = TreeNode(6)
    p2 = TreeNode(2)
    p5.left = p6
    p5.right = p2

    p7 = TreeNode(7)
    p4 = TreeNode(4)
    p2.left = p7
    p2.right = p4

    p0 = TreeNode(0)
    p8 = TreeNode(8)
    p1.left = p0
    p1.right = p8

    solution = Solution()
    result = solution.lowestCommonAncestor(p3, p5, p4)
    print('result = ', result.val)
