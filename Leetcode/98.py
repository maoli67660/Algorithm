# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root) -> bool:
        if root == None:
            return True

        isValidLeft = True
        isValidRight = True

        if root.left != None:
            isValidLeft = root.left.val < root.val
        if root.right != None:
            isValidRight = root.val < root.right.val

        return isValidLeft and isValidRight and self.isValidBST(root.left) and self.isValidBST(root.right)

    def isValidBST_2(self, root) -> bool:
        pre_order_ls = []

        def pre_order(p):
            if p:
                pre_order(p.left)
                pre_order_ls.append(p.val)
                pre_order(p.right)

        pre_order(root)
        for i in range(len(pre_order_ls) - 1):
            if not pre_order_ls[i] < pre_order_ls[i + 1]:
                return False
        return True


if __name__ == '__main__':
    # [10, 5, 15, null, null, 6, 20]
    p1 = TreeNode(10)
    p2 = TreeNode(5)
    p3 = TreeNode(15)
    p1.left = p2
    p1.right = p3

    p4 = TreeNode(6)
    p5 = TreeNode(20)
    p3.left = p4
    p3.right = p5
    solution = Solution()
    result = solution.isValidBST_2(p1)
    print("result = ", result)
